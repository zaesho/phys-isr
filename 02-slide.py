from manim import *
from math import *
import matplotlib as plt
import numpy as np
from trainbackend import *
from manim.utils.file_ops import open_file as open_media_file 

class SlideTwo(Scene):
    def construct(self):
        
        #TD Text
        td = Tex("Time Dilation")
        tdgraph = Tex("Time Dilation (Temporal Vs. Spatial Movement)")
        tdgraph.scale(0.6).shift(2.5*UP)

        #Play Out
        td.scale(2)
        self.play(Write(td),run_time=2)
        self.wait(0.5)
        self.play(ScaleInPlace(td,0.25))
        self.play(td.animate.shift(2.5*UP))
        self.play(Transform(td,tdgraph))

        #Defining Graph


        graph_axes = Axes(
            x_range=[0, 1, 0.25],
            y_range=[0, 1, 0.25],
            y_length=7,
            x_length=7,
            tips=False,
            axis_config={"include_numbers": True,"numbers_to_exclude": [0.25,0.75]},
            #y_axis_config={"scaling": LogBase(custom_labels=True)},
        ).add_coordinates()
        graph  = graph_axes.plot(lambda x: np.sqrt(1-(x**2)), x_range=(0, 1, 0.01),color=YELLOW)

        labels = graph_axes.get_axis_labels(
            Text("Spatial Speed").scale(0.45).shift(1.25*RIGHT), Text("Temporal Speed").scale(0.45).shift(2*UP)
        )

        fofc = Text("Displayed as multiples of c.").shift(5*LEFT+3*DOWN).scale(0.4)


        td_graph = VGroup(graph_axes,graph,labels).scale(0.65).shift(0.7*DOWN)
        td_graph -= graph
        self.play(Create(td_graph),Create(fofc))
        self.play(Create(graph),run_time=2)

        dot = Dot(radius=0.05) 
        

        dot.move_to(graph_axes.c2p(0,1))
        self.play(Create(dot))
        self.play(MoveAlongPath(dot,graph),
                  run_time=1.5)
        graph.reverse_direction()
        self.wait(0.2)
        self.play(MoveAlongPath(dot,graph),
                  run_time=2.5)
        
        td_graph += graph
        td_graph += dot
        td_graph += fofc

        self.play(FadeOut(td_graph))
        self.play(FadeOut(tdgraph))

        self.remove(all)


    


if __name__ == '__main__':
    scene = SlideTwo()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)