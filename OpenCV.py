# pip install opencv-contrib-python main pkg and contrib pkg
# pip install opencv-python main package
# pip install caer # speed up workflow
"""
read img and videos
file path wrong error: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
https://github.com/jasmcaus/opencv-course/tree/master/Section%20%231%20-%20Basics
"""
import cv2 as cv
# img = cv.imread('Photos/flower.jpg')  # this method take in a path to an image and returns that image as a matrix of pixels
# cv.imshow('flower',img) #2 para: name of the new window, actual matrix of pixels to display, this img is greater than my screen
# cv.waitKey(0) #keyboard binding function but pop up too fast
# cv.destroyAllWindows() # add destroyAllWindows task to the queue and delay it.
# cv.waitKey(1)
 

"""
read videos
"""
# capture = cv.VideoCapture('Videos/boat.mp4') #int of you use webcam or camera that is connecting your cmputer, usually use 0 to connect just one camera or video path
# # use loop to read vidos frame by frame
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video',frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):  # if the letter D is pressed then break loop and stop playing this video
#         break
# capture.release()  # release capture device and dstroy all windows
# cv.destroyAllWindows()

"""
resizeing and rescaling the images to prevent computational strain
rescaling videos changes width and heights
"""

def resclareFrame(frame, scale=0.2):
    # images, videos and live videos, existing files or vieos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)



# capture = cv.VideoCapture('Videos/boat.mp4') #int of you use webcam or camera that is connecting your cmputer, usually use 0 to connect just one camera or video path
# # use loop to read vidos frame by frame
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = resclareFrame(frame)
#     cv.imshow('video',frame)
#     cv.imshow('Video Resized',frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):  # if the letter D is pressed then break loop and stop playing this video
#         break
# capture.release()  # release capture device and dstroy all windows
# cv.destroyAllWindows()

# def changeRes(width,height):  # you can also change brightness
#     # live videos, camera videos
#     capture.set(3,width)
#     capture.set(4,height)


# img = cv.imread('Photos/cat1.jpg')  # this method take in a path to an image and returns that image as a matrix of pixels
# resized_image = resclareFrame(img)
# cv.imshow('cat1',resized_image) #2 para: name of the new window, actual matrix of pixels to display, this img is greater than my screen
# cv.waitKey(0) #keyboard binding function but pop up too fast
# cv.destroyAllWindows() # add destroyAllWindows task to the queue and delay it.
# cv.waitKey(1)

"""
drawing shapes & putting text
"""
import numpy as np
# create dummy image or blank image
blank = np.zeros((500,500,3),dtype='uint8')  # height, width, color channels
cv.imshow('blank',blank)
# 1.paint the image a certain color
# blank[:] = 0,255,0  #0,0,255 red
# blank[200:300,300:400] = 0,0,255 
# cv.imshow('Green',blank)
# 2.draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED) #OR -1

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)
cv.waitKey(0)
# 3. draw a rectangle 
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255), thickness = 3)
cv.imshow('Circle',blank)
cv.waitKey(0)
# img = cv.imread('Photos/cat_small.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)
