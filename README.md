# Person-and-Vehicle-Counter

## Steps

### Clone Repository
```
$git clone https://github.com/Megaworld-Data-Analytics-Team/Person-and-Vehicle-Counter.git
```

### Obtain Tensorflow model of YOLOv3 / YOLOv3 Tiny

For YOLOv3:
1. Download pre-trained weights of YOLOv3:
    - https://pjreddie.com/media/files/yolov3.weights
2. Save yolov3.weights to ./weights folder
3. Download the checkpoint/tf files, then save to repository under ./checkpoints
    - https://drive.google.com/drive/folders/1LeBnZjTcvEAZkkcmBgeLWS4_Ha-On26v?usp=sharing

For YOLOv3 tiny:
1. Download pre-trained weights of YOLOv3 Tiny
    - https://pjreddie.com/media/files/yolov3-tiny.weights
2. Save weights to the repository's ./weights folder
3. Execute the following code in Anaconda prompt (cd *local directory*):
```
python convert.py --weights ./weights/yolov3-tiny.weights --output ./checkpoints_tiny/yolov3-tiny.tf --tiny
```
You may also download the generated Tensorflow models through the following link (then save to ./weights):
https://drive.google.com/drive/folders/1CqP1sA0fdmyhopt4iuoIk2Om7HLWIGUf?usp=sharing


### Run Person and Vehicle Counter
Using YOLOv3 Model (with Detection Zone):
```
main.ipynb
```
Using YOLOv3 Tiny Model (with Detection Zone):
```
main_tiny.ipynb
```
Using YOLOv3 Model (detects on Whole Frame):
```
main_whole-frame.ipynb
```
Using YOLOv3 Tiny Model (detects on Whole Frame):
```
main_tiny_whole-frame.ipynb
```


## Test Data
(UPDATED 5-16-2022)
Download: https://drive.google.com/drive/folders/1_pF952TQmR4aCSZYXuGDmhgPKDkJBwRR?usp=sharing
Note: save the downloaded 'video' folder to ./data folder


## References:
Python: Real-time Multiple Object Tracking (MOT) with Yolov3, Tensorflow and Deep SORT [FULL COURSE] by eMaster Class Academy
https://youtu.be/zi-62z-3c4U

# Facial Sentiment Detection
## Steps
1. Download prediction models and save them to directory
    - https://drive.google.com/drive/folders/1DbiBhYoROeKZy58umuORPKs13rGwDd5d?usp=sharing
2. Run the code:
```
Age, Gender, and Emotion Detection.ipynb
```
