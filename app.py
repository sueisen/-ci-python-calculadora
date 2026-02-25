# app.py
# Mini aplicación de consola que usa calculator.py

from calculator import add, sub, mul, div

def main():
    print("=== Calculadora Simple ===")
    print("Operaciones: add, sub, mul, div")
    op = input("Elige operación: ").strip()
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if op == "add":
        result = add(a, b)
    elif op == "sub":
        result = sub(a, b)
    elif op == "mul":
        result = mul(a, b)
    elif op == "div":
        result = div(a, b)
    else:
        print("Operación no válida.")
        return

    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
