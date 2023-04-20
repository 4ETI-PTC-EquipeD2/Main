import numpy as np
from matplotlib import pyplot as plt

import cv2

I = cv2.imread("Pika.png",0)
print(len(I), len(I[0]))
#I = cv2.normalize(I,None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
plt.figure()
plt.subplot(211)
plt.imshow(I)
Qr = cv2.QRCodeDetector().detectAndDecode(I)
Qrla = cv2.QRCodeDetector().detect(I)
plt.subplot(212)
print('La valeur de Qr ,',Qr[0])
print('Le detect ,', Qrla)

