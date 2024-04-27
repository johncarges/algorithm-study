

fibonacci = {}

dynamic = False

def fib(n):
    if n in fibonacci:
        return fibonacci[n]
    if n in [0,1]:
        return 1
    else:
        ans = fib(n-1) + fib(n-2)
        if dynamic: 
            fibonacci[n] = ans
        return ans
    


print(fib(30))

dynamic = True
print(fib(30))