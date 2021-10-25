# Classes

class Bone():
    # bone coordinates are in the format ((x,y),(x,y))
    # TODO bone thickness
    def __init__(self, coor):
        self.parent_joint = Joint(coor[0])
        self.child_joint = Joint(coor[1])
        self.children = []  # Bones
    
    def add_child(self, end_coor):
        # end_coor is coordinate of child bones child joint
        # child bones parent joint is parent bones child joint
        self.children.append( Bone( (self.child_joint.pos, end_coor) ) )
    
    def rotate(self, theta):
        pass
        #self.child_joint.move() # TODO some rotation to coordinates math
    
    def translate(self, delta):
        self.parent_joint.move(delta)  # dont need this cause child joint of parent bone is parent joint of child bone?
        self.child_joint.move(delta)
        if children:
            for c in children:
                c.translate(delta)



class Head(Bone):
    def __init__(self, coor):
        super().__init__(coor)



class Joint():
    # coor is a 2-tuple (x,y)
    def __init__(self, coor):
        self.pos = coor
    
    def move(self, delta):
        # relative movement?
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])


class Scene():
    def __init__(self, size, bg):
        self.size = size
        self.bg = bg
        self.entities = []
    
    def add_entity(self, e):
        self.entities.append(e)
