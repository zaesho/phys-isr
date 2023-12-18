from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class PhotonClock2(Scene):
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
        cs = 0.05
        circle.scale(rs*cs)

        #Setting the Circle's Starting Coordinate to be the Bottom of the Train
        circle.shift(((rs-((1/2)*(cs*rs)))*DOWN))

        #Defining Bob's Stopwatch Clock
        stopwatch = DecimalNumber(0)
        casing = Circle().surround(stopwatch,buffer_factor=1.5).set_stroke(color=RED,opacity=0.8)
        clock = VGroup(stopwatch,casing)
        clock.scale(0.6)
        clock.next_to(rectangle).shift(RIGHT)

         #Header
        header = Text("Photon Clock").scale(0.8).shift(3*UP)


        #Animation Playout for MObjects
        rectangle.scale(rs*1.05)
        self.play(Write(header))
        self.play(Create(rectangle))
        self.play(Create(circle))
        self.play(Create(clock))

    
        #Runtime for Photon Movement
        rt = lightclockverticalduration(10)*(10**8)

        print(rt)

        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*UP),run_time=rt, rate_func=rate_functions.linear)
        stopwatch.set_value(1)
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*DOWN),run_time=rt, rate_func=rate_functions.linear)
        stopwatch.set_value(2)
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*UP),run_time=rt, rate_func=rate_functions.linear)
        stopwatch.set_value(3)
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*DOWN),run_time=rt, rate_func=rate_functions.linear)
        self.play(stopwatch.animate.set_value(4),run_time=0.5)

if __name__ == '__main__':
    scene = PhotonClock2()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)









