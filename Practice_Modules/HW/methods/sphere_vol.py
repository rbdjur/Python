import math
#declare function that takes a parameter, r as an argument that represents the radius of a sphere.
def sphere_vol(r):
    #define the volume of a sphere
    v = ((4.0 / 3.0)*math.pi*r**3)
    return v
    # return {0:.2f}.format(v)
#Assign the return value of the function to a variable, vSphere
vSphere = sphere_vol(10)
#print the variable
print(vSphere)