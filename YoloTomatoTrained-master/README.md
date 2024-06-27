# Technology 
- Yolov5 Model
- Colab Pro
- Google Cloud AMD for Hosting Applcation
- Django Web Server
- HTML/CSS JS






# YoloTomatoTrained
The code you provided is a Python script that uses YOLOv5 to train a custom object detection model on a corn 
dataset, and then performs object detection on a video file using the trained model.
Next, it loads the pre-trained YOLOv5s model using the torch.hub.load() function:

Then, it trains a custom YOLOv5 model on a corn dataset using the train.py script by running the following command:

This command specifies the input source (--source $video_path), the path to the trained model weights 
(--weights /content/drive/MyDrive/YOLO-LealDisease-Detection-main/yolov5/runs/train/exp12/weights/best.pt), and the 
confidence threshold for object detection (--conf 0.2). The script uses YOLOv5 to detect objects in each frame of the
video and outputs the results as a video with bounding boxes around the detected objects.

Overall, this script demonstrates how to use YOLOv5 to train a custom object detection model on a specific dataset 
and perform object detection on video files using the trained model.
