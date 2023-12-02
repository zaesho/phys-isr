from math import *
import matplotlib as plt
import numpy as np
import manim as manim


def main():
    #Defining a function which takes numerical input measurement of inert reference frame and returns the scaling factor L'

    a = float(input("What is the inertial measurement?\n"))
    def scalingfactor(a):
        
        c = 3*(10**8)
        scale = sqrt((1-((a**2)/(c**2))))
        print("The relativistic scaling factor is: ",scale)
        return(scale)

        
    #scalingfactor() returns a scaling factor whose inverse is multiplied by the original value (a) to return the A' or relativistic value.

    prime = a/scalingfactor(a)
    print("\n The adjusted (relativistic) value is ",prime)


if __name__ == "__main__":
    main()
