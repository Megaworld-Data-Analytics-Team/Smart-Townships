# Person-and-Vehicle-Counter

## Steps:

### Clone Repository
```
$git clone https://github.com/Megaworld-Data-Analytics-Team/Person-and-Vehicle-Counter.git
```

### Generate Tensorflow model of YOLOv3
1. Download pre-trained weights of YOLOv3 and YOLOv3 Tiny
  - https://pjreddie.com/media/files/yolov3.weights
  - https://pjreddie.com/media/files/yolov3-tiny.weights
2. Save weights to the repository's ./weights folder
3. Execute the following code in Anaconda prompt (cd *local directory*)

For YOLOv3:
```
python convert.py
```
For YOLOv3 tiny:
```
python convert.py --weights ./weights/yolov3-tiny.weights --output ./weights/yolov3-tiny.tf --tiny
```

### Run Person and Vehicle Counter
Using YOLOv3 Model:
```
main.ipynb
```
Using YOLOv3 Tiny Model:
```
main_tiny.ipynb
```

## Test Data
https://drive.google.com/file/d/1hMTFYq6_LsXYuDdMp_da94fHx39hlWgQ/view?usp=sharing
Note: save test data to ./data/video folder

## References:
Python: Real-time Multiple Object Tracking (MOT) with Yolov3, Tensorflow and Deep SORT [FULL COURSE] by eMaster Class Academy
https://youtu.be/zi-62z-3c4U
