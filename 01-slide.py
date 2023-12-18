from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class Intro(MovingCameraScene):
    def construct(self):
        c=3.00*10**8 #Speed of Light
        v=0.5*c #Alice Velocity
        sf=scalingfactor(v) #Relativistic Scaling Factor for Alice
        t_len = 1 #(In Kilometers); The length of the train track is 10 units, which will arbitrarily represent 1 kilometer.
        rt=((t_len*1000)/v)*(10**6) #Runtime for Alice Train Motion.
        print(rt)

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

        #Defining a Stick Figure VGroup
        person = VGroup()
        person.add(head,body,rleg,lleg)
        person.scale(0.5)
        person.set_stroke(color=BLUE,opacity=1)

        #Text for "Alice"
        alice = Tex("Alice")
        alice.shift(1.25*UP)
        alice.scale(0.8)

        self.play(Create(person),
                  Write(alice))

        #Making a Train
        train = Rectangle()
        train.scale(3)

        self.play(Create(train),
                  person.animate.move_to(0.575*train.get_bottom()),
                  alice.animate.move_to(train.get_center())
        )
        
        #Adjusting the Camera to Zoom Out

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=train.width * 3))
        self.wait(0.3)

        #Making the "Tracks"

        traintrack = NumberLine(
            x_range=[0, 1000*t_len, 100],
            length=25,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
        ).move_to(train.get_bottom()).shift(1.75*UP).set_fill(color=WHITE,opacity=0.5)

        #Defining Bob
        personb = person.copy().set_stroke(color=RED,opacity=1).scale(2).move_to(train.get_end()).shift(8*DOWN+2*RIGHT)
        bob = Tex("Bob").move_to(personb.get_top()).shift(0.5*UP)
        
        #Rendering Tracks, Bob
        self.play(train.animate.shift(2*UP),
                  person.animate.shift(2*UP),
                  alice.animate.shift(2*UP),
                  Create(personb),
                  Write(bob))
        self.play(FadeIn(traintrack),runtime=3)

        #Defining Bob's Stopwatch Clock
        stopwatch = DecimalNumber(0,
            unit="\mu s")
        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            mob.set_value(0+self.clock)
        casing = Circle().surround(stopwatch,buffer_factor=1.5).set_stroke(color=YELLOW,opacity=0.8)
        clock = VGroup(stopwatch,casing)
        clock.move_to(personb)
        clock.shift(2*LEFT)

        #Defining Alice's Stopwatch Clock
        a_stopwatch = DecimalNumber(0,
           unit="\mu s")
        self.aclock = 0
        def update_atimer(mob, dt):
            self.aclock += dt*sf
            mob.set_value(0+self.aclock)
        acasing = Circle().surround(a_stopwatch,buffer_factor=1.5).set_stroke(color=RED,opacity=0.8)
        aclock = VGroup(a_stopwatch,acasing)

        #Alice Objects VGroup
        alicetrain = VGroup(alice,train,person)

        #Moving Alice To The Start of the Track
        self.play(FadeOut(alicetrain),run_time=0.5)
        alicetrain.move_to(traintrack.get_start())
        alicetrain.shift(0.5*alicetrain.height*UP)
        self.play(Create(alice),
                  Create(train),
                  Create(person),
                  run_time=1)
        self.camera.frame.save_state()
        self.wait(0.5)

        #Creating the Stopwatch

        self.play(Create(clock),
                self.camera.frame.animate.set(width=clock.width * 6).move_to(clock),
                alicetrain.animate.stretch(sf,1))
        self.play(Flash(casing,flash_radius=1.15))
        self.play(Restore(self.camera.frame))
        self.wait(0.5)
    
        #Alice Begins Moving
        stopwatch.add_updater(update_timer)
        self.play(alicetrain.animate.shift(2.04*traintrack.get_end()*RIGHT),
            run_time=rt,
            rate_func=rate_functions.linear)
        stopwatch.remove_updater(update_timer)
        self.wait(2)

        #Calculate the Velocity

        v_alice = MathTex("\frac{1km}{6.67\mu s}=\frac{1}{2}c")
        #Playout Velocity Calculations

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=50))
        self.play(self.camera.frame.animate.shift(12*UP))
        v_alice.shift(12*UP)
        self.play(self.camera.frame.animate.set(width=2),
                  Write(v_alice))
        self.wait(3)
        self.play(Restore(self.camera.frame))



        #Give Alice Her Clock
        self.play(FadeOut(alicetrain),
                  stopwatch.animate.set_value(0))
        alicetrain.move_to(traintrack.get_start())
        alicetrain.shift(0.5*alicetrain.height*UP)
        aclock.move_to(traintrack.get_midpoint())
        aclock.shift(7*UP)
        self.play(Create(alicetrain),
                  Create(aclock))
        self.wait(1)

        
        #Defining Alice Jump Path

        xpath1 = Line(start=(1/8)*traintrack.width*LEFT,
                     end=(1/8)*traintrack.width*RIGHT+1*UP,
                     color=RED)
        xpath1.set_fill(RED,opacity=0.3)
        xpath2 = Line(start=(1/8)*traintrack.width*LEFT+1*UP,
                     end=(1/8)*traintrack.width*RIGHT,
                     color=RED)
        xpath2.set_fill(RED,opacity=0.3) 

        xpath2.shift((1/4)*traintrack.width*RIGHT)
        xpath1.shift(0.05*UP)
        xpath2.shift(0.05*UP)
        xpath1.shift((1/8)*traintrack.width*RIGHT)
        xpath2.shift((1/8)*traintrack.width*RIGHT)

        stopwatch.set_value(0)
        self.clock = 0
        stopwatch.add_updater(update_timer)

        
        self.play(
            alicetrain.animate.shift(0.5*(2.04*traintrack.get_end())*RIGHT),
            run_time=0.5*rt,
            rate_func=rate_functions.linear)
        stopwatch.remove_updater(update_timer)
        self.play(stopwatch.animate.set_value(0))
        
        self.aclock = 0 
        self.clock = 0


        self.wait(2)
        self.play(FadeOut(alice),run_time=0.2)
        stopwatch.add_updater(update_timer)
        a_stopwatch.add_updater(update_atimer)
        self.play(
            MoveAlongPath(person,xpath1),
            train.animate.shift(0.25*(2.04*traintrack.get_end())*RIGHT),
            run_time=0.25*rt,
            rate_func=rate_functions.linear)
        self.play(
            MoveAlongPath(person,xpath2),
            train.animate.shift(0.25*(2.04*traintrack.get_end())*RIGHT),
            run_time=0.25*rt,
            rate_func=rate_functions.linear)
        
        stopwatch.remove_updater(update_timer)
        a_stopwatch.remove_updater(update_atimer)
        self.wait(2)

        #Fade Everything Out, Highlight the Clocks

        alicetrain -= alice
        self.play(FadeOut(alicetrain),
                  FadeOut(traintrack),
                  FadeOut(bob),
                  FadeOut(personb),
                  run_time=0.5)
        #Define New "Equals" Text

        notequal = Text("≠")
        phantomr = Point().shift(2*RIGHT)
        phantoml = Point().shift(2*LEFT)

        self.camera.frame.save_state()
        self.play(Write(notequal),
                  clock.animate.move_to(phantomr),
                  aclock.animate.move_to(phantoml),
                  self.camera.frame.animate.set(width=9),
                  run_time=2)
        
        
        



if __name__ == '__main__':
    scene = Intro()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)









