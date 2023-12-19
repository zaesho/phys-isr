from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class SceneFour(MovingCameraScene):
    def construct(self):

        head = Circle()
        head.scale=0.5
        head.shift(UP)
        
        #Creating MObjects for the Stick Figures
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


        self.vel = 1
        def vector_inc(mob,dt):
            self.vel += dt
            mob.set_value(0+self.vel)
        
        self.velo = 0
        def vector_incr(mob,dt):
            self.velo += dt*0.125
            mob.set_value(0+self.velo)

        self.theight = 1
        self.theightsf = 1
        self.alicesize = 1
        def scaler(mob,dt):
            sf = scalingfactor(self.velo*(3*10**8))
            self.theightsf = sf+(0*dt)
            self.alicesize = (1-(sf*dt))
            print(self.theightsf)
            heightarrow.next_to(train,1.5*UP)
            mob.set_value(sf)
        def height_dec(mob,dt):
            self.theight -= dt*0.05
            mob.set_value(0+self.theight)
            heightarrow.next_to(train,1.5*UP)
        
        #Making a Train
        train = always_redraw(lambda:Rectangle(
            width=self.theightsf*6,
            height=3
            
        ).set_fill(color=BLUE,opacity=0.2))

        #Defining a Stick Figure VGroup
        person = always_redraw(lambda:VGroup(head,body,rleg,lleg).scale((self.alicesize)).move_to(0.575*train.get_bottom()))
        person.scale(0.5)
        person.set_stroke(color=BLUE,opacity=1)

        #Text for "Alice"
        alice = Tex("Train")
        alice.shift(1.25*UP)
        alice.scale(0.8)


        self.play(Write(alice))
        
        self.play(Create(train),
                  alice.animate.move_to(train.get_center())
        )
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=train.width * 3.5))
        self.wait(0.3)



        heightarrow = always_redraw(lambda: Arrow(start=LEFT,end=train.height*self.theight*RIGHT,color=YELLOW)).next_to(train,1.5*UP)
        heightunit = Tex("l=").next_to(heightarrow,UP)
        heighttext = DecimalNumber(self.theightsf,unit="m").next_to(heightunit,RIGHT)
    


        velocity = always_redraw(lambda: Arrow(start=LEFT,
                         end=(self.vel)*RIGHT,
                         color=RED,
                         ).next_to(train,1.5*DOWN))
        
        
        
        velval = always_redraw(lambda: DecimalNumber(self.velo,unit="c").next_to(velocity,LEFT))

        vequals = always_redraw(lambda:Tex("v=").next_to(velval,LEFT))


        self.play(AnimationGroup(GrowArrow(velocity.next_to(train,1.5*DOWN)),GrowArrow(heightarrow)),
                Write(velval.next_to(velocity,LEFT)), 
                Write(vequals),
                Write(heightunit),
                Write(heighttext))
        heightarrow.add_updater(scaler)
        velocity.add_updater(vector_inc)
        velval.add_updater(vector_incr)
        heighttext.add_updater(scaler)
        train.add_updater(scaler)
        self.wait(8)


if __name__ == '__main__':
    scene = SceneFour()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
