def lru(num_pages, sequence):
    memory = [-1] * num_pages  
    usage_order = []  
    hit = 0  
    miss = 0  

    for page in sequence:
        print(f"page: {page}")  

        if page in memory:
            hit += 1  
            
            usage_order.remove(page) 
            usage_order.append(page) #Atualiza a lista de uso

            for page_in_memory in memory:
                if page_in_memory == page:
                    print(f"[{page_in_memory}] <- (hit)")
                else:
                    print(f"[{page_in_memory}]")

        else:
            miss += 1

            if -1 not in memory:  
                least_used_page = usage_order.pop(0)  
                index_to_replace = memory.index(least_used_page)
                memory[index_to_replace] = page
            else:
                index_to_replace = memory.index(-1)
                memory[index_to_replace] = page

            usage_order.append(page)

            for page_in_memory in memory:
                if page_in_memory == page:
                    print(f"[{page_in_memory}] <- (miss)")
                else:
                    print(f"[{page_in_memory}]")

        print()  

    total = len(sequence)
    print(f"Hit rate : ({hit}/{total})")
    print(f"Miss rate : ({miss}/{total})")

