import argparse
import fifo
import lru
import opt

def main(pages, sequence, algorithm):
    if algorithm == "fifo":
        fifo.fifo(pages, sequence)
    elif algorithm == "lru":
        lru.lru(pages, sequence)
    elif algorithm == "opt":
        opt.opt(pages, sequence)
    else:
        raise ValueError("Algoritmo inválido. Escolha entre 'fifo', 'lru' ou 'opt'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pages", type=int, help="Número de páginas. Ex: '5'")
    parser.add_argument("sequence", type=str, help="Sequência de páginas. Ex: '2,1,3,4,6,2,1'")
    parser.add_argument("algorithm", type=str, help="'fifo', 'lru' ou 'opt'")
    
    try:
        args = parser.parse_args()
        pages = args.pages
        if pages <= 0:
            raise ValueError("Erro. Número de páginas deve ser > 0")

        try:
            sequence = list(map(int, args.sequence.split(',')))
        except ValueError:
            raise ValueError("A sequência deve conter apenas números inteiros separados por vírgulas.")

        algorithm = args.algorithm.lower()
        main(pages, sequence, algorithm) #Execução final

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")
