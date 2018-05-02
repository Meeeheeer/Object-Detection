import cv2
import numpy as np

def main(template,aImage)	
	img = cv2.imread(aImage)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	template = cv2.imread(template,0)
	w, h = template.shape[::-1]
	
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.7
	loc = np.where( res >= threshold)
	
	for pt in zip(*loc[::-1]):
	    cv2.rectangle(img, pt, (pt[0] + w-50, pt[1] + h-50), (0,255,255), 2)
	
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	
	args = sys.argv[1:]
	print(args)
	main(args[0], args[1])