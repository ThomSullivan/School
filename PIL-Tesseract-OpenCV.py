import io
import zipfile
from PIL import ImageDraw
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
from IPython.display import display



#make file handle to target zip file
ziphandle = zipfile.ZipFile("readonly/images.zip", mode='r')
# load CV XML classifiers readonly/haarcascade_frontalface_default.xml
                        # readonly/haarcascade_eye.xml
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
#make a list of pictures names
picture_names = ziphandle.namelist()

#for each picture name
for picture in picture_names:
    #open picture to memory
    get_img = ziphandle.read(picture)
    fh = io.BytesIO(get_img)
    #create PIL copy
    img = Image.open(fh)
    #display(picture)
    num_array = np.asarray(img)
    gray_num_array = cv.cvtColor(num_array, cv.COLOR_BGR2GRAY)
    #make a string of all words #tesseact to make a string pytesseract.image_to_sting()
    pytes_string = pytesseract.image_to_string(img)
    #print(pytes_string[:500])
    #find in string 'Mark' or 'Chirs'  #look for word on page
    if pytes_string.find('Mark') or pytes_string.find('Chris'):
        print('Results found in file '+str(picture))
        #if string found detect faces
        #make a list of rectangles
        faces = face_cascade.detectMultiScale(gray_num_array,1.3) #<- returns list of rectangles [x,y,w,h]
        if len(faces) == 0:
            print('But there were no faces in that file!')
            continue
        just_faces = []
        for x,y,w,h in faces:
            #crop  rectangle(s) from image add to list? PIL (x,y,x+w,y+h)
            just_faces.append(img.crop((x,y,x+w,y+h)))

        # create contact sheet of faces
        first_image=just_faces[0]
        contact_sheet=Image.new(first_image.mode, (500,200))
        x=0
        y=0
        for face in just_faces:
            face.thumbnail((100,100))
            contact_sheet.paste(face,(x,y))
            if x+100 == contact_sheet.width:
                x=0
                y=y+100
            else:
                x=x+100
        # thumbnail / resize contact sheet
        #contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
        display(contact_sheet)
