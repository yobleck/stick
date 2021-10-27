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
            im_draw.ellipse(
                            [(e.pos[0]-e.radius, e.pos[1]-e.radius), (e.pos[0]+e.radius, e.pos[1]+e.radius)],
                            fill="black", width=e.thicc
                            )
            if e.children:
                for c in e.children:
                    im_draw.line([c.parent_joint.pos, c.child_joint.pos], fill="black", width=c.thicc)
    im.save("/tmp/" + str(frame) + ".png")
    subprocess.Popen(["gwenview", "/tmp/" + str(frame) + ".png"])


def render_video():
    pass
