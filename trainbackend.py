from math import *
import matplotlib as plt
import numpy as np



def lightclockverticalduration(trainheight):
    c = 3*(10**8)
    lightclockruntime = trainheight/c

    return lightclockruntime

def scalingfactor(v):
    c = 3*(10**8)
    sf = (1-((v/c)**2))**(1/2)

    return sf

