import math

shape = input ("Would you like to find the volume of a cube, sphere, cylinder, or pyramid(square base)? ")

if (shape == "cube"):
    side = int(input ("Enter the side: "))
    volume = side**3
    print ("The volume of the cube is:", volume)
if (shape == "sphere"):
    radius = int(input ("Enter the radius: "))
    volume = (radius**3)*(4/3)*math.pi
    print ("The volume of the sphere is", volume)
if (shape == "cylinder"):
    radius = int(input ("Enter the radius: "))
    height = int(input ("Enter the height: "))
    volume = (radius**2)*math.pi*height
    print ("The volume of the sphere is", volume)
if (shape == "pyramid"):
    side = int(input ("Enter the side of the base: "))
    height = int(input ("Enter the height: "))
    volume = (side**2)*math.pi*height*(1/3)
    print ("The volume of the pyramid is", volume)
    
    
