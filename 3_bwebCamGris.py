from cv2 import *

namedWindow("laWebCam")
laWebCam = VideoCapture(0);

while True:
    next, frame = laWebCam.read()

    gray = cvtColor(frame, COLOR_BGR2GRAY)
    gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)
    can = Canny(gauss, 0, 30, 3)

    imshow("laWebCam", can)
    if waitKey(50) >= 0:
        break;
