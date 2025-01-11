def magic(x):
    if x==1:
        return 1
    return x*magic(x-1)

print(magic(3))
