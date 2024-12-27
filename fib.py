def fibo_dp_mem(n):
    mem = [0, 1]
    for i in range(2, n + 1):
        mem[i % 2] = mem[0] + mem[1]
    return mem[n % 2]

print(fibo_dp_mem(5))

def recursive(n):
    if n<=1:
        return n
    return recursive(n-1) + recursive(n-2)

print(recursive(5))