# YOLOv8 Object Detection

## Overview
This project demonstrates basic object detection using the pre-trained **YOLOv8 Nano (yolov8n.pt)** model from Ultralytics. The script detects objects in an input image, saves the annotated output image with bounding boxes, and prints the detected object names with their confidence scores.

## Requirements

- Python 3.x
- ultralytics

Install the required packages:

```bash
pip install -r requirements.txt
```

## Project Files

```
.
├── detect.py
├── requirements.txt
├── images/
│   └── bus.jpg
├── results.jpg
└── README.md
```

## Running the Project

Execute the following command:

```bash
python detect.py
```

## Output

- `results.jpg` – Image with detected objects and bounding boxes.
- Console output showing detected object names and confidence scores.

## Model Used

- **YOLOv8 Nano (`yolov8n.pt`)** – A lightweight pre-trained object detection model provided by Ultralytics.
