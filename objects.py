# Classes
import math

class Bone():
    # bone coordinates are in the format ((x,y),(x,y)) or (Joint,(x,y))
    # TODO decorations
    def __init__(self, coor, thicc=None):
        print("bone created")
        if type(coor[0]) is tuple:
            self.parent_joint = Joint(coor[0])
        elif type(coor[0]) is Joint:
            self.parent_joint = coor[0]
        self.child_joint = Joint(coor[1])
        self.length = math.dist(self.parent_joint.pos, self.child_joint.pos)
        print(self.length)
        self.children = []  # Bones
        self.thicc = thicc or 1  # deal with pass by reference?

    def add_child(self, end_coor, thicc=None):
        # end_coor is coordinate of child bones child joint
        # child bones parent joint is parent bones child joint
        self.children.append( Bone( (self.child_joint, end_coor), thicc ) )
        
    def rotate(self, angle=None, anchor_joint=None, mouse_pos=None):  # mouse_pos is temporary
        if not angle and mouse_pos:
            #mouse_pos = ()  # function to get mouse_pos from xlib
            angle = math.atan2((self.parent_joint.pos[1]-mouse_pos[1]), (self.parent_joint.pos[0]-mouse_pos[0]))
            print(angle)
            #rot_cw = True
        if not anchor_joint:
            anchor_joint = self.parent_joint
        #TODO rotation is wrong. need to take into account clockwise vs counter clockwise
        temp_child_joint_rel_origin = (self.child_joint.pos[0]-anchor_joint.pos[0], self.child_joint.pos[1]-anchor_joint.pos[1])
        after_rotation = rot_cw(temp_child_joint_rel_origin, angle)
        self.child_joint.move_abs((after_rotation[0]+anchor_joint.pos[0], after_rotation[1]+anchor_joint.pos[1]))
        if self.children:
            for c in self.children:
                c.rotate(angle=angle, anchor_joint=anchor_joint)

    """TODO DELETE THIS LATER
    def mouse_rotate(self, mouse_pos):
        #scratch all the below.
        #get the angle the same way
        #then just calculate shifting all the points to the origin then use the equations in the stackoverflow post
        #then undo the origin shifting
        #(think of all the child points as a rotating squareish spiral
        
        #https://stackoverflow.com/questions/20104611/find-new-coordinates-of-a-point-after-rotation
        #https://www.khanacademy.org/math/geometry/hs-geo-transformations/hs-geo-rotations/a/rotating-shapes
        #pass
        slope = (self.parent_joint.pos[1]-mouse_pos[1])/(self.parent_joint.pos[0]-mouse_pos[0])
        angle = math.atan2((self.parent_joint.pos[1]-mouse_pos[1]), (self.parent_joint.pos[0]-mouse_pos[0]))
        new_x = self.length * math.cos(angle)
        new_y = self.length * math.sin(angle)
        new_x2 = -self.child_joint.pos[1]*math.sin(angle) + self.child_joint.pos[0]*math.cos(angle)
        new_y2 = self.child_joint.pos[1]*math.cos(angle) - self.child_joint.pos[0]*math.sin(angle)
        print("out:", mouse_pos, slope, angle, new_x, new_y, new_x2, new_y2)
        #old_child_pos = self.child_joint.pos
        #self.child_joint.pos = (self.parent_joint.pos[0]-new_x, self.parent_joint.pos[1]-new_y)
        self.child_joint.move_abs( (self.parent_joint.pos[0]-new_x, self.parent_joint.pos[1]-new_y) )
        if self.children:
            for c in self.children:
                pass
                #c._rotate(angle, self.parent_joint.pos)
                #c._translate((new_x, new_y))
    
    def _rotate(self, angle, og_bone_origin):
        dist_from_origin = math.sqrt( (self.child_joint.pos[0]-og_bone_origin[0])**2 + (self.child_joint.pos[1]-og_bone_origin[1])**2 )
        new_x = dist_from_origin * math.cos(angle)
        new_y = dist_from_origin * math.sin(angle)
        self.child_joint.move_abs( (self.parent_joint.pos[0]-new_x, self.parent_joint.pos[1]-new_y) )
        """

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
        self.thicc = thicc or 1
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
        print("joint created")
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
        self.entities = []  # acts like photoshop layers

    def add_entity(self, e):
        self.entities.append(e)


"""HELPER FUNCTIONS"""
#https://stackoverflow.com/questions/20104611/find-new-coordinates-of-a-point-after-rotation
#https://en.wikipedia.org/wiki/Rotation_matrix
def rot_cw(pos, angle):
    return (pos[1]*math.sin(angle) + pos[0]*math.cos(angle),
            pos[1]*math.cos(angle) - pos[0]*math.sin(angle))

def rot_ccw(pos, angle):
    return (pos[0]*math.cos(angle) - pos[1]*math.sin(angle),
            pos[0]*math.sin(angle) + pos[1]*math.cos(angle))
