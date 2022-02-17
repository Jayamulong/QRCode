import cv2
import datetime

Time = datetime.datetime.now()

cap=cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()
while True:
	_,img=cap.read()
	data,one,_=detector.detectAndDecode(img)
	if data:
		a=data
		break
	cv2.imshow("QRCode Scanner", img)
	if cv2.waitKey(1)==ord("q"):
		break

print(Time)
print(data)
cv2.destroyAllWindows()