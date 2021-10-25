# Main exe
import objects
import x
import output

def run():
    s = objects.Scene((20,20), "white")
    
    #h = objects.Head( ((0,0),(1,1)) )
    b = objects.Bone( ((10,10),(10,11)) )
    b.add_child((9,11))
    b.add_child((11,11))
    
    s.add_entity(b)
    
    

if __name__ == "__main__":
    run()
print("clean exit")
