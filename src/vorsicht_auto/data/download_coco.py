import os
import shutil
import fiftyone as fo
import fiftyone.zoo as foz

TRAFFIC_CLASSES = [
    "car", "truck", "bus", "motorcycle", "bicycle", "train",
    "traffic light", "stop sign",
    "person", "dog", "horse"
]
fo.config.dataset_zoo_dir = "data/raw"

dataset = foz.load_zoo_dataset(
    "coco-2017",
    label_types=["detections"],
    classes=TRAFFIC_CLASSES,
    max_samples=100,
)

print("Dataset downloaded to", fo.config.dataset_zoo_dir)