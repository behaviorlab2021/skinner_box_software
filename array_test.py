import random
import math

image_array = ["image1.png", "image2.png", "image3.png", "image4.png", "image5.png", "image6.png", "image7.png"]

# print(len(image_array))
randint = math.floor(random.random()*7)


print(f"A random integer: {randint}.")

print(random.randint(0,2))