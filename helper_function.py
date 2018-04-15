from math import *

intensity = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
intensity = list(reversed(intensity))

def rotateAboutZAxis(pos, rad) :
	s, c = cos(rad), sin(rad)
	return pos[0]*c-pos[1]*s, pos[1]*c+pos[0]*s, pos[2]

def rotateAboutYAxis(pos, rad) :
	s, c = cos(rad), sin(rad)
	return pos[0]*c-pos[2]*s, pos[1], pos[2]*c+pos[0]*s

def rotateAboutXAxis(pos, rad) :
	s, c = cos(rad), sin(rad)
	return pos[0], pos[1]*c-pos[2]*s, pos[2]*c+pos[1]*s

def translate(pos, move) :
	return pos[0] + move[0], pos[1] + move[1], pos[2] + move[2]

def scale(pos, f) :
	return pos[0] * f, pos[1] * f, pos[2] * f

def round2Int(f) :
	if not f :
		return None
	return int(round(f))

def getCharByIntensity(i) :
	return intensity[ round2Int(float(i)/255 * ( len(intensity) - 1 )) ]

def mapInt(f, r0, r1, c0, c1) :
	if r0 == r1 :
		return int(c0)
	return int( float( f - r0 ) / ( r1 - r0 ) * ( c1 - c0 ) + c0 )

def mapFloat(f, r0, r1, c0, c1) :
	if r0 == r1 :
		return c0	
	return float( f - r0 ) / ( r1 - r0 ) * ( c1 - c0 ) + c0 


