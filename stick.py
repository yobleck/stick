# Main exe
import objects
import x
import output

def run():
    s = objects.Scene((20,20), "white")
    
    h = objects.Head((10,10), radius=3)
    h.add_child((10,18))
    s.add_entity(h)
    output.draw_frame(s, 0)
    h.translate((0,-5))
    output.draw_frame(s, 1)
    
    """
    b = objects.Bone( ((10,10),(10,11)) )
    b.add_child((9,11))
    #.add_child((11,11))
    s.add_entity(b)

    output.draw_frame(s, 0)
    b._translate((0,5))
    output.draw_frame(s, 1)
    """
    

if __name__ == "__main__":
    run()
print("clean exit")
