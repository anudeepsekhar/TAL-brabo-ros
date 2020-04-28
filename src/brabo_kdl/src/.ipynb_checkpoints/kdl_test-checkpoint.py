import roslib
import rospy
from pykdl_utils.kdl_parser import kdl_tree_from_urdf_model
from urdf_parser_py.urdf import URDF

robot = URDF.from_parameter_server()
##print(robot)
tree = kdl_tree_from_urdf_model(robot)
print tree.getNrOfSegments()
base_link = 'base_link'
end_link = 'link_5'
chain = tree.getChain(base_link, end_link)
print chain.getNrOfJoints()
