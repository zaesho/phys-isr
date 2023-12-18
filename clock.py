from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 

class ClockTest(Scene):
    def construct(self):
        dn = DecimalNumber(0)
        self.add(dn)

        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            mob.set_value(0+self.clock)

        dn.add_updater(update_timer)
        self.wait(5.02)


if __name__ == '__main__':
    scene = ClockTest()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
