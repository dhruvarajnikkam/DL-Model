import cv2
from core.models import VideoFarmImages, FarmVideo
import os
import cv2
from django.core.files import File

from core.tasks import *
from multiprocessing import Process


def convert_video_images(video_id):
    farm_video = FarmVideo.objects.get(id=video_id)
    # get video path
    video_path = farm_video.video.path
    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Calculate delay from desired FPS
    fps = 5
    delay = int(1000 / fps)

    # Initialize frame counter
    frame_count = 0

    # Loop over frames
    while cap.isOpened():
        # Read frame
        ret, frame = cap.read()
        if not ret:
            farm_video.status="completed"
            farm_video.save()
            break

        # Capture one frame per FPS
        if frame_count % fps == 0:
            # Process frame here (e.g. run YOLOv5 model)
 

            # Display frame (optional)
            file_name = f"frame{frame_count:04d}.jpg"
            cv2.imwrite(file_name, frame)
            save_frame(video_id, file_name)

        frame_count += 1

    # Release video file
    cap.release()


# s="/home/abhishek/Downloads/git-clones/yolov5/runs/detect/exp6/test_video.mp4"
# get_video(s)
def save_frame(video_id, file_name):
    # Open saved file
    with open(file_name, "rb") as f:
        # Create Django file object
        django_file = File(f)

        # Create new VideoFrame instance
        vf = VideoFarmImages(farm_video_id=video_id)

        # Set Django file object as the image field
        vf.image.save(file_name, django_file, save=True)

        detact_obj=DetactFarmImages.objects.create(farm_images=vf)

        p = Process(target=detect_images, args=( vf.id,detact_obj.id))
        p.start()
        print("frame completed desginse ",detact_obj)

    # Delete temporary file
    os.remove(file_name)
