from calculadora_ti import calcular_bonus_ti

# 01-engenharia-de-software/test_calculadora_ti.py

# O teste define o comportamento esperado do sistema
def test_deve_calcular_bonus_para_desenvolvedor_senior():
    salario_base = 10000
    cargo = "Senior"

    # Esperamos que uma função (que ainda não criamos) calcule o bônus correto
    # Um Sênior deve ganhar 20% de bônus (10000 * 0.20 = 2000)
    bonus_calculado = calcular_bonus_ti(salario_base, cargo)

    assert bonus_calculado == 2000
