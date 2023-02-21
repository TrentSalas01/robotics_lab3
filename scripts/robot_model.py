import numpy as np
import math
def dh_transformation(linkLength, linkTwist, jointAngle, linkOffset): #normA, weirdA, theta, d
    '''
    * receives the Denavit-Hartenberg parameters (according to the convention 
      explained in class)
    * returns a combined homogenous transformation according to this convention.    
    '''
    #combines parameters into homogenous transformation
    trans = np.array([[math.cos(jointAngle), -math.sin(jointAngle)*math.cos(linkTwist), math.sin(jointAngle)*math.sin(linkTwist), linkLength*math.cos(jointAngle)],
				              [math.sin(jointAngle), math.cos(jointAngle)*math.cos(linkTwist), -math.cos(jointAngle)*math.sin(linkTwist), linkLength*math.sin(jointAngle)],
					            [0.0, math.sin(linkTwist), math.cos(linkTwist), linkOffset],
					            [0.0, 0.0, 0.0, 1.0]])
    #returns the transformation
    return trans
    
def kinematic_chain(myArray):
    '''
    * receives a 2D list/array containing the DH 
      parameters of a robotic manipulator
    * returns a homogenous transformation for the 
      kinematic chain (combination of the transformations for all of the frames). 
    '''
    #gets first array
    arr1 = myArray[0]
    #gets second array
    arr2 = myArray[1]
    #multiplies arrays
    mult = np.dot(arr1, arr2)
    #returns result
    return mult

def get_pos(hTrans):
    '''
    * receives a homogeneous transformation as input
    * returns the x, y, z components of the position
    '''
    #retreives x coordinate
    x = hTrans[0][3]
    #retreives y coordinate
    y = hTrans[1][3]
    #retreives z coordinate
    z = hTrans[2][3]
    #returns the coordinates
    return "x:", x,"y:", y, "z:", z

def get_rot(hTrans):
    '''
    * receives a homogeneous transformation as input 
    * returns roll-pith-yaw angles
    '''
    #retreives the roll angle
    roll = math.atan(hTrans[2][1] / hTrans[2][2])
    #retreives the pitch angle
    pitch = math.atan((-hTrans[2][0]) / math.sqrt((hTrans[2][1])**2 + (hTrans[2][2])**2))
    #retreives the yaw angle
    yaw = math.atan(hTrans[1][0] / hTrans[0][0])
    #returns the  angles
    return "roll:", roll,"pitch:", pitch, "yaw:", yaw