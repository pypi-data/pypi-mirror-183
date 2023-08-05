import cv2
from PIL import Image

print('로드 성공')

def imgload(Imgpath):
    img = cv2.imread(Imgpath)
    if img is None:
        img = Image.open(Imgpath)
        img = cv2.cvtColor(np.uint8(img), cv2.COLOR_BGR2RGB)
    return img