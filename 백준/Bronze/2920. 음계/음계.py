scales = list(map(int, input().split()))

if scales == sorted(scales):
    print("ascending")
elif scales == sorted(scales, reverse=True):
    print("descending")
else:
    print("mixed")