import os
HOME = os.getcwd()
print(HOME)

import ultralytics
ultralytics.checks()

import torch
from ultralytics import YOLO

def main():
    #Free GPU memory
    torch.cuda.empty_cache()

    # Model Size 'n' for nano, 's' for small, 'm' for medium, 'l' for large, 'x' for extra large
    model_size = 'l'  # Change this to 'n', 's', 'm', 'l', or 'x' as needed

    model_name = f'yolov8{model_size}.pt'
    model = YOLO(model_name)
    model.model.load_pretrained = False

    # Move model to GPUs
    model = model.cuda()

    dloc = f"{HOME}/Robotdataset/"

    print(f"Training YOLOv8{model_size.upper()} model...")

    train_config = {
        'epochs': 100,
        'batch': 32,
        'imgsz': 308,
        'device': '0',
        'data': f"{dloc}data.yaml",
        'project': 'runs/train',
        'name': 'experiment',
        'save_period': 50,
        'verbose': True
    }

    model.train(**train_config)
    model.save(f'yolov8_{model_size}.pt')

if __name__ == '__main__':
    main()