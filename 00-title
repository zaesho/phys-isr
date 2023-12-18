from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 



class Title(Scene):
    def construct(self):
        Title = Text("Time Dilation Explained")
        credits= Text("By:\nGian Villarini\nGavin Smith\nLucas Tan\nBraeden West").scale(0.6)

        self.add(Title)
        self.wait(1)
        self.play(FadeOut(Title))
        self.play(Write(credits))
        

if __name__ == '__main__':
    scene = Title()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)









