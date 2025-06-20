# from adafruit_circuitplayground import cp
import time
import random

[]#use a list to contain the neopixel light pins numbers in a specific repeating
#pattern. The randint function is also used to create the actual light displayed.
MAX_PIXEL = 9
BLACK = (0, 0, 0)
pixel_range = []

#makes list of pixels
for i in range(MAX_PIXEL + 1):
    pixel_range.append(int(i))

#makes random list of pixels
pixel_pattern = random.sample(pixel_range, k=10)

#a function that returns a tuple with the red, green and blue values randomly generated.
#example
def pixel_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green, blue)

def pixel_black():
    for i in range(MAX_PIXEL + 1)
        cp.pixels[i] = BLACK

#inside the infinite while loop use a for loop to iterate through the pattern list
#while True:
for pixel in pixel_pattern:
#        pixel_black()
#        time.sleep(.05)
#        cp.pixels[pixel] = pixel_color()
#        time.sleep(.05)
    pix_color = pixel_color()
    print(pixel, pix_color)
#Inside the for loop the specific pixel should be turned on using the randomly
    #generated color.
    #Make sure this is a flash action, so it should then be turned off by setting 
    #the pixel to black as in previous labs


