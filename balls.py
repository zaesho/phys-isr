from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 


class Balls(Scene):
    def construct(self):
        grid = NumberPlane(background_line_style={"stroke_opacity": 0.3})
        self.add(grid)
        num_balls = 2
        speed = 1 # units per second
        balls = [Circle(radius=0.25, color=RED) for _ in range(num_balls)]
        paths = [Line(start=2*j*UP+3*LEFT, end=2*j*UP+2*(j)*RIGHT, color=RED) for j in range(num_balls)]
        self.add(*[path for path in paths])
        animations = [MoveAlongPath(ball, path, rate_func=linear, run_time=path.get_length()/speed) for ball, path in zip(balls, paths)]
        self.play(AnimationGroup(*animations))

if __name__ == '__main__':
    scene = Balls()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)