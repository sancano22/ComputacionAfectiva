from PIL import Image
import face_recognition

image = face_recognition.load_image_file("personas.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # detección facial coordenadas de donde se encuentra el rostro.
    face_image = image[top:bottom, left:right]

    pil_image = Image.fromarray(face_image)
    pil_image.show()

#encoding_1 = face_recognition.face_encodings (image)[0] 
#encoding_2 = face_recognition.face_encodings (image)[0]

#resultados = face_recognition.compare_faces([encoding_1], encoding_2, tolerancia = 0.50)
    
   
print(encoding_1)