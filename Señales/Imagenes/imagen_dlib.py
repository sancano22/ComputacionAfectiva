import cv2
import dlib

img=cv2.imread("cara.jpg",);
#cv2.imshow(winname="Face",mat=img)

#cambiar a escala de grises
grises=cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

rostros=detector(grises)

for rostro in rostros:
	x1=rostro.left() #puntos de izquierda
	y1=rostro.top()
	x2=rostro.right()
	y2=rostro.bottom()

	#identificar rasgos faciales
	
	marcadores=predictor(grises,rostro)
	x=marcadores.part(21).x
	y=marcadores.part(21).y


	#cv2.rectangle(img=img,pt1=(x1,y1),pt2=(x2,y2),color=(0,255,0),thickness=4)
	cv2.circle(img,(x,y),5,(0,255,0),-1)

cv2.imshow(winname="Face",mat=img)




cv2.waitKey(delay=0)
cv2.destroyAllWindows()