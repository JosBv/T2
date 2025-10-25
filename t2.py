import random

def generar_palabra():
    return ''.join(chr(random.randint(97, 122)) for _ in range(4))

def tiene_vocal(palabra):
    for letra in palabra:
        if letra in 'aeiou':
            return True
    return False

def contar_con_vocales(matriz):
    if not matriz or not matriz[0]:
        return 0
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas == 1 and columnas == 1:
        return 1 if tiene_vocal(matriz[0][0]) else 0
    mitad_f = filas // 2
    mitad_c = columnas // 2
    sub1 = [fila[:mitad_c] for fila in matriz[:mitad_f]]
    sub2 = [fila[mitad_c:] for fila in matriz[:mitad_f]]
    sub3 = [fila[:mitad_c] for fila in matriz[mitad_f:]]
    sub4 = [fila[mitad_c:] for fila in matriz[mitad_f:]]
    return (contar_con_vocales(sub1) +
            contar_con_vocales(sub2) +
            contar_con_vocales(sub3) +
            contar_con_vocales(sub4))

def main():
    while True:
        print("\n=== MATRIZ DE PALABRAS ALEATORIAS ===")
        try:
            filas = int(input("Ingrese el número de filas (máx. 8): "))
            columnas = int(input("Ingrese el número de columnas (máx. 8): "))
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            continue
        if filas > 8 or columnas > 8 or filas <= 0 or columnas <= 0:
            print("\nDimensiones inválidas. La matriz no puede superar 8 x 8. Intente nuevamente.\n")
            continue
        matriz = [[generar_palabra() for _ in range(columnas)] for _ in range(filas)]
        print("\nMatriz generada:\n")
        for fila in matriz:
            print(' '.join(fila))
        total_vocales = contar_con_vocales(matriz)
        print(f"\nTotal de palabras que contienen al menos una vocal: {total_vocales}")
        opcion = input("\n¿Desea generar una nueva matriz? (s/n): ").strip().lower()
        if opcion != 's':
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main()