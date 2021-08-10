#!mkdir -p /Documents/DATA      #you can create a folder for your frames using  this command in linux terminal
import cv2
cap= cv2.VideoCapture('video-link')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('folder-link/image'+str(i)+'.jpg',frame)     #para salvar no notebook use cv2.imwrite('DATAEMOTION/train/image'+str(i)+'.jpg',frame)
    i+=1        # frames qtd
 
cap.release()
cv2.destroyAllWindows()
