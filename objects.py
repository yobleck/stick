# Classes
import math

class Bone():
    # bone coordinates are in the format ((x,y),(x,y)) or (Joint,(x,y))
    # TODO decorations
    def __init__(self, coor, thicc=None):
        #print("bone created")
        if type(coor[0]) is tuple:
            self.parent_joint = Joint(coor[0])
        elif type(coor[0]) is Joint:
            self.parent_joint = coor[0]
        self.child_joint = Joint(coor[1])
        self.length = math.dist(self.parent_joint.pos, self.child_joint.pos)
        #print(self.length)
        self.children = []  # Bones
        self.thicc = thicc or 1  # deal with pass by reference?

    def add_child(self, end_coor, thicc=None):
        # end_coor is coordinate of child bones child joint
        # child bones parent joint is parent bones child joint
        self.children.append( Bone( (self.child_joint, end_coor), thicc ) )
        
    def rotate(self, angle=None, anchor_joint=None, mouse_pos=None):  # mouse_pos is temporary
        if not anchor_joint:
            anchor_joint = self.parent_joint
        
        temp_child_joint_rel_origin = (self.child_joint.pos[0]-anchor_joint.pos[0], self.child_joint.pos[1]-anchor_joint.pos[1])
        
        if not angle and mouse_pos:
            #mouse_pos = ()  # TODO function to get mouse_pos from Xlib
            #angle = math.atan2((self.parent_joint.pos[1]-mouse_pos[1]), (self.parent_joint.pos[0]-mouse_pos[0]))
            # zero the two points rel to origin then do cosine rule
            temp_mouse_pos_rel_origin = (mouse_pos[0]-anchor_joint.pos[0], mouse_pos[1]-anchor_joint.pos[1])
            a = math.dist((0,0), temp_child_joint_rel_origin)
            b = math.dist((0,0), temp_mouse_pos_rel_origin)
            c = math.dist(temp_child_joint_rel_origin, temp_mouse_pos_rel_origin)
            angle = math.acos( (a**2+b**2-c**2)/(2*a*b) )
            #print(angle, math.atan2(temp_child_joint_rel_origin[1],temp_child_joint_rel_origin[0]),
                  #math.atan2(temp_mouse_pos_rel_origin[1],temp_mouse_pos_rel_origin[0]))
        
        #TODO rotation is wrong? need to take into account clockwise vs counter clockwise
        
        after_rotation = rot_cw(temp_child_joint_rel_origin, angle)
        self.child_joint.move_abs((after_rotation[0]+anchor_joint.pos[0], after_rotation[1]+anchor_joint.pos[1]))
        if self.children:
            for c in self.children:
                c.rotate(angle=angle, anchor_joint=anchor_joint)

    def _translate(self, delta):
        # Never call this directly on a Bone. only call through Head/parent Bone
        self.child_joint.move_rel(delta)
        if self.children:
            for c in self.children:
                c._translate(delta)


class Head(): #bone
    def __init__(self, coor, radius=None, thicc=None):
        self.pos = coor
        self.radius = radius or 5
        self.child_joint = Joint((self.pos[0],self.pos[1]+self.radius))
        self.thicc = thicc or 1  # TODO fill or border only option
        self.children = []

    def add_child(self, end_coor, thicc=None):
        self.children.append( Bone( (self.child_joint, end_coor), thicc ) )
        #return last index of children?

    def translate(self, delta):
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])
        self.child_joint.move_rel(delta)
        if self.children:
            for c in self.children:
                c._translate(delta)


class Joint():
    # coor is a 2-tuple (x,y)
    def __init__(self, coor):
        #print("joint created")
        self.pos = coor

    def move_rel(self, delta):
        # relative movement
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])
    
    def move_abs(self, new_coor):
        self.pos = new_coor


class Scene():
    def __init__(self, size, bg):
        self.size = size
        self.bg = bg
        self.entity_layers = []  # acts like photoshop layers

    def add_entity(self, e):
        self.entity_layers.append(e)


"""HELPER FUNCTIONS"""
#https://stackoverflow.com/questions/20104611/find-new-coordinates-of-a-point-after-rotation
#https://en.wikipedia.org/wiki/Rotation_matrix
#https://www.mathsisfun.com/algebra/trig-cosine-law.html
#https://stackoverflow.com/questions/1211212/how-to-calculate-an-angle-from-three-points
def rot_cw(pos, angle):
    return (pos[1]*math.sin(angle) + pos[0]*math.cos(angle),
            pos[1]*math.cos(angle) - pos[0]*math.sin(angle))

def rot_ccw(pos, angle):  # NOTE is this still needed
    return (pos[0]*math.cos(angle) - pos[1]*math.sin(angle),
            pos[0]*math.sin(angle) + pos[1]*math.cos(angle))
