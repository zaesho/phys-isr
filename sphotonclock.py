from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class PhotonClock(Scene):
    def construct(self):

        #Train Base Construction
        rectangle = Rectangle()
        rs = 1
        rectangle.scale(rs)
        rectangle.set_fill(WHITE, opacity=0.0)
        #Photon Construction
        circle = Circle()
        circle.set_fill(YELLOW, opacity = 1.0)
        circle.set_stroke(YELLOW)

        #Scaling Factor for the Photon Relative to the Train's
        cs = 0.1
        circle.scale(rs*cs)

        #Setting the Circle's Starting Coordinate to be the Bottom of the Train
        circle.shift(((rs-((1/2)*(cs*rs)))*DOWN))

        #Animation Playout for MObjects
        rectangle.scale(rs*1.05)
        self.play(Create(rectangle))
        self.play(Create(circle))

        
        
        #Runtime for Photon Movement
        rt = lightclockverticalduration(10)*(10**8)

        print(rt)




        #Text for Time Scale
        tstext = Text("Time Scale = 100, 000, 000s per second")
        tstext.scale(0.67)
        tstext.shift(4*UL,DOWN,RIGHT)
        self.play(Write(tstext),runtime=1)
        #UP AND DOWN LOOP
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*UP),run_time=rt, rate_func=rate_functions.linear)
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*DOWN),run_time=rt, rate_func=rate_functions.linear)

if __name__ == '__main__':
    scene = PhotonClock()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)









