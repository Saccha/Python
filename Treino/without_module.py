def divisao(dividendo,divisor):
    quociente = 0
    resto = dividendo
    while (resto - divisor >= 0):
        quociente += 1
        resto = resto - divisor
    
    return quociente, resto

print("Quociente e resto")
print( divisao(20, 4) )
