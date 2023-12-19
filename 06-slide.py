from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class SlideSix(Scene):
    def construct(self):
        lengthcontraction = Text("Length Contraction")

        self.play(Write(lengthcontraction))
        self.wait(3)
        self.play(lengthcontraction.animate.shift(3*UP).scale(0.5))

        s_text = MathTex("S")
        s_circ = Circle().surround(s_text,buffer_factor=1.75).set_stroke(color=YELLOW)
        frame_s = VGroup(s_text,s_circ)
        
        self.play(Create(frame_s))
        self.play(frame_s.animate.shift(2*UP))

        rod = Line(start=2*LEFT,end=2*RIGHT).shift(0.5*DOWN+LEFT)
        rodvector= Arrow(start=1*LEFT,end=1*RIGHT,color=YELLOW)
        rodvector.next_to(rod,RIGHT)
        rodvel = always_redraw(lambda: Text("v").next_to(rodvector,DOWN))

        self.play(Create(rod))
        self.play(AnimationGroup(GrowArrow(rodvector),Create(rodvel),lag_ratio=0.5))

        stopwatch = DecimalNumber(0,
            unit="\mu s")
        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            mob.set_value(0+self.clock)
        casing = Circle().surround(stopwatch,buffer_factor=1.5).set_stroke(color=RED,opacity=0.8)
        clock = VGroup(stopwatch,casing)
        clock.shift(2*DOWN).scale(0.6)
        self.play(GrowFromCenter(clock))

        self.wait(2)

        s_prime = MathTex("S^{'}").shift(2*UP)

        self.play(AnimationGroup(s_circ.animate.set_stroke(color=RED),Transform(s_text,s_prime)),
                  AnimationGroup(rodvector.animate.next_to(clock,RIGHT),rod.animate.shift(RIGHT),lag_ratio=0.5))
        self.wait(0.5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        conventions = Text("First, some conventions...").shift(2*UP).set_fill(color=BLUE)
        sprimeconvention = MathTex("A.\\,Measurements\\,in\\,S^{'}\\,will carry\\,'\\,.").set_fill(color=YELLOW)
        stationaryconvention = MathTex("B.\\,Measurements\\,in\\,stationary\\,frames\\\will\\,be\\,denoted\\,with\\,subscript\\,X_{o}.").set_fill(color=YELLOW).shift(1.5*DOWN)

        self.play(AnimationGroup(Write(conventions),Write(sprimeconvention), lag_ratio=0.5))
        self.wait(0.2)
        self.play(sprimeconvention.animate.set_fill(color=WHITE),
                  Write(stationaryconvention))
        self.wait(0.2)
        self.play(stationaryconvention.animate.set_fill(color=WHITE))

        self.wait(0.5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        doubleequations = MathTex("T_{o}\\,=\\,\\frac{L}{v}\\,\\,\\,and\\,\\,\\,T^{'}\\,=\\,\\frac{L^{'}_{o}}{v}").set_stroke(color=BLUE)
        vsolve = MathTex("v\\,=\\,\\frac{L}{T_{o}}\\,=\\,\\frac{L^{'}_{o}}{T^{'}}").set_stroke(color=BLUE)
        crossmultiplication = MathTex("\\frac{T^{'}}{T_{o}}\\,=\\,\\frac{L^{'}_{o}}{L^{'}}").set_stroke(color=BLUE)
        gammaequivalence = MathTex("\\frac{T^{'}}{T_{o}}\\,=\\,\\frac{L^{'}_{o}}{L^{'}}\\,=\\,\\gamma").set_stroke(color=BLUE)

        self.play(Write(doubleequations))
        self.wait(0.5)
        self.play(Transform(doubleequations,vsolve))
        self.wait(0.5)
        self.play(Transform(doubleequations,crossmultiplication))
        self.wait(0.5)
        self.play(Transform(doubleequations,gammaequivalence))
        self.wait(0.5)








        



if __name__ == '__main__':
    scene = SlideSix()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
