
---
# Page Replacement Algorithms - Operational Systems

Este projeto é uma simulação de algoritmos de substituição de páginas para sistemas de gerenciamento de memória em Sistemas Operacionais. Ele implementa três algoritmos: First-In-First-Out, Least Recently Used e Optimal Page Replacement. 

## Estrutura do Projeto

O projeto é composto por três arquivos principais, cada um implementando um algoritmo:

- `fifo.py`
- `lru.py`
- `opt.py`

O arquivo `main.py` recebe entradas do usuário e executa o algoritmo escolhido.

## Uso

Para executar o projeto, utilize o comando (os arquivos devem estar na mesma pasta):

```bash
python main.py <pages> <sequence> <algorithm>
```

### Argumentos

- `pages` (int): Quantidade de páginas disponíveis na memória (int > 0).
- `sequence` (str): Sequência de páginas, separadas por vírgulas (`7,0,1,2,0,3,0,4`).
- `algorithm` (str): Algoritmo a ser utilizado (`fifo`, `lru` ou `opt`).

### Exemplo

Executar o algoritmo FIFO com 3 páginas e uma sequência de referência de páginas:

   ```bash
   python main.py 3 "7,0,1,2,0,3,0,4" fifo
   ```


### Output

O programa tem como saída o Miss rate e o Hit rate das páginas, além de uma simulação visual no terminal:

![{56AF1116-2347-42C6-B202-A401E89175F4}](https://github.com/user-attachments/assets/70b12720-d9f6-4741-b962-f1a3b42aa7d6)


## Help

Para visualizar o help dos argumentos, use:

```bash
python main.py --help
```
