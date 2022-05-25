# Smart Townships

Welcome to the Smart Townships repository! The repository includes automated counting of persons and vehicles in video streams. The counter programs are implemented either through YOLOv3 models or OpenVINO Intel Models. You may view instructions on these corresponding sections below.
Moreover, additional programs on demographic and sentiment prediction based on facial features are also included. 

## Clone Repository
```
$git clone https://github.com/Megaworld-Data-Analytics-Team/Person-and-Vehicle-Counter.git
```

## YOLOv3 Models
### Obtain Tensorflow model of YOLOv3 / YOLOv3 Tiny

For YOLOv3:
1. Download pre-trained weights of YOLOv3:
    - https://pjreddie.com/media/files/yolov3.weights
2. Save yolov3.weights to ./weights folder
3. Download the checkpoint/tf files, then save to repository under ./checkpoints
    - https://drive.google.com/drive/folders/1LeBnZjTcvEAZkkcmBgeLWS4_Ha-On26v?usp=sharing <br />

For YOLOv3 tiny:
1. Download pre-trained weights of YOLOv3 Tiny
    - https://pjreddie.com/media/files/yolov3-tiny.weights
2. Save weights to the repository's ./weights folder
3. Execute the following code in Anaconda prompt (cd *local directory*):
```
python convert.py --weights ./weights/yolov3-tiny.weights --output ./checkpoints_tiny/yolov3-tiny.tf --tiny
```
You may also download the generated Tensorflow models through the following link (then save to ./weights):
https://drive.google.com/drive/folders/1CqP1sA0fdmyhopt4iuoIk2Om7HLWIGUf?usp=sharing <br />


### Run Person and Vehicle Counter
Located at: *notebooks/person and vehicle counter/original*  
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
<br />


## OpenVINO Intel Models

### Install OpenVINO Development Tools
Follow the steps: https://docs.openvino.ai/latest/openvino_docs_install_guides_install_dev_tools.html

### Run Person and Vehicle Counter Using OpenVINO Models
1. In command terminal:
    - Activate OpenVINO Virtual Environment
    - Launch Jupyter Notebook/Jupyter Lab
2. Execute the code in the repository:
    Located at: *notebooks/person and vehicle counter/openvino*  
    Counter with DeepSORT Tracking (optimal):
    ```
    main_whole-frame_OpenVINO_DeepSORT
    ```
    Counter with Centroid Tracking
    ```
    main_whole-frame_OpenVINO_CentroidTracker
    ```
<br />

## Test Data
(UPDATED 5-16-2022) <br />
Download: https://drive.google.com/drive/folders/1_pF952TQmR4aCSZYXuGDmhgPKDkJBwRR?usp=sharing <br />
Note: save the downloaded 'video' folder to ./data folder <br />


## References:
Python: Real-time Multiple Object Tracking (MOT) with Yolov3, Tensorflow and Deep SORT [FULL COURSE] by eMaster Class Academy <br />
https://youtu.be/zi-62z-3c4U
<br />


# Facial Sentiment Detection
## Steps
1. Download prediction models and save them to directory
    - https://drive.google.com/drive/folders/1DbiBhYoROeKZy58umuORPKs13rGwDd5d?usp=sharing
2. Run the code:  
Located at: *notebooks/demographics and sentiment detection*  
Haarcascades Version:
```
Age, Gender, and Emotion Detection.ipynb
```
OpenVINO Version
```
Demographics-and-Sentiment_Detection
```
