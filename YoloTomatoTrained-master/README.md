# Youtube Link 
#### [https://www.youtube.com/watch?v=RXmJ54QYwvc](https://www.youtube.com/watch?v=RXmJ54QYwvc) 


[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/73653940/232318929-088736c2-7f49-4a6f-a580-5a6afbc05267.png)](https://www.youtube.com/watch?v=RXmJ54QYwvc)



# Project Desciption

Agricultural yield and to maintain high-quality produce. The study of plant diseases involves analyzing observable patterns in the plant using the naked eye. Plant health monitoring and disease detection are crucial for achieving sustainable agriculture. However, monitoring plant diseases manually is challenging, requiring a considerable amount of labor, expertise in the field of plant diseases, and lengthy processing times. Despite the significant improvement in machine learning (ML) and predictive analysis efficiency for the classification of diseased plants remains very limited to the dataset provided. Thus causing a delay in the generation of reports. Our project uses the machine-learning classification algorithm to distinguish healthy crops from diseased ones. The outcome of this research will be a report that includes the percentage of diseased and healthy crops, along with the type of disease and its respective remedies. For the conducted experiments, the YOLOv5 model yielded the best performance of 92% in terms of accuracy and proved to be more efficient in identifying crop damage compared to manual sorting. Additionally, the system developed contains a sensor-based device that measures the pH, moisture, temperature, and TDS of soil to ensure optimal conditions for plant growth. Implementation of this proposed method has the potential to significantly increase crop yield and reduce losses caused by disease, thereby benefiting farmers and consumers alike.


# Graphs

![P_curve](https://user-images.githubusercontent.com/73653940/232319915-b4ae99cb-211f-42b0-a123-88de196a89ef.png)
![R_curve](https://user-images.githubusercontent.com/73653940/232319919-fe44395e-be09-43e7-ad2a-06c224a9b0c8.png)
![confusion_matrix](https://user-images.githubusercontent.com/73653940/232319923-ba61f6de-b46b-408e-a766-584dd76b25b7.png)
![F1_curve](https://user-images.githubusercontent.com/73653940/232319924-f537e694-ff9c-4da4-a1c7-5f3dc87da088.png)


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


# Project Link
## [ http://34.131.211.246/farm-video-upload/]( http://34.131.211.246/farm-video-upload/) 
- Username : admin
- Password : qwerty123@#


