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

        #Coordinate Plane (x-axis)
        grid = NumberLine(
            x_range=[0, 20, 5],
            length=2*rectangle.width,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,

        )
        grid.shift(2*DOWN)

        #Moving the Rectangle to the start of the Plane (shifted up a little)
        rectangle.match_x(grid)
        rectangle.match_y(grid)
        rectangle.shift((0.5*rectangle.height+0.2)*UP,
                        (0.49*grid.width*LEFT))
        rectangle.shift(0.15*UP)

        #Scaling Factor for the Photon Relative to the Train's
        cs = 0.1
        circle.scale(rs*cs)

        #Setting the Circle's Starting Coordinate to be the Bottom of the Train
        circle.move_to(rectangle)
        circle.shift(((rs-((1/2)*(cs*rs)))*DOWN))

        #Runtime for Photon Movement
        rt = 2.88

        print(rt)

        #Text for Time Scale
        tstext = Text("Time Scale = 0.00000001s per second")
        tstext.scale(0.67)
        tstext.shift(4*UL,DOWN,RIGHT)

        #Defining the path for Photon Movement

        xpath1 = Line(start=(1/2)*rectangle.width*LEFT,
                     end=rectangle.height*UP+(1/2)*rectangle.width*RIGHT,
                     color=RED)
        xpath1.set_fill(RED,opacity=0.3)
        xpath1.shift(((rs-((1/2)*(cs*rs)))*DOWN)+0.1*DOWN+0.01*LEFT)

        xpath2 = Line(end=(1/2)*rectangle.width*RIGHT,
                     start=rectangle.height*UP+(1/2)*rectangle.width*LEFT,
                     color=RED)
        xpath2.shift(((rs-((1/2)*(cs*rs)))*DOWN)+0.1*DOWN+0.01*LEFT+rectangle.width*RIGHT)
        xpath2.set_fill(RED,opacity=0.3)
        
        #Centering XPaths

        xpath1.shift((1/2)*rectangle.width*LEFT,(0.5*rectangle.height-0.25)*DOWN)
        xpath2.shift((1/2)*rectangle.width*LEFT,(0.5*rectangle.height-0.25)*DOWN)
        
        #Animation Playout for MObjects
        rectangle.scale(rs*1.05)
        
        self.play(Create(rectangle),
                  Create(circle),
                  Create(grid),
                  Write(tstext,runtime=0.5))
        
        self.play(Create(xpath1))
        self.play(Create(xpath2))

        #UP AND DOWN LOOP
        self.play(MoveAlongPath(circle,xpath1),
                  rectangle.animate.shift(0.5*grid.width*RIGHT+0.1*LEFT),
                  run_time=rt,
                  rate_func=rate_functions.linear)
        self.play(MoveAlongPath(circle,xpath2),
                  rectangle.animate.shift(0.5*grid.width*RIGHT+0.1*LEFT),
                  run_time=rt, 
                  rate_func=rate_functions.linear)

        #self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*UP),run_time=rt, rate_func=rate_functions.linear)
        #self.play(circle.animate.shift(2*((rs-((1/2)*(cs*rs))))*DOWN),run_time=rt, rate_func=rate_functions.linear)

if __name__ == '__main__':
    scene = PhotonClock()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)




