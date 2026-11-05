# 01-engenharia-de-software/calculadora_ti.py

def calcular_bonus_ti(salario, cargo):
    if cargo == "Senior":
        return salario * 0.20
    elif cargo == "Pleno":
        return salario * 0.10
    return salario * 0.05
