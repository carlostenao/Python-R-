pais= input("Ingresa pais: ")


if pais.capitalize()=='Canada':
    provincia = input("Ingresa provincia: ")
    if provincia.capitalize() in('Alberta','Nunavut','Yukon'):
        tax = 0.05
    elif provincia.capitalize()=='Ontario':
            tax=0.13
    else:
        tax = 0.15
else:
    tax=0.0
print(tax)
