from deepface import Deepface

obj = DeepFace.analyze (img_path = "/home/tania/Documentos/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/rostro.jpeg", actions =['age','gender','rece','emotion'])
print ("El resultado del analisis es: ")
print(obj)