# Classes

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
        self.children = []  # Bones
        self.thicc = thicc or 1  # deal with pass by reference?

    def add_child(self, end_coor):
        # end_coor is coordinate of child bones child joint
        # child bones parent joint is parent bones child joint
        self.children.append( Bone( (self.child_joint, end_coor) ) )

    def rotate(self, theta):
        pass
        #self.child_joint.move() # TODO some rotation to coordinates math
        if self.children:
            for c in self.children:
                c._translate()

    def _translate(self, delta):
        # Never call this directly on a Bone. only call through Head or parent Bone
        #self.parent_joint.move(delta)  # dont need this cause child joint of parent bone is parent joint of child bone?
        self.child_joint.move(delta)
        if self.children:
            for c in self.children:
                c._translate(delta)



class Head(): #bone
    def __init__(self, coor, radius=None, thicc=None):
        #super().__init__(coor)
        self.pos = coor
        self.radius = radius or 5
        self.child_joint = Joint((self.pos[0],self.pos[1]+self.radius))
        self.thicc = thicc or 1
        self.children = []

    def add_child(self, end_coor):
        self.children.append( Bone( (self.child_joint, end_coor) ) )
        #return last index of children?

    def translate(self, delta):
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])
        self.child_joint.move(delta)
        if self.children:
            for c in self.children:
                c._translate(delta)



class Joint():
    # coor is a 2-tuple (x,y)
    def __init__(self, coor):
        print("joint created")
        self.pos = coor

    def move(self, delta):
        # relative movement?
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])


class Scene():
    def __init__(self, size, bg):
        self.size = size
        self.bg = bg
        self.entities = []  # acts like photoshop layers

    def add_entity(self, e):
        self.entities.append(e)
