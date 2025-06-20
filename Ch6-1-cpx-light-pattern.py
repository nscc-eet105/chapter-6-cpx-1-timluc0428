from adafruit_circuitplayground import cp
import time
import random

#use a list to contain the neopixel light pins numbers in a specific repeating
#pattern. The randint function is also used to create the actual light displayed.
MAX_PIXEL = 9
BLACK = (0, 0, 0)

#initialize empty lists for pixel range & pixel_pattern 
pixel_range = []
pixel_pattern = []

#makes list of pixels
for i in range(MAX_PIXEL + 1):
    pixel_range.append(int(i))

#makes random list of pixels with no repeats. random.shuffle is not included in circuit python
for i in range(MAX_PIXEL + 1):
    random_int = random.choice(pixel_range)
    pixel_pattern.append(random_int)
    pixel_range.remove(random_int)
print(pixel_pattern)

#a function that returns a tuple with the red, green and blue values randomly generated.
def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def pixel_black():
    for i in range(MAX_PIXEL + 1):
        cp.pixels[i] = BLACK

#inside the infinite while loop use a for loop to iterate through the pattern list
while True:
    for pixel in pixel_pattern:
        pixel_black()
        time.sleep(.05)
        cp.pixels[pixel] = pixel_color()
        time.sleep(.05)