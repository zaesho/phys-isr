from isrbackend import *
from manim import *
from math import *


class CreateGraph(Scene):
    def construct(self):
        self.x_leftmost_tick = self.x_max+1
        self.y_bottom_tick = self.y_max+1 
        c = 3*(10**8)
        scaled_c= c/(10**7)
        axes = Axes(
            x_range=[-scaled_c*10, scaled_c*10],
            y_range=[-scaled_c*100, scaled_c*100],
            axis_config={"color": BLUE},
        )

        # Create Graph
        graph = axes.plot(lambda x: x/(sqrt((1-((x**2)/(c**2))))), color=WHITE)
        graph_label = axes.get_graph_label(graph, label="Solutions  of  t'(x)")

        # Display graph
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)