import knewtonalta as ka


def differentiate(equation):
    output = []
    for monomial in equation.monomials:
        new_monomial = ka.Monomial(monomial.coefficient * monomial.power, monomial.power - 1)
        if new_monomial.coefficient != 0:
            output.append(new_monomial)
    return ka.Equation(*output)


def instant_roc(equation, x):
    dif_equation = differentiate(equation)
    irc = dif_equation.solve(x)
    return irc
