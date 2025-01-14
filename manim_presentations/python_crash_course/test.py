from manim import *

class Test(Scene):
    def construct(self):
        code = Code(code="x = 3", language='python')
        self.play(Write(code))