from PIL import Image, ImageDraw

img = Image.open("mapImages.png")
width , height = img.size


draw = ImageDraw.Draw(img)

centerx = width//2 
centery = height//2
square_color = (0, 255, 0)

# square_position = (centerx, centery, centerx + 20,centery+ 40)

# draw.rectangle(square_position, outline=square_color, width=5)

# img.save("sampleImageWithSquare.png")

# Define the start and end angles
start_angle = 280
end_angle = 360

# Define the fill and outline colors
fill_color = (255, 0, 0)  # Red fill
outline_color = (0, 0, 0)  # Black outline

shape = [(centerx, centery),(centerx+20,centery+20)]
draw.pieslice(shape, start =280, end = 360, fill=fill_color, outline=outline_color)
img.save("sampleImageWithSquare.png")
