n = int(input())
data = {}
for _ in range(n):
    name = input()
    score = float(input())
    data[name] = score
    for i in data:
        for j in data:
            if data[i] == data[j]:
                print(i)
                print(j)
                   
                