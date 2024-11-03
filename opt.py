def opt(num_pages, sequence):
    memory = [-1] * num_pages
    hit = 0
    miss = 0

    for i, page in enumerate(sequence):
        print(f"page: {page}")  

        if page in memory:
            hit += 1
            for page_in_memory in memory:
                if page_in_memory == page:
                    print(f"[{page_in_memory}] <- (hit)")
                else:
                    print(f"[{page_in_memory}]")
        else:
            miss += 1
            if -1 in memory:
                empty_index = memory.index(-1)
                memory[empty_index] = page
            else:
                future_use = []
                for page_in_memory in memory:
                    if page_in_memory in sequence[i + 1:]: #Se a pagina estiver na sequencia, a partir de onde está a itereação de agora
                        next_use = sequence[i + 1:].index(page_in_memory)
                    else:
                        next_use = len(sequence) - i + 1 
                    future_use.append(next_use)

                # Encontra a página com maior distância de uso futuro e substitui
                page_to_replace_index = future_use.index(max(future_use))
                replaced_page = memory[page_to_replace_index]
                memory[page_to_replace_index] = page

            for page_in_memory in memory:
                if page_in_memory == page:
                    print(f"[{page_in_memory}] <- (miss)")
                else:
                    print(f"[{page_in_memory}]")
                    
        print()  


    print(f"Hit rate  : ({hit}/{len(sequence)})")
    print(f"Miss rate : ({miss}/{len(sequence)})")