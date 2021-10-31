# Main exe
import objects
import x
import output

def run():
    s = objects.Scene((200,200), "white")
    
    h = objects.Head((100,100), radius=30)
    h.add_child((100,180), thicc=5) #neck
    h.children[0].add_child((80,180), thicc=5) #forearm
    h.children[0].children[0].add_child((80,200), thicc=2) #lower arm
    h.children[0].children[0].children[0].add_child((50,200), thicc=3) #hand
    s.add_entity(h)
    #output.draw_frame(s, 0)
    h.translate((0,-50))
    output.draw_frame(s, 1)
    #h.children[0].children[0].mouse_rotate((80,140))
    h.children[0].children[0].rotate(mouse_pos=(80,140))
    output.draw_frame(s, 2)
    #h.children[0].children[0].mouse_rotate((130,190))
    h.children[0].children[0].rotate(mouse_pos=(130,190))
    output.draw_frame(s, 3)
    #h.children[0].children[0].mouse_rotate((130,100))
    h.children[0].children[0].rotate(mouse_pos=(130,100))
    output.draw_frame(s, 4)
    
    output.render_video()
    

if __name__ == "__main__":
    run()
print("clean exit")
