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

        #Creating MObjects for the Stick Figures

        head = Circle()
        head.scale=0.5
        head.shift(UP)

        body = Line(
            start=(1*UP),
            end=(1*DOWN),
        )
        head.set_stroke(color=WHITE,opacity=1)
        body.shift(DOWN)

        rleg = Line(
            start=(1*LEFT),
            end=(1*DOWN+0.15*RIGHT),
        )
        rleg.shift(2*DOWN+1*RIGHT)
        lleg = Line(
            start=(1*RIGHT),
            end=(1*DOWN+0.15*LEFT),
        )
        lleg.shift(2*DOWN+1*LEFT)

        #Defining a Stick Figure VGroup
        person = VGroup()
        person.add(head,body,rleg,lleg)
        person.scale(0.5)
        person.set_stroke(color=BLUE,opacity=1)

        #Scaling Factor for the Photon Relative to the Train's
        cs = 0.3
        circle.scale(rs*cs)

        #Setting the Circle's Starting Coordinate to be the Bottom of the Train
        circle.shift(((rs-((1/2)*(cs*rs)))*DOWN))

        #Animation Playout for MObjects
        rectangle.scale(rs*1.05)

        #person.scale(0.25*rectangle.height)
        #person.shift(person.height*0.5*UP)
        self.play(Create(rectangle))
        self.play(Create(circle))
        #self.play(person.animate.shift(0.8*UP))
        #self.play(person.animate.shift(0.8*DOWN))

        
        
        #Runtime for Photon Movement
        rt = lightclockverticalduration(10)*(10**8)

        print(rt)




        #Text for Time Scale
        #tstext = MathTex("Time\,Scale=\\frac{10\\,ns}{1\\,s}")
        #tstext.scale(0.67)
        #tstext.shift(4*UL,2*DOWN,RIGHT)
        #self.play(Write(tstext),runtime=1)
        #UP AND DOWN LOOP
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*UP),run_time=rt, rate_func=rate_functions.linear)
        self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*DOWN),run_time=rt, rate_func=rate_functions.linear)

if __name__ == '__main__':
    scene = PhotonClock2()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)









