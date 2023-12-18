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
            x_range=[0, 10, 5],
            length=2*rectangle.width,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,

        )
        grid.shift(2*DOWN)
        label = Text("Meters").scale(0.45)

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
        rt = 3.33

        print(rt)

        #Text for Time Scale
        tstext = MathTex("Time\,Scale=\\frac{10\\,ns}{1\\,s}")
        tstext.scale(0.67)
        tstext.shift(4*UL,DOWN,RIGHT)

        #Defining the path for Photon Movement

        xpath1 = Line(start=(1/2)*rectangle.width*LEFT,
                     end=rectangle.height*UP+(1/2)*rectangle.width*RIGHT,
                     color=RED)
        xpath1.set_fill(RED,opacity=0.05).set_stroke(RED,opacity=0.3)
        xpath1.shift(((rs-((1/2)*(cs*rs)))*DOWN)+0.1*DOWN+0.01*LEFT)

        xpath2 = Line(end=(1/2)*rectangle.width*RIGHT,
                     start=rectangle.height*UP+(1/2)*rectangle.width*LEFT,
                     color=RED)
        xpath2.shift(((rs-((1/2)*(cs*rs)))*DOWN)+0.1*DOWN+0.01*LEFT+rectangle.width*RIGHT)
        xpath2.set_fill(RED,opacity=0.05).set_stroke(RED,opacity=0.3)
        
        #Centering XPaths

        xpath1.shift((1/2)*rectangle.width*LEFT,(0.5*rectangle.height-0.25)*DOWN)
        xpath2.shift((1/2)*rectangle.width*LEFT,(0.5*rectangle.height-0.25)*DOWN)

        #Defining Stopwatch Clock
        stopwatch = DecimalNumber(0,
            unit="ns")
        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            mob.set_value(0+self.clock)
        casing = Circle().surround(stopwatch,buffer_factor=1.5).set_stroke(color=RED,opacity=0.8)
        clock = VGroup(stopwatch,casing)
        clock.shift(4*RIGHT+3*UP).scale(0.5)
        
        #Rectangle Dimensioner
        rectangle.save_state()
        rectangle.move_to(ORIGIN)
        headert = Text("Train").shift(2.5*UP).scale(0.8)
        theight = Vector([0,rectangle.height]).next_to(rectangle).set_stroke(color=RED).set_fill(RED)
        heighttext = Text("10m").next_to(theight).scale(0.5)
        tvelocity = Vector([0.5*rectangle.width,0]).shift(2*DOWN).scale(0.8).set_stroke(color=YELLOW).set_fill(YELLOW)
        velocitytext = MathTex("v = \\frac{1}{2}c").shift(2*DOWN+0.5*LEFT).scale(0.5)

        self.play(Create(rectangle))
        self.play(Create(theight),
                  Write(heighttext),
                  Write(headert))
        
        self.wait(1)

        self.play(Create(tvelocity),
                  Write(velocitytext))
        
        self.wait(1)
    
        self.play(FadeOut(rectangle),
                  FadeOut(theight),
                  FadeOut(heighttext),
                  FadeOut(tvelocity),
                  FadeOut(velocitytext),
                  FadeOut(headert))
        
        rectangle.restore()


    
        #Animation Playout for Movement
        rectangle.scale(rs*1.05)
        
        label.shift(3*DOWN)
        self.play(Create(rectangle),
                  Create(circle),
                  Create(grid),
                  Write(label),
                  Write(tstext,runtime=0.5),
                  Create(clock))
        
        self.play(Create(xpath1))
        self.play(Create(xpath2))
        self.add(circle)

        #UP AND DOWN LOOP
        stopwatch.add_updater(update_timer)
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




