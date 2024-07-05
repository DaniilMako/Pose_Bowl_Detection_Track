import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Загрузка изображения
image = Image.open("00a3812a62f3e6c2e2e494d610ea3d39.png")
# image = Image.open("/kaggle/working/images/000dbf763348037b46558bbcb6a032ac.png")
plt.imshow(image)

# Загрузка маски
with open("00a3812a62f3e6c2e2e494d610ea3d39.txt", "r") as file:
    # with open("/kaggle/working/labels/000dbf763348037b46558bbcb6a032ac.txt", "r") as file:
    lines = file.readlines()

#834,826,921,842
def draw_yolo():
    # Применение маски к изображению
    for line in lines:
        class_id, x_center, y_center, width, height = map(float, line.split())
        print('coordinates:\n', x_center, y_center, width, height)
        # print(image.width, image.height)
        left = (x_center - width / 2) * image.width * 2
        top = (y_center - height / 2) * image.height * 2
        rect_width = width * image.width - left
        rect_height = height * image.height - top
        print('left, top, rect_width, rect_height:\n', left, top, rect_width, rect_height)
        rect = patches.Rectangle((left, top), rect_width, rect_height, linewidth=3, edgecolor='b', facecolor='none')
        plt.gca().add_patch(rect)

    plt.show()


def draw_coco():
    image = cv2.imread("00a3812a62f3e6c2e2e494d610ea3d39.png")
    # 960,192,1066,293
    cv2.rectangle(image, (960,192), (1066,293), (0, 255, 0), 2)
    image = cv2.resize(image, None, fx=0.8, fy=0.8)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# draw_yolo()
draw_coco()
