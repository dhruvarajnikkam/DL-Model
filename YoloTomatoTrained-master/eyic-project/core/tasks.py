from celery import shared_task
from .models import *
import cv2
import torch
from PIL import Image

model = torch.hub.load(
    "ultralytics/yolov5", "custom", "/home/abhishek/Downloads/software/weights/best.pt"
)



@shared_task
def detect_images(image_id,deact_farm_id):
    image_path = VideoFarmImages.objects.get(id=image_id).image.path
    results = model(image_path)
    df = results.pandas().xyxy[0]
    
    detact_obj=DetactFarmImages.objects.get(id=deact_farm_id)

    # detact_obj=DetactFarmImages.objects.create(farm_images__id=image_id)
    for i in df["name"]:
        # detact_obj=DetactFarmImages.objects.create(farm_images_id=image_id)

        if i.strip():
            disease_obj = Disease.objects.get(name=i)
            print("disease_obj",disease_obj)
            detact_obj.disease_detected.add(disease_obj)

        detact_obj.save()
    

    # print(image_id, results.pandas[])
    # print(results, results.print())

    return results


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
