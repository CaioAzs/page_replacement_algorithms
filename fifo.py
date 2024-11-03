def fifo(num_pages, sequence):
    memory = [-1] * num_pages  
    position = 0  
    hit = 0  
    miss = 0  

    for page in sequence:
        print(f"page: {page}")

        if page in memory:
            hit += 1
            for element in memory:
                if element == page:
                    print(f"[{element}] <- (hit)")
                else:
                    print(f"[{element}]")

        else:
            # Se a página não estiver na memória, é um Miss
            miss += 1
            memory[position] = page  
            
            #===============IMPORTANTE==============#
            # Atualiza a posição de modo circular, vai para a próxima página SOMENTE quando é Miss
            position = (position + 1) % num_pages  

            for element in memory:
                if element == page:
                    print(f"[{element}] <- (miss)")
                else:
                    print(f"[{element}]")
        print()

    total = len(sequence)
    print(f"Hit rate : ({hit}/{total})")
    print(f"Miss rate : ({miss}/{total})")