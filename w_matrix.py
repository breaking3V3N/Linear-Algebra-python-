import sympy as sym
import typing

from   sympy import symbols,functions
from typing import List

from w_vector import w_vec
class w_mat:

    def __init__(self, inpt_matrix: List[w_vec]):
        self.rows = inpt_matrix
        self.num_rows = len(self.rows)

        self.num_cols = self.rows[0].dimension
        self.cols = self.get_cols()


    def get_cols(self):
        agg_cols = []
        for col_iter in range(0,self.num_cols):
            col = []
            for row in self.rows:
                col.append(row.vector[col_iter])
            agg_cols.append(col)
        return agg_cols

    def get_col(self, index: int )->w_vec:
        return self.cols[index]

    def get_row(self, index: int) -> w_vec:
        return self.rows[index]

    def can_mult(self,other)->bool:
        """

        :param other:
        :return:
        """
        if self.num_cols == other.num_rows:
            return True
        else:
            return False



    def __mul__(self, other):
        if self.can_mult(other):
            new_mat = []
            for row in self.rows:
                new_row = []
                for col in other.cols:
                    new_row.append(row.dot_product(w_vec(col)))
                new_mat.append(w_vec(new_row))
            return w_mat(new_mat)



    """
    def deleted_matrix(self,row_index:int,col_index:int):
        return self.

    #def calc_determinant(self)->symbols:


    MAKE RECURSIVE

    def __pow__(self, power, modulo=None):

        for x in range(1,power+1):



    def can_add
    
    def can_mult

    def __add__(self,other):
        for row_iter in self.num_rows:
            for col_iter in other.num_cols:
    """



x,y,z,c = symbols('x y z c')

x1,y1,z1,c1 = symbols('x1 y1 z1 c1')
x2,y2 = symbols('x2 y2')

a = w_vec([x,y,z])
b = w_vec([x1,y1,z1])
mat = w_mat([w_vec([x,y]),w_vec([z,c])])
mat_1 = w_mat([w_vec([x1,y1]),w_vec([x2,y2])])

n_mat = mat*mat_1
print(n_mat.get_cols())