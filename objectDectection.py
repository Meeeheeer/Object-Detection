import sys,cv2
import numpy as np


def main(template,ImageA):
	aImage = cv2.imread(ImageA)
	temp = cv2.imread(template, 0)
	aCopy = aImage.copy()
	aImage = cv2.cvtColor(aImage , cv2.COLOR_BGR2GRAY)
	th , tw = temp.shape[:2]

	match = cv2.matchTemplate(aImage,temp,cv2.TM_SQDIFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
	topcorner = min_loc
	bottomcorner = (topcorner[0] + tw, topcorner[1] + th)

	cv2.rectangle(aCopy,topcorner,bottomcorner,(0,0,255),2)

	cv2.imshow('template',aCopy)
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.imwrite('template.jpg',aCopy)
		cv2.destroyALLWindows()

if __name__ == '__main__':
	
	args = sys.argv[1:]
	print(args)
	main(args[0], args[1])
