def calcular_nivel(vitorias, derrotas):
    """
    Calcula o saldo de vitórias e determina o nível do jogador.
    Argumentos:
        vitorias (int): Quantidade de vitórias.
        derrotas (int): Quantidade de derrotas.
    Retorna:
        tuple: (saldo_vitorias, nivel)
    """
    saldo_vitorias = vitorias - derrotas
    
    if saldo_vitorias < 10:
        nivel = "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    else: # saldo_vitorias >= 101
        nivel = "Imortal"
        
    return saldo_vitorias, nivel

def main():
    print("--- Calculadora de Partidas Rankeadas ---")
    try:
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))
        
        saldo, nivel = calcular_nivel(vitorias, derrotas)
        
        print(f"O Herói tem de saldo de **{saldo}** está no nível de **{nivel}**")
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros para vitórias e derrotas.")

if __name__ == "__main__":
    main()
