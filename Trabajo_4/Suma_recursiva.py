def suma_digitos(N):
    # Caso base: si el número es de un solo dígito
    if N < 10:
        return N
    else:
        # Caso recursivo: último dígito + suma de los dígitos restantes
        return (N % 10) + suma_digitos(N // 10)     #(N%10) obtiene el último dígito, (N//10) elimina el último dígito

# Ejemplo de uso
numero = int(input("Digite un número entero: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")