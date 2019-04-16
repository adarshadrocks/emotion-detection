#!/usr/bin/python3
import cv2
#from cv2 import *

def findmouth(img):

	# INITIALIZE: loading the classifiers
	haarFace  = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	haarMouth = cv2.CascadeClassifier('haarcascade_mouth.xml')
	# running the classifiers 
	'''
	storage = cv.CreateMemStorage()
	detectedFace = cv2.HaarDetectObjects(img, haarFace, storage)
	detectedMouth = cv2.HaarDetectObjects(img, haarMouth, storage)
	'''
	detectedFace  = haarFace.detectMultiScale(img, 1.3, 5)
	detectedMouth = haarMouth.detectMultiScale(img, 1.3, 5)

	# FACE: find the largest detected face as detected face
	maxFaceSize = 0
	maxFace = 0
	print ("0")
	print (len(detectedMouth))
	
	if (detectedFace).all(): 
		print ("1")
		
		for x,y,h,w in detectedFace: # face: [0][0]: x; [0][1]: y; [0][2]: width; [0][3]: height 
			if h*w > detectedFace.all():
				print (x)
				print (y)
				print (h)
				print (w)
				maxFaceSize = (w*h)
				maxFace= img[(x,y),(x+w,y+h)]
				print ("3")

		if maxFace.any() == 0: # did not detect face
			return 2

	def mouth_in_lower_face(mouth,face):
	# if the mouth is in the lower 2/5 of the face 
	# and the lower edge of mouth is above that of the face
	# and the horizontal center of the mouth is the center of the face
	#if (mouth[0][1] > face[0][1] + face[0][3] * 3 / float(5) and mouth[0][1] + mouth[0][3] < face[0][1] + face[0][3] and abs((mouth[0][0] + mouth[0][2] / float(2)) - (face[0][0] + face[0][2] / float(2))) < face[0][2] / float(10)): 	
		for x,y,w,h in mouth:
			print (x)
			print (mouth.y)
			print (mouth.w)
			print (mouth.h)

			if (mouth.y > face.y + face.height * 3 / 5 and  mouth.y + mouth.height < face.y + face.height and abs((mouth.x + mouth.width / 2)) - (face.x + face.width / 2) < face.width / 10):
					return True
			else:
				return False


	# FILTER MOUTH
	filteredMouth = []
	

	if (detectedMouth).any:
		if True:
			k=len(detectedMouth)
			for i in range(k):
				filteredMouth.append(detectedMouth[i])
			print (filteredMouth)
			print (filteredMouth[0])
			#print (len(filteredMouth))
	maxMouthSize = 0
	for i in range(len(filteredMouth)):
		for j in range(4):
		#for x,y,w,h in filteredMouth:
			if filteredMouth[i][2]*filteredMouth[i][3] > maxMouthSize:
	  			maxMouthSize = filteredMouth[i][2]*filteredMouth[i][3]
	  			print (maxMouthSize)
	  			#maxMouth=detectedMouth((x,y),((x+w),(y+h)))
		#maxMouth = detectedMouth[(filteredMouth[i][0],filteredMouth[i][1]),(filteredMouth[i][3]+filteredMouth[i][0],filteredMouth[i][1]+filteredMouth[i][2])]
	  	
	  
	try:
		#return maxMouth
		return filteredMouth
	except UnboundLocalError:
		return 2
    


    #maxMouth=detectedMouth[(x,y),(x+w),(y+h)]