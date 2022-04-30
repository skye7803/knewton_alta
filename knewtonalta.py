import numpy as np


class Monomial:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def display(self):
        display_list = [str(self.coefficient), "x", "^", str(self.power)]
        if self.power == 0:
            display_list.remove("x")  
            display_list.remove("^")
            display_list.remove(str(self.power))
        elif self.power == 1 or self.power == -1:
            display_list.remove("^")
            display_list.remove(str(self.power))
        if self.coefficient == 1:
            display_list.remove(str(self.coefficient))
        elif self.coefficient == -1:
            display_list[0] = "-"
        
        return "".join(display_list)


class Equation:
    def __init__(self, *args):
        self.monomials = args

    # For some reason this function prints 'None' as well as what I want it to when displaying a differentiated function
    def display(self):
        display_list = []
        for monomial in self.monomials:
            display_list.append(monomial.display())
            
        print(" + ".join(display_list))

    def quad_equation(self, empty_var="", return_eq=False):
        a = self.monomials[0].coefficient
        if empty_var == 'b':
            b = 0
            c = self.monomials[1].coefficient
        elif empty_var == 'c':
            b = self.monomials[1].coefficient
            c = 0
        else:
            b = self.monomials[1].coefficient
            c = self.monomials[2].coefficient
        if np.sqrt(b ** 2 - 4 * a * c >= 0):
            pos_x = (-b + np.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
            neg_x = (-b - np.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
            if return_eq:
                print((str(-b) + " + or - sqrt(" + str(b**2 - 4 * a * c) + ") / " + str(2 * a)))
            return pos_x, neg_x
        else:
            raise ValueError

    def differentiate(self):
        output = []
        for monomial in self.monomials:
            new_monomial = Monomial(monomial.coefficient * monomial.power, monomial.power - 1)
            if new_monomial.coefficient != 0:
                output.append(new_monomial)
        return output

    def solve(self, x):
        answer = 0
        for monomial in self.monomials:
            answer += (monomial.coefficient * x ** monomial.power)
        return answer


mono1 = Monomial(-5/3, 3)
mono2 = Monomial(10, 2)
mono3 = Monomial(-15, 1)
mono4 = Monomial(-5, 0)

eq1 = Equation(mono1, mono2, mono3)
eq1.display()

eq1d = Equation(*eq1.differentiate())
print(eq1d.display())

# eq1d2 = Equation(*eq1d.differentiate())
# print(eq1d2.display())
#
# print(eq1d.quad_equation(return_eq=True))
#
# x1, x2 = eq1d.quad_equation()
#
# if eq1d2.solve(x1) > 0:
#     print(str(x1) + ' is a local minimum')
# else:
#     print(str(x1) + ' is a local maximum')
#
# if eq1d2.solve(x2) > 0:
#     print(str(x2) + ' is a local minimum')
# else:
#     print(str(x2) + ' is a local maximum')
