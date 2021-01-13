import sympy as sym
from sympy import symbols, functions

import typing
from typing import List

class w_vec:

    def __init__(self, inpt_vector: List[symbols]):
        self.vector = inpt_vector
        self.dimension = len(inpt_vector)

    def compute_magnitude(self)->symbols:
        sum = 0
        for element in self.vector:
            sum += element ** 2
        return sym.sqrt(sum)

    #figure out type
    def same_dim(self, other)->bool:
        if self.dimension == other.dimension:
            return True
        return False
    
    def dot_product(self,other)->symbols:
        dot_sum = 0
        for element in range(0,self.dimension):
            dot_sum += self.vector[element] * other.vector[element]
        return dot_sum

    def __add__(self, other):
        added_vec = []
        ####need to make sure can add
        for vec_it in range (0,self.dimension):
            added_vec.append(self.vector[vec_it] + other.vector[vec_it])
        return added_vec
    

    def scale(self,scalar:symbols):
        scale_vec = []
        for element in self.vector:
            scale_vec.append(element*scalar)
        return w_vec(scale_vec)
