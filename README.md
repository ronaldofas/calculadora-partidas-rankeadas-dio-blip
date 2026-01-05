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

## Estrutura do Projeto

O projeto foi refatorado para seguir uma arquitetura modular:

```
project_root/
├── assets/
│   └── medieval_shield.png        <-- Imagem do escudo
├── src/
│   ├── logic/
│   │   ├── __init__.py
│   │   └── calculator.py          <-- Lógica (RankedCalculator)
│   └── ui/
│       ├── __init__.py
│       ├── cli.py                 <-- Interface Linha de Comando (RankedCLI)
│       └── gui.py                 <-- Interface Gráfica (RankedGUI)
├── main.py                        <-- Ponto de entrada
├── .gitignore                     <-- Arquivos ignorados pelo Git
└── README.md                      <-- Documentação
```

- `assets/`: Contém os recursos visuais (imagens).
- `src/`: Contém o código-fonte organizado por responsabilidade.
  - `logic/`: Contém a lógica de negócios (`calculator.py`).
  - `ui/`: Contém as interfaces de usuário (`cli.py` e `gui.py`).
- `main.py`: Ponto de entrada da aplicação.


