import ultralytics
from ultralytics import YOLO
import wandb
from wandb_callback import callbacks

ultralytics.checks()
  
wandb.login(key='6d95c1525f637135175b2cf7e8ef4d653f6d3b6f')
wandb.init(entity="benw1",project = "wild_grass",settings=wandb.Settings(start_method="thread"))

ymodel = YOLO("/homes/bweinhold/CIS_732/ultralytics/yolov8x.pt")
#ymodel = YOLO("/homes/bweinhold/CIS_732/runs/detect/train2/weights/best.pt")

for event,func in callbacks.items():
    ymodel.add_callback(event,func)

ymodel.train(data="/homes/bweinhold/CIS_732/80-10-10-balanced_set/split_balanced.yaml", epochs=200, imgsz=640)
    
