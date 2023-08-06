import os
import cv2
import time
import numpy as np


class MouseHandler:
    def __init__(self, width, height, crop_size=64):
        self.w = width
        self.h = height
        self.x = self.w // 2
        self.y = self.h // 2
        self.s = crop_size

    def mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.x = x % self.w
            self.y = y % self.h

    def get_crop_rect(self):
        x, y, s = self.x, self.y, self.s
        h, w = self.h, self.w

        x1 = x - s // 2
        y1 = y - s // 2

        x1 = np.clip(x1, 0, w - s - 1)
        y1 = np.clip(y1, 0, h - s - 1)

        x2 = x1 + s
        y2 = y1 + s

        return x1, y1, x2, y2


def compare(images: list, crop_size: int = 64, zoom: int = 4):
    mh = MouseHandler(images[0].shape[1], images[0].shape[0], crop_size)
    cv2.namedWindow("image-compare")
    cv2.setMouseCallback("image-compare", mh.mouse_event, None)

    zoom_size = (crop_size * zoom, crop_size * zoom)
    while True:
        x1, y1, x2, y2 = mh.get_crop_rect()
        views = []
        crops = []
        for image in images:
            view = image.copy()

            crops.append(
                cv2.resize(
                    image[y1:y2, x1:x2], zoom_size, interpolation=cv2.INTER_NEAREST
                )
            )

            cv2.rectangle(view, (x1, y1), (x2, y2), (0, 255, 0), 1)
            views.append(view)

        views = np.concatenate(views, 1)
        crops = np.concatenate(crops, 1)
        cv2.imshow("image-compare", views)
        cv2.imshow("image-crops", crops)
        key = cv2.waitKey(30)

        if key == 27:
            break
        if key == ord("c"):
            capture_dir = "./captures"
            os.makedirs(capture_dir, exist_ok=True)
            capture_path = os.path.join(capture_dir, f"{time.time_ns()}.png")
            cv2.imwrite(capture_path, crops)
            print("Capture Image ->", capture_path)

    cv2.destroyAllWindows()
