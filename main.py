import pandas as pd

url  = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=1900-01-01&endtime=2024-09-10&minmagnitude=8&orderby=magnitude"

df = pd.read_csv(url, sep="|")

print(df.head())


newdf = df[["Latitude", "Longitude", "Magnitude"]]

from PIL import Image, ImageDraw
img = Image.open("mapImages.png")
width , height = img.size


draw = ImageDraw.Draw(img)

centerx = width//2 
centery = height//2
square_color = (0, 255, 0)
start_angle = 280
end_angle = 360

# Define the fill and outline colors
fill_color = (255, 0, 0)  # Red fill
outline_color = (0, 0, 0)  # Black outline

all_rows = newdf.iterrows()

pixelToCoordinateDifference = (width / 360) 

for idx,row in all_rows:
  long = row["Longitude"]
  lat = row["Latitude"]
  mag = row["Magnitude"]

  x = centerx + (long *pixelToCoordinateDifference)
  y = centery - (lat* pixelToCoordinateDifference)
  shape = [(x-16,y-16),(x+16,y+16)]
  draw.pieslice(shape, start =280, end = 360, fill=fill_color, outline=outline_color) 

img.save("sampleImageWithSquare.png")