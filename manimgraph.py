from manim import *


class CreateGraph(Scene):
    def construct(self):
        

        # Create Graph
        graph = axes.plot(lambda x: x, color=WHITE,scaling=LogBase(base=2))
        graph_label = axes.get_graph_label(graph, label='x^{2}')


        # Display graph
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)