from PIL import Image, ImageDraw
import random

def random_color():
    return (round(255*random.random()),round(255*random.random()),round(255*random.random()))
    
  
def create_rectangles(width, height):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # draw.ellipse takes a 4-tuple (x0, y0, x1, y1) where (x0, y0) is the top-left bound of the box
    # and (x1, y1) is the lower-right bound of the box.
    
#     draw.ellipse((ball_x, ball_y, ball_x + ball_size, ball_y + ball_size), fill='red')
    x,y=0,0
    for i in range(10):
        draw.rectangle((x,y,x+40,y+40), fill=random_color())
        for i in range(10):
            draw.rectangle((x,y,x+40,y+40), fill=random_color())
            x+=40
        x=0
        y+=40
    return img
# print (random_color())
frames = []
x, y = 0, 0
for i in range(100):
    new_frame = create_rectangles(400, 400)
    frames.append(new_frame)

 
# Save into a GIF file that loops forever
# frames.save('random_rects.png', format='PNG')
frames[0].save('shifting_squares.gif', format='GIF', append_images=frames[1:], save_all=True, duration=150, loop=0)
print('done')
