def contar_formas_escaleraNo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def mostrar_resultado(n):
    total = contar_formas_escaleraNo(n)
    print("------------------------------------------------")
    print(f"Escalones: {n}")
    print(f"Total de formas posibles: {total}")
    print("------------------------------------------------")


print("Cálculo de formas de subir una escalera con pasos de 1, 2 y 3.")
print("Ingresa un número entero mayor o igual a 0.\n")

entrada = input("Número de escalones: ")

if entrada.isdigit():
    escalones = int(entrada)
    mostrar_resultado(escalones)
else:
    print("Entrada inválida. Debes ingresar un número entero.")