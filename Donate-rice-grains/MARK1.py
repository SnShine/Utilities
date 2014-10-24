#Import required libraries. We need to download some, if you don't have tham.
import cv2
import os
import pyscreenshot as ImageGrab
import numpy as np
import time
from pymouse import PyMouse
import random
 
#defining a function rand.
def rand():
    m = PyMouse()
    #find a random int and put it into 'do'
    do= random.randint(1,4)
    #basic if, elif loop
    if do == 1:
    #clicking at point (395, 429). Here 1 implies a   left-click
    m.click(395, 429, 1)
    elif do== 2:
    m.click(395, 466, 1)
    elif do == 3:
    m.click(395, 505, 1)
    else:
    m.click(395, 544, 1)
    m.move(50,50)
    print("Rand")
    #wait for 1 sec, giving time to browser to refresh
    time.sleep(1)
 
trails= 0
#two forloops because, I am waiting for 5 secs after every 10 calculations just to make the system stable
for guns in range (0,1000):
  for buns in range(0,10):
  #Using try,catch to avoid any errors
    try:
      img= ImageGrab.grab() #taking a screenshot
      img.save('output.png')
      pic= cv2.imread('output.png')
      pic2= pic[360:570, 380:470] #cropping the pic, works in my case
      cv2.imwrite('output.png', pic2)
      u= 'convert output.png -resize 700 output.png'
      os.system(u) #writing to terminal (re-sizing the pic)
      s= 'tesseract output.png output'
      os.system(s) #writing to terminal (running Tesseract)
      f= open('output.txt', 'r')
      string= f.read().replace('\n', ' ')
      string= string.replace(' ', ' ')
      string= string.replace(' ', ' ')
      first= string[:string.find('x')] #finding first integer
      second= string[string.find('x')+1:string.find(' ')] #finding second integer
      pro= int(first)*int(second)
      print(pro)
      print(string)
      m= PyMouse()
      string= string[string.find(' ')+1:]
      a= int(string[:string.find(' ')])
      #print(a)
      #checking if product is equal to any of answers and clicking on that particular option
      if pro == a:
        m.click(395, 429, 1)
        m.move(50,50) #move cursor to any random point which is not in our area of interest, avoiding tesseract to think it as some character
        print("Pass")
        time.sleep(1)
      else:
        string= string[string.find(' ')+1:]
        b= int(string[:string.find(' ')])
        #print(b)
        if pro == b:
          m.click(395, 466, 1)
          m.move(50,50)
          print("Pass")
          time.sleep(1)
        else:
          string= string[string.find(' ')+1:]
          c= int(string[:string.find(' ')])
          #print(c)
          if pro == c:
            m.click(395, 505, 1)
            m.move(50,50)
            print("Pass")
            time.sleep(1)
          else:
            d= int(string[string.find(' ')+1:])
            #print(d)
            if pro == d:
              m.click(395, 544, 1)
              m.move(50,50)
              print("Pass")
              time.sleep(1)
            else:
              rand() #tesseract can't detect 100% accurately. So, tick any option randomly in case it didn't find correct answer
              #print("haha")
    except (ValueError, NameError, TypeError):
      rand() #tick randomly in case of any errors
  trails+= 10
  print("Total= " + str(trails))
  time.sleep(5) #waiting for 5secs after every 10 loops to make my system stable.
