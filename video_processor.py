from ultralytics import YOLO
import os


def main():
    model = YOLO("yolov8m-seg.pt")
    results = model.track(source=os.getcwd() + "/Videos/Shot One Decent Camera Movement.mp4", show=True, save=True)


if __name__ == "__main__":
    main()