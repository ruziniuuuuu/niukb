# # Brute Force
# def func():
#     n = int(input())
#     seqs = list(map(int, input().split()))

#     sources = list()
#     plus = 0
#     for seq in seqs:
#         if len(sources) == 0:
#             source = [seq]
#             sources.append(source)
#         else:
#             flag = 0
#             for i, source in enumerate(sources):
#                 if seq == 65536:
#                     sources.remove(i)
#                     plus += 1
#                 if source[-1] + 1 == seq:
#                     source.append(seq)
#                     flag = 1
#                     break
#             if flag == 0:
#                 source = [seq]
#                 sources.append(source)
    
#     print(len(sources) + plus)
        

# if __name__ == "__main__":
#     func()

def func():
    n = int(input())
    seqs = list(map(int, input().split()))
    
    sources = set()
    last_seq = {}
    
    for seq in seqs:
        if seq == 65536:
            sources.add(len(sources))
        else:
            found = False
            for source in list(sources):
                if last_seq.get(source, -1) + 1 == seq:
                    last_seq[source] = seq
                    found = True
                    break
            if not found:
                new_source = len(sources)
                sources.add(new_source)
                last_seq[new_source] = seq
    
    print(len(sources))

if __name__ == "__main__":
    func()