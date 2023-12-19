from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class SlideFourPartTwo(MovingCameraScene):
    def construct(self):
        
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
        person.set_stroke(color=RED,opacity=1)

        #Text for "Bob"
        bob = always_redraw(lambda: Tex("Bob").scale(0.8).next_to(person,UP))

        #Making a Car

        self.twidth = 10

        train = always_redraw(lambda:
            Rectangle(width=self.twidth,height=5)
        )
        trainscale = always_redraw(lambda:
            NumberLine(
            x_range=(0,self.twidth,(self.twidth*0.1)),
            length= train.width

        ).next_to(train,1.5*DOWN))

        trainmeasure = always_redraw(lambda:
            DecimalNumber(self.twidth,unit="m").next_to(trainscale,DOWN))
        
        velocityarrow = always_redraw(lambda:Arrow(start=0*LEFT,end=0.5*train.width*LEFT,color=RED).next_to(trainmeasure,1*DOWN))
        velocityarrow.shift(0.5*velocityarrow.width*LEFT)
        velocityarrowunit = always_redraw(lambda:Tex("v=0.5c").next_to(velocityarrow,RIGHT))

        #Alice Train

        atrain = Rectangle().scale(3).to_corner(UL)
        aperson = person.copy().set_stroke(color=BLUE,opacity=1).scale(1).move_to(0.575*atrain.get_bottom())
        alice = always_redraw(lambda: Tex("Alice").next_to(aperson,UP))




        #Animation Playout

        self.play(Create(person),
                  Write(bob))
        
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=train.width * 2.5))
        self.wait(0.3)

        self.play(AnimationGroup(Create(train),
                  AnimationGroup(person.animate.shift(0.5*train.height*DOWN+0.75*person.height*UP)),
                  AnimationGroup(Create(trainscale),Write(trainmeasure),lag_ratio=0.5),lag_ratio=0.5
                  ))
        person.save_state() 

        self.camera.frame.save_state()
        traingroup = VGroup(train,person)
        self.play(
                self.camera.frame.animate.set(width=train.width*6),
                self.camera.frame.animate.shift(2*UP+2*LEFT))


        atraingroup = VGroup(atrain,aperson,alice).shift(5.5*UL).scale(0.4)
        aperson.shift(0.1*UP)
        alice.shift(0.1*UP)
        self.play(Create(atrain),
                  Create(aperson))
        
        self.wait(2)

        self.play(GrowArrow(velocityarrow),
                  Create(velocityarrowunit),
                  train.animate.stretch((np.sqrt(3)*0.5),0),
                  person.animate.stretch((np.sqrt(3)*0.5),0),
                  trainmeasure.animate.set_value(8.66))





if __name__ == '__main__':
    scene = SlideFourPartTwo()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
