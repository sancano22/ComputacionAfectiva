from deepface import DeepFace

DeepFace.stream(db_path = "dataset")

#models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]

#backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']

#face detection and alignment
#detected_face = DeepFace.detectFace("img.png", detector_backend = backends[4])

#face verification
#obj = DeepFace.verify("dataset/img1.jpg", "dataset/img2.jpg", detector_backend = backends[4])

#face recognition
#df = DeepFace.find(img_path = "img.png", db_path = "dataset", detector_backend = backends[4])

#facial analysis
#demography = DeepFace.analyze("dataset/img4.jpg", detector_backend = backends[4])

print (demography)