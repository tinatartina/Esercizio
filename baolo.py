lista_1 = ["freddo", "caldo", "ghiacciato", "tiepido"]
print(lista_1[0])
print(lista_1[-1])
print(lista_1[1:3])
lista_1[1] = "bollente"#cambia il valore di una variabile in una lista 
print(lista_1)
lista_1[0:2] = ["cold", "boiling"] 
print(lista_1)
lista_1.append("freezing")
print(lista_1)
lista_1.insert(2, "evaporato")
print(lista_1)
lista_2 = ["acqua", "thè", "coca-cola"]
lista_1.extend(lista_2)
print(lista_1)
bibite = ("fanta", "sprite", "cedrata")
lista_1.extend(bibite)
print(lista_1)