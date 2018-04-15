from Tkinter import *
from math import *
from helper_function import *

WIDTH = 120
HEIGHT = 60
PRIMITIVE = "CUBE" #	Chooose between CUBE and PYRIMID
SCALE = 1 # Scale the primitive

########################## Below is the helper functions, nothing needs to be changed ##########################

camera_pos = [ 0,0,-5 ]
intensity = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
intensity = list(reversed(intensity))
canvas = " " * WIDTH * HEIGHT

cube_vert = [
	( -1, -1, -1 ), (  1, -1, -1 ), (  1,  1, -1 ), ( -1, 1, -1 ),
	( -1, -1,  1 ), (  1, -1,  1 ), (  1,  1,  1 ), ( -1, 1,  1 )
]

cube_edge = [
	( 0, 1 ), ( 1, 2 ), ( 2, 3 ), ( 3, 0 ),
	( 4, 5 ), ( 5, 6 ), ( 6, 7 ), ( 7, 4 ),
	( 0, 4 ), ( 1, 5 ), ( 2, 6 ), ( 3, 7 )
]

pyrimid_vert = [
	(0,1,0), (1,0,0), (-1,0,0), (0,0,-1), (0,0,1)
]

pyrimid_edge = [
	(0,1), (0,2), (0,3), (0,4), (1,3), (3,2), (2,4), (4,1)
]

def setPixel(x,y,p) :
	global canvas
	if x < 0 or x > WIDTH-1 or y < 0 or y > HEIGHT - 1 :
		return 
	canvas[y*WIDTH+x] = getCharByIntensity(p)

def plotLineLow(x0,y0,x1,y1,p):
	dx = x1 - x0
	dy = y1 - y0
	yi = 1
	if dy < 0 :
		yi = -1
		dy = -dy

	D = 2*dy - dx
	y = y0

	for x in range(x0,x1+1) :
		setPixel(x,y,p)
		if D > 0 :
			y = y + yi
			D = D - 2*dx
		D = D + 2*dy

def plotLineHigh(x0,y0,x1,y1,p):
	dx = x1 - x0
	dy = y1 - y0
	xi = 1
	if dx < 0 :
		xi = -1
		dx = -dx
	D = 2*dx - dy
	x = x0
	for y in range(y0, y1+1):
		setPixel(x,y,p)
		if D > 0 :
			x = x + xi
			D = D - 2*dy
		D = D + 2*dx

def plotLine(x0,y0,x1,y1,p) :
	if abs(y1 - y0) < abs(x1 - x0) :
		if x0 > x1 :
			plotLineLow(x1, y1, x0, y0, p)
		else :
			plotLineLow(x0, y0, x1, y1, p)
	else :
		if y0 > y1 :
			plotLineHigh(x1, y1, x0, y0, p)
		else :
			plotLineHigh(x0, y0, x1, y1, p)

def round2Int(f) :
	return int(round(f))

def getCharByIntensity(i) :
	return intensity[ round2Int(float(i)/255 * ( len(intensity) - 1 )) ]

def vertexProcessing(vert) :
	x,y,z = vert[0], vert[1], vert[2]
	x,y,z = camera_pos[0] + x, camera_pos[1] + y, camera_pos[2] + z
	f = WIDTH//2/z # amplify 
	x, y = x * f + WIDTH//2, y * f + HEIGHT//2
	return x, y

def renderCUBE() :
	for v0, v1 in cube_edge :
		_v0 = rotateAboutYAxis(cube_vert[v0][:], time*0.05)
		_v1 = rotateAboutYAxis(cube_vert[v1][:], time*0.05)
		_v0 = rotateAboutXAxis(_v0, time*0.05)
		_v1 = rotateAboutXAxis(_v1, time*0.05)
		_v0 = scale(_v0, SCALE)
		_v1 = scale(_v1, SCALE)
		_v0_x, _v0_y = vertexProcessing(_v0)
		_v1_x, _v1_y = vertexProcessing(_v1)
		plotLine(round2Int(_v0_x),round2Int(_v0_y),round2Int(_v1_x),round2Int(_v1_y),255) 

def renderPYRIMID() :
	for v0, v1 in pyrimid_edge :
		_v0 = rotateAboutYAxis(pyrimid_vert[v0][:], time*0.05)
		_v1 = rotateAboutYAxis(pyrimid_vert[v1][:], time*0.05)
		_v0 = rotateAboutXAxis(_v0, time*0.05)
		_v1 = rotateAboutXAxis(_v1, time*0.05)
		_v0 = scale(_v0, SCALE)
		_v1 = scale(_v1, SCALE)
		_v0_x, _v0_y = vertexProcessing(_v0)
		_v1_x, _v1_y = vertexProcessing(_v1)
		plotLine(round2Int(_v0_x),round2Int(_v0_y),round2Int(_v1_x),round2Int(_v1_y),255) 

PRIMITIVES = {
	"CUBE" : renderCUBE,
	"PYRIMID" : renderPYRIMID
}

def render() :
	PRIMITIVES[PRIMITIVE]()

########################## Below is the GUI settings, nothing needs to be changed ##########################

root = Tk()
T = Text(root, height=HEIGHT, width=WIDTH, bd=0, highlightthickness=0)
T.pack()

time = 0

def clearCanvas() :
	global canvas
	canvas = " " * WIDTH * HEIGHT

def unpackCanvas() :
	global canvas
	canvas = list(canvas)

def packCanvas() :
	global canvas
	canvas = "".join(canvas)

def update() :
	global count, canvas, time
	T.delete("1.0", "end")
	clearCanvas()
	unpackCanvas()
	render()
	packCanvas()
	time += 1
	T.insert(END, canvas)
	T.after(10, update)

def close(event):
	global root
	root.withdraw()
	sys.exit()

root.bind('<Escape>', close)

update()

root.mainloop()

