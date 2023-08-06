from label_studio_ml.model import LabelStudioMLBase
import numpy as np
from fast_label_studio import brush
import PIL.Image
from io import BytesIO
import requests
from fastai.vision.all import tensor
from fastai.vision.all import *
from typing import List, Tuple
from dotenv import load_dotenv
import os
load_dotenv() 

API_TOKEN = os.environ["API_TOKEN"]
HOST = os.environ["LABEL_STUDIO_HOST"]

get_msk = lambda o: Path(str(o).replace("orig.jpg", "mask_grey.png"))

def read_img(p):
    response = requests.get(f"{HOST}{p}", headers={'Authorization': f'Token {API_TOKEN}'})
    image = PIL.Image.open(BytesIO(response.content))
    return tensor(image)
    

class SegmentationModel(LabelStudioMLBase):
    def __init__(self, labels: List[str], input_shape: Tuple[int, int], model_path: str, **kwargs):
        """SegmentationModel initialization

        Args:
            labels (List[str]): list of labels (must include background)
            input_shape (Tuple[int, int]): input shape (height, width)
            model_path (str): path to latest model
        """
        super(SegmentationModel, self).__init__(**kwargs)
        self.labels = labels
        self.input_shape = input_shape
        self.model = load_learner(Path(model_path))

    def predict(self, tasks, **kwargs):
        from_name, schema = list(self.parsed_label_config.items())[0]
        to_name = schema["to_name"][0]
        print(from_name, to_name, len(tasks))
        images = []
        for task in tasks:
            p = task["data"]["image"]
            images.append(read_img(p))
            
    
        test_dl = self.model.dls.test_dl(images)
        preds = self.model.get_preds(dl=test_dl)
        results = []
        for pred in preds[0]:
            predictions = []
            mask = pred.argmax(dim=0)
            for i in range(pred.shape[0]):
                new_mask = np.zeros(self.input_shape, dtype=np.uint8)
                new_mask[mask == i] = 100
                rle = brush.mask2rle(new_mask)
                predictions.append(
                            {
                                "from_name": from_name,
                                "to_name": to_name,
                                "type": "brushlabels",
                                "original_width": self.input_shape[1],
                                "original_height": self.input_shape[0],
                                "image_rotation": 0,
                                "value": {
                                    "brushlabels": [self.labels[i]],
                                    "format": "rle",
                                    "rle": rle,
                                },
                                "score": 0.5,
                            }
                )
            
        
            results.append({ "result": predictions })
        
        return results
    