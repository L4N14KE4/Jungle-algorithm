n = list(input())
exchange = []

for i in range(len(n)):
    if n[i] == n[i].lower():
        exchange += n[i].upper()
    else:
        exchange += n[i].lower()

result = "".join(j for j in exchange)
print(result)