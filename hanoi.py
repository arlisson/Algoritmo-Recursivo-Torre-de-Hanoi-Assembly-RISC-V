def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

if __name__=='__main__':
    # Exemplo de uso
    n = int(input("Digite o número de discos: "))
    torre_hanoi(n, "A", "C", "B")