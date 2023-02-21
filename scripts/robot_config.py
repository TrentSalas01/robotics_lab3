import robot_model
import math


#a (two-link planar manipulator)
output = robot_model.kinematic_chain([robot_model.dh_transformation(1,0,0, math.pi/2), robot_model.dh_transformation(1,0,0, math.pi/2)])
print("========================")
print(robot_model.get_pos(output))
print(robot_model.get_rot(output)) #normA, weirdA, theta, d
############################################################################################################################################################


#b (6 DoF UR5e (Case 1))
#1 n 2
output = robot_model.kinematic_chain([robot_model.dh_transformation(0, math.pi/2, 0, 0.1625), robot_model.dh_transformation(-0.425, 0, 0, 0)])
# 3
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(-0.3922, 0, 0, 0)])
# 4
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(0, math.pi/2, 0, 0.1333)])
# 5
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(0, -math.pi/2, 0, 0.0997)])
# 6
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(0, 0, 0, 0.0996)])
print("========================")
print(robot_model.get_pos(output))
print(robot_model.get_rot(output))
############################################################################################################################################################


#b (6 DoF UR5e (Case 2))
#1 n 2
output = robot_model.kinematic_chain([robot_model.dh_transformation(0, math.pi/2, 0, 0.1625), robot_model.dh_transformation(-0.425, 0, -math.pi/2, 0)])
# 3
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(-0.3922, 0, 0, 0)])
# 4
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(0, math.pi/2, 0, 0.1333)])
# 5
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(0, -math.pi/2, 0, 0.0997)])
# 6
output = robot_model.kinematic_chain([output, robot_model.dh_transformation(0, 0, 0, 0.0996)])
print("========================")
print(robot_model.get_pos(output))
print(robot_model.get_rot(output))