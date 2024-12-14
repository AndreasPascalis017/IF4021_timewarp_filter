import cv2
import time

cap = cv2.VideoCapture(0)

threshold = 1
ret, temp = cap.read()
lasth = 0
newing = temp.copy()
upsidedown = False

print(temp.shape)
while True:
    ret, img = cap.read()
    img = cv2.flip(img, int(not upsidedown))
    if (type(img) == type(None)):
        break
    temp[lasth:lasth + threshold] = img[lasth:lasth +threshold]

    newing[0: lasth] = temp[0: lasth]
    newing[lasth:-1] = img[lasth:-1]
    cv2.line(newing, (0, lasth), (640, lasth),
             (0, 255, 0), thickness=2)
    lasth += threshold
    cv2.imshow('video', newing)
    if cv2.waitKey(33) == 27:
        break
    if lasth >= img.shape[1]:
        break

cv2.imwrite('image.png', newing)
cv2.destroyAllWindows()