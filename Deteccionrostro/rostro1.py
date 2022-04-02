#comparando dos rostros
import face_recognition 
imagenConocida = face_recognition.load_image_file("albert-einstein.jpg") 
imagenDesconocida = face_recognition.load_image_file("cara.jpg") 
codificadoEinstein = face_recognition.face_encodings(imagenConocida)[0] 
codificadoNoConocido = face_recognition.face_encodings(imagenDesconocida)[0] 
resultado = face_recognition.compare_faces([codificadoEinstein], codificadoNoConocido)
print (format(resultado[0]))
