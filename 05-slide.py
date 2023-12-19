from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class SlideFive(Scene):
    def construct(self):
        derivationheader = Text("Derivation")

        self.play(Write(derivationheader))
        self.play(derivationheader.animate.scale(0.5).to_corner(UP))

        straightline = Line(start=1*DOWN,end=1*UP,color=YELLOW).shift(2*LEFT)
        dot_a = Dot(radius=0.05).move_to(straightline).shift(DOWN)

        triangularpath = Line(start=1*DOWN+1*LEFT,end=1*UP+1*RIGHT,color=RED).shift(2*RIGHT)
        dot_b = Dot(radius=0.05).move_to(triangularpath).shift(DL)

        self.play(AnimationGroup(Create(straightline),Create(dot_a),lag_ratio=0.5),
                AnimationGroup(Create(triangularpath),Create(dot_b),lag_ratio=0.5))
        
        self.play(AnimationGroup(MoveAlongPath(dot_a,straightline),MoveAlongPath(dot_b,triangularpath)))

        straightline.reverse_direction()
        triangularpath.reverse_direction()

        self.wait(0.2)

        self.play(AnimationGroup(MoveAlongPath(dot_a,straightline),MoveAlongPath(dot_b,triangularpath)))

        self.play(FadeOut(dot_a,dot_b,triangularpath,straightline))

        atext = Text("a")
        self.play(Create(atext))
        self.wait(0.3)
        self.play(FadeOut(atext))
        self.wait(0.5)
        stationarys = Tex("S").set_stroke(color=RED,opacity=1)
        stationarytimetaken = MathTex("S\\,=\\,\\frac{2h}{c}")

        self.play(Write(stationarys))
        self.wait(0.2)
        self.play(Transform(stationarys,stationarytimetaken))
        self.wait(0.2)
        self.play(FadeOut(stationarys))
        
        sprime = MathTex("S^{'}").set_stroke(color=BLUE,opacity=1)

        self.play(Write(sprime))
        self.play(sprime.animate.shift(3*LEFT))
        self.play(sprime.animate.set_fill(color=WHITE,opacity=0.4))

        rtri = Polygon([-1,-1,0],[1,1,0],[1,-1,0]).set_stroke(color=YELLOW,opacity=1)
        self.play(Create(rtri))

        sidelengths = VGroup( 
            MathTex("h").next_to(rtri,RIGHT),
            MathTex("v\cdot t_{s}").next_to(rtri,DOWN),
        )

        self.play(Create(sidelengths),run_time=2)

        t_distance = MathTex("d =\\,2\\sqrt{h^2+(v\\cdot t)^2}")  
        tsubs = MathTex("t_s=2 \\sqrt{h^2+( \\frac{v \\cdot t}{2})^2}\\,\\,\\cdot {\\frac{1}{c}}")
        solvedtsubs = MathTex("t_s = \\frac{2h}{\\sqrt{c^2-v^2}}")

        unsolveda = MathTex("\\frac{2h}{\\sqrt{c^2-v^2}} = a(\\frac{2h}{c})")
        solveda = MathTex("a = \\frac{c}{\\sqrt{c^2-v^2}}")

        self.play(FadeOut(rtri),
                  FadeOut(sidelengths))
        self.play(Write(t_distance))
        self.play(t_distance.animate.shift(2*UP).scale(0.5).set_fill(color=WHITE,opacity=0.4),
                  sprime.animate.move_to(ORIGIN).set_fill(color=WHITE,opacity=1))
        self.play(Transform(sprime,tsubs))
        self.wait(0.5)
        self.play(Transform(sprime,solvedtsubs))
        self.play(FadeOut(t_distance),
                  AnimationGroup(sprime.animate.shift(2*UP).scale(0.5).set_fill(opacity=0.4),
                                 Write(unsolveda),lag_ratio=0.5))
        self.wait(0.5)
        self.play(Transform(unsolveda,solveda))

        shrinkingfactorarrow = Arrow(start=1*DL,end=1*UR).next_to(unsolveda,DL).set_fill(color=YELLOW).set_stroke(color=YELLOW)
        shrinkingfactortext = Text("Shrinking Factor").scale(0.5).next_to(shrinkingfactorarrow,DL)

        self.play(Create(shrinkingfactorarrow))
        self.play(Write(shrinkingfactortext),run_time=0.5)

        self.wait(0.5)

        self.play(FadeOut(shrinkingfactorarrow),
                  FadeOut(shrinkingfactortext))
        solvedgamma = MathTex("\\gamma = \\frac{c}{\\sqrt{c^2-v^2}}")

        self.play(Transform(unsolveda,solvedgamma))

        solvedgammac = MathTex("\\gamma = \\frac{1}{\\sqrt{1-\\frac{v^2}{c^2}}")
        
        self.play(Transform(unsolveda,solvedgammac))



    

        


if __name__ == '__main__':
    scene = SlideFive()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
