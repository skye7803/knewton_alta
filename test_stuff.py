import knewtonalta as ka
import differentiate as diff

mono1 = ka.Monomial(1, 2)
mono2 = ka.Monomial(-3, 1)
mono3 = ka.Monomial(2, 0)

eq1 = ka.Equation(mono1, mono2, mono3)
eq1.display()
eq1d = diff.differentiate(eq1)
eq1d.display()

print(diff.instant_roc(eq1, 0))

# to be used later VVV

# eq1d = Equation(*eq1.differentiate())
# print(eq1d.display())

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
