import numpy as np
import math
def dh_transformation(linkLength, linkTwist, jointAngle, linkOffset):
    '''
    * receives the Denavit-Hartenberg parameters (according to the convention 
      explained in class)
    * returns a combined homogenous transformation according to this convention.    
    '''
    trans = np.array([[math.cos(jointAngle), -math.sin(jointAngle)*math.cos(linkTwist), math.sin(jointAngle)*math.sin(linkTwist), linkLength*math.cos(jointAngle)],
				              [math.sin(jointAngle), math.cos(jointAngle)*math.cos(linkTwist), -math.cos(jointAngle)*math.sin(linkTwist), linkLength*math.sin(jointAngle)],
					            [0.0, math.sin(linkTwist), math.cos(linkTwist), linkOffset],
					            [0.0, 0.0, 0.0, 1.0]])
    return trans
    
def kinematic_chain(myArray):
    '''
    * receives a 2D list/array containing the DH 
      parameters of a robotic manipulator
    * returns a homogenous transformation for the 
      kinematic chain (combination of the transformations for all of the frames). 
    '''
    np.identity(4)
    

def get_pos(hTrans):
    '''
    * receives a homogeneous transformation as input
    * returns the x, y, z components of the position
    '''
    x = hTrans[0][3]
    y = hTrans[1][3]
    z = hTrans[2][3]
    return "x:", x,"\ny:", y, "\nz:", z

def get_rot(hTrans):
    '''
    * receives a homogeneous transformation as input 
    * returns roll-pith-yaw angles
    '''
    roll = np.arctan(hTrans[2][1] / hTrans[2][2])
    pitch = np.arctan((-hTrans[2][0]) / math.sqrt((hTrans[2][1])^2 + (hTrans[2][2])^2))
    yaw = np.arctan(hTrans[1][0] / hTrans[0][0])

    return "roll:", roll,"\npitch:", pitch, "\nyaw:", yaw