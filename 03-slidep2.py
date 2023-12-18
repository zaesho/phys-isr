from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class SidebySide(Scene):
    def construct(self):
        alicet = Text("Alice").scale(0.4).shift(2.15*LEFT+1.25*UP)
        bobt = Text("Bob").scale(0.4).shift(2.15*RIGHT,1.25*UP)
        header = Text("Frame of Reference Comparison").scale(0.6).shift(2.25*UP)
        alicer = Rectangle().set_fill(opacity=0).set_stroke(color=BLUE,opacity=1).scale(1).shift(2.15*LEFT)
        bobr = Rectangle().set_fill(opacity=0).set_stroke(color=RED,opacity=1).scale(1).shift(2.15*RIGHT)

        self.add(header)
        self.add(alicer)
        self.add(bobr)

        self.play(Write(alicet),
              Write(bobt))



if __name__ == '__main__':
    scene = SidebySide()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
