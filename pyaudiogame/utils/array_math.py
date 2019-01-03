# These are simple equasions dealing with arrays. It is to avoid using numpy. If this file becomes too complex though, numpy will be needed.
import math

def magnitude(v):
	return math.sqrt(v[0]**2 + v[1]**2)

def vector(p1, p2):
	return [p1[0] - p2[0], p1[1] - p2[1]]


def dotProduct(v1, v2):
	return ((v1[0] * v2[0]) + (v1[1] * v2[1]))

def sumArray(a1,a2):
	return [a1[i]+a2[i] for i in range(len(a1))]
