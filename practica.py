
def calcular(nota):
    if nota > 75.0:
        return ("O")
    elif nota >= 60.0 and nota <= 75.0:
        return ("A")
    elif nota >= 50.0 and nota <= 59.0:
        return ("B")
    elif nota >= 40.0 and nota <= 49.0:
        return ("C")
    elif nota < 40.0:
        return ("D")
    else: 
        return -1

if __name__ == "__main__":
    nota = float(input("Ingrese su nota: "))
    print("su nota es: " + calcular(nota))
