import numpy as np
from manim import *

class ClockTest(Scene):
    def construct(self):
        dn = DecimalNumber(0)
        self.add(dn)

        self.clock = 0
        def update_timer(mob, dt):
            self.clock += dt
            mob.set_value(5-self.clock)

        dn.add_updater(update_timer)
        self.wait(5.02)