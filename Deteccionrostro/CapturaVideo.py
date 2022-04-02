from fer import FER
import cv2

process_this_frame = True
video_captura=cv2.VideoCapture(0)

detector = FER(mtcnn=True)
#raw_data = video_captura.analyze(detector, display=True)
#df = video_captura.to_pandas(raw_data)
#print (df)
while True:
    ret, frame = video_captura.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_captura.release()
cv2.destroyAllWindows
        

