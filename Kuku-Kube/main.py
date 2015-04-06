from selenium import webdriver
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyperclip
import time, math

m= PyMouse()
k= PyKeyboard()

# m.move(335, 580)		#when start button is located below
# m.move(335, 400)		#when start button is above

# m.move(620, 360)		#to copy inspect element

# m.move(76, 400)		#left bordor
# m.move(580,400)		#right bordor
# m.move(400, 192)		#top bordor
# m.move(400, 698)		#bottom bordor

# m.click(335, 580)		#start game
# print("The game's ON!")
# time.sleep(0.1)

for i in range(370):
	
	m.click(620, 360)
	k.press_key(k.control_key)
	time.sleep(0.05)
	k.tap_key("c")
	time.sleep(0.05)
	k.release_key(k.control_key)
	#print("Copied Inspect Element.")

	x = pyperclip.paste()
	#print(x)
	#print(len(x))
	tiles= x.count("rgb")

	z= []
	for j in range(tiles):
		st= x.index("rgb")
		x= x[st+1:]
		#print(len(x))
		y= x[3:x.index(";")- 1]
		y= y.split(",")
		z.append(tuple(y))
		#print(y)

	#print(z)
	zset= set(z)
	zset= list(zset)
	if z.count(zset[0])== 1:
		press= z.index(zset[0])+ 1
	else:
		press= z.index(zset[1])+ 1

	#print("tiles: ", tiles, "press: ", press)

	side= int(math.sqrt(tiles))
	if press% side== 0:
		row= press/side
		colomn= side
	else:
		row= press/side + 1
		colomn= press%side

	print("row: "+ str(row)+ "; colomn: "+ str(colomn))

	temp= 698- 192
	temp = temp/ side
	ycursor= 192+ (row*temp)- (temp/2)
	temp= 580- 76
	temp = temp/ side
	xcursor= 76+ (colomn*temp)- (temp/2)

	m.click(xcursor, ycursor)
	time.sleep(0.05)
