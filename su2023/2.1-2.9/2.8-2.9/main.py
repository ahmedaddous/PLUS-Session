from manim import *
from random import random
# import numpy as np

class RepresentSubspace(VectorScene):
    def construct(self):
        plane = NumberPlane(
                    x_range=(-15, 15, 1),
                    y_range=(-8, 8, 1),
                    x_length=5,
                    y_length=2
                )
        basis_vec = Vector([1, 2, 0], color=PINK)
        
        self.add_plane(animate=True)
        self.wait(2)
        self.play(Create(basis_vec))
        self.wait()
        self.play(Write(basis_vec.coordinate_label(color=PINK)))
        self.wait()

        for i in np.arange(-2, 2, 0.2):
            self.play(
                    Create(
                        Vector(
                            basis_vec.get_end() * i,
                            color=YELLOW,
                            stroke_width=2
                        )
                    ),
                    duration=0.25
                )

        self.wait(2)

    def calculate_span(self,list_of_vecs: List[Vector], sample_size: int) -> List[Vector]:
        """
        The purpose of this method is, given a number of vectors, to calculate a number of
        the vectors in their span. The method should be able to calculate the vectors and put
        them in a list, but it'll not animate them.

        INPUT:
        sample_size  (int): The number of vectors to calculate from the span of list_of_vecs
        list_of_vecs (List[Vector]): The vectors whose span I'm taking

        OUTPUT:
        List[Vector]: A subset of the span of list_of_vecs 
        """
        sample_span = [random()]
