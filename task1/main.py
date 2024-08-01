def caching_fib():
    cache = {}
    def fib(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fib(n-1)+fib(n-2)
        return cache[n]
    return fib

fib = caching_fib()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610