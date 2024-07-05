from ultralytics import YOLO
import cv2

# обучение
# model = YOLO('yolov9e.pt', task='detect')
# model.info()
# print(model.names)
# results = model.train(data='data.yaml', epochs=2, imgsz=640)


model = YOLO('best.pt')  # подгружаю свою модель
# проверка на пикче
res = model.predict("C:\\Users\\Makovey\\Ultralytics result\\datasets\\0\\images\\000f13aff94499d03e3997afc55b0aa0.png")
img = res[0].plot()
while True:
    cv2.imshow('plain', img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
