#!/usr/bin/python26
''' Use this pattern when you are comparing two pairs, say (A, B) and comparing
    it against (X, Y) and you need to do something different for every
    combination of match and mismatch. For example, if A == X and B == Y,
    you want to do task1; if A == X and B != Y, you would do task2, etc.
'''
################################################################################
# PATTERN
################################################################################

class CompareAndDo(object):
    def __init__(self):
        self.func = {'TT':self.a_eq_x_b_eq_y, 'TF':self.a_eq_x_b_neq_y, 'FT':self.a_neq_x_b_eq_y, 'tt':self.a_eq_y_b_eq_x, 'tf':self.a_eq_y_b_neq_x, 'ft':self.a_neq_y_b_eq_x, 'ff':self.none_of_them_equal}

    def run(self, u, v):
        forward = self.true_false_forward(u, v)
        backward = self.true_false_backward(u, v)
        if 'T' in forward:
            return self.func[forward]()
        elif 't' in backward:
            return self.func[backward]()
        else:
            return self.func['ff']()

    def true_false_forward(self, u, v):
        # will return any of these combinations: TT, TF, FT, FF
        return ('T' if u[0] == v[0] else 'F') + ('T' if u[1] == v[1] else 'F')

    def true_false_backward(self, u, v):
        # will return any of these combinations: tt, tf, ft, ff
        return ('t' if u[0] == v[1] else 'f') + ('t' if u[1] == v[0] else 'f')

    def a_eq_x_b_eq_y(self): # responds to TT
        return 'a equals x, b equals y'

    def a_eq_x_b_neq_y(self): # responds to TF
        return 'a equals x, b not equal y'

    def a_neq_x_b_eq_y(self): # responds to FT
        return 'a not equal to x, b equal to y'

    def a_eq_y_b_eq_x(self): # responds to tt
        return 'a equals y, b equals x'

    def a_eq_y_b_neq_x(self): # responds to tf
        return 'a equals y, b not equal to x'

    def a_neq_y_b_eq_x(self): # responds to ft
        return 'a not equal to y, b equals x'

    def none_of_them_equal(self): # responds to FF or ff
        return 'none of them are equal'

print('using pattern')
a, b = [1, 2]
x, y = [2, 3]
c = CompareAndDo()
print(c.run([a, b], [x, y]))

################################################################################
# Code to be replaced
################################################################################

print('\n\nusing ordinary approach')
a, b = [1, 2]
x, y = [4, 3]
if a == x:
    if b == y:
        print('a equals x, b equals y')
    else:
        print('a equals x, b not equal to y')
elif b == y:
    print('a not equal to x, b equals y')
elif a == y:
    if b == x:
        print('a equals y, b equals x')
    else:
        print('a equals y, b not equal to x')
elif b == x:
    print('a not equal to y, b equals x')
else:
    print('none of them are equal')
