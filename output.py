#import PIL
from PIL import Image, ImageDraw
#Image.new("RGBA",(10,10))
import ffmpeg
import subprocess
import pickle


def draw_frame(scene, frame):
    with open("/tmp/" + str(frame) + ".pkl", "wb") as f:
        pickle.dump(scene, f, pickle.HIGHEST_PROTOCOL)  # NOTE pickle is insecure. hashing to check integrity?
    # set canvas size to scene.size
    # set background to scene.bg color or image
    # place all scene.entities and children and decorations
    # draw bones as lines based on their joints
    im = Image.new("RGBA", scene.size, color=scene.bg)

    if scene.entity_layers:
        for e in scene.entity_layers:
            im_draw = ImageDraw.Draw(im)
            im_draw.ellipse(  # entities are assumed to be Heads
                            [(e.pos[0]-e.radius, e.pos[1]-e.radius), (e.pos[0]+e.radius, e.pos[1]+e.radius)],
                            fill="black", width=e.thicc
                            )
            if e.children:
                for c in e.children:
                    draw_bones(c, im_draw)

    im.save("/tmp/" + str(frame) + ".png")
    subprocess.Popen(["gwenview", "/tmp/" + str(frame) + ".png"], stderr=subprocess.DEVNULL)

def draw_bones(bone, im_d):
    im_d.line([bone.parent_joint.pos, bone.child_joint.pos], fill="black", width=bone.thicc)  # draw bone
    im_d.ellipse(
        [(bone.child_joint.pos[0]-bone.thicc/2, bone.child_joint.pos[1]-bone.thicc/2),
         (bone.child_joint.pos[0]+bone.thicc/2, bone.child_joint.pos[1]+bone.thicc/2)],
        fill="red", width=bone.thicc
        )  # draw joints
    if bone.children:
        for c in bone.children:
            draw_bones(c, im_d)  # recurse


def render_video():
    pass
