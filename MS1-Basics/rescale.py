import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

url = '../Resources/Photos/cat_large.jpg'

img = cv.imread(url)

img = rescaleFrame(img)

cv.imshow("Large Cat", img)

cv.waitKey(0)

url = '../Resources/Videos/dog.mp4'

capture = cv.VideoCapture(url)

while True:
    isTrue, frame = capture.read()
    
    frame_recaled = rescaleFrame(frame)

    cv.imshow("Video", frame_recaled)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()