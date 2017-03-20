{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "import imutils\n",
    "import time\n",
    "\n",
    "#loading the haar cascade\n",
    "cat_classifier = cv2.CascadeClassifier(\"Haarcascades\\haarcascade_frontalcatface.xml\")\n",
    "\n",
    "#Define a function to detect cats from the output video of your webcam\n",
    "def cat_detector(img):\n",
    "    #Convert image to grayscale\n",
    "    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) \n",
    "    cats = cat_classifier.detectMultiScale(gray, 1.3, 5)\n",
    "    \n",
    "    if cats is ():\n",
    "        return img\n",
    "    \n",
    "    for(x,y,w,h) in cats:\n",
    "        x = x - 50\n",
    "        w = w + 50\n",
    "        y = y - 50\n",
    "        h = h + 50\n",
    "        #Draw a rectangle around the region of interest\n",
    "        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)\n",
    "        #Cropping the region of interest\n",
    "        roi_color = img[y:y+h, x:x+w]\n",
    "    \n",
    "    image = cv2.flip(img,1)\n",
    "    return roi_color #Cropping out the region of interest and returning it\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "time.sleep(2)\n",
    "\n",
    "while True:\n",
    "    \n",
    "    ret, frame = cap.read()\n",
    "    cv2.imshow(\"Cat Detector\",cat_detector(frame))\n",
    "    if cv2.waitKey(1) == 13:\n",
    "        break\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
