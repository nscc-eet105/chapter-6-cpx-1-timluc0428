from adafruit_circuitplayground import cp
import time

[]#use a list to contain the neopixel light pins numbers in a specific repeating
#pattern. The randint function is also used to create the actual light displayed.
MAX_PiXEL = 9

pixel_range = []


for i in range(MAX_PiXEL + 1):
    pixel_range.append(int(i))

print(pixel_range)


#a list of the pins which use it pixel at least once.

#a function that returns a tuple with the red, green and blue values randomly generated.
#example
def pixel_color():
    red = random.randint(0,255)

#inside the infinite while loop use a for loop to iterate through the pattern list
while True:
    for pixel in pattern:
        cp.pixels[pixel] = pixel_color()

#Inside the for loop the specific pixel should be turned on using the randomly
    #generated color.
    #Make sure this is a flash action, so it should then be turned off by setting 
    #the pixel to black as in previous labs

