# Calculadora de Partidas Rankeadas

Este projeto é parte do desafio da DIO para criar uma calculadora de partidas rankeadas.

## Objetivo

Criar uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
calcula o saldo de Rankeadas (vitórias - derrotas) e determina o nível baseando-se no saldo.

## Níveis

- **Ferro**: Saldo < 10
- **Bronze**: Saldo entre 11 e 20
- **Prata**: Saldo entre 21 e 50
- **Ouro**: Saldo entre 51 e 80
- **Diamante**: Saldo entre 81 e 90
- **Lendário**: Saldo entre 91 e 100
- **Imortal**: Saldo >= 101

## Como Executar

Certifique-se de ter o Python instalado.

### Modo Gráfico (GUI)

Execute o comando sem parâmetros para abrir a interface gráfica:

```bash
python3 main.py
```

### Modo Linha de Comando (CLI)

Para executar no terminal, utilize a flag `--cli` ou `-c`:

```bash
python3 main.py --cli
```
ou
```bash
python3 main.py -c
```

