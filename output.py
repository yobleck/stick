#import PIL
from PIL import Image, ImageDraw
#Image.new("RGBA",(10,10))
import ffmpeg
import subprocess


def draw_frame(scene, frame):
    # set canvas size to scene.size
    # set background to scene.bg color or image
    # place all scene.entities and children and decorations
    # draw bones as lines based on their joints
    im = Image.new("RGBA", scene.size, color=scene.bg)

    if scene.entities:
        for e in scene.entities:
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
    im_d.line([bone.parent_joint.pos, bone.child_joint.pos], fill="black", width=bone.thicc)
    if bone.children:
        for c in bone.children:
            draw_bones(c, im_d)


def render_video():
    pass
