from pathlib import Path
from ultralytics import YOLO
def main():
    model=YOLO("yolov8n.pt")
    img_source="images/bus.jpg"
    results=model.predict(source=img_source,conf=0.25,verbose=True)
    if not results:
        raise RuntimeError("No detection results")
    output_path=Path("result.jpg")
    results[0].save(filename=str(output_path))
    print("Detection successful")
    boxes=results[0].boxes
    if boxes is None or len(boxes)==0:
        print("No objects detected")
    else:
        print("\nDetected objects:")
        for class_id, confidence in zip(boxes.cls.tolist(),boxes.conf.tolist()):
            class_name=model.names[int(class_id)]
            print(f"class = {class_name} - {confidence} confidence")
if __name__ == "__main__":
    main()