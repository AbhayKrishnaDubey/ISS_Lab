from math import comb
                                
def AKS(n):
    if (n ^ 1 == n + 1):        # check if it's even
        if n == 2:
            return True         
        return False
    for i in range(3,n//2):
        if comb(n,i)%n != 0:    # check if any coefficient isn't divisible by n
            return False
    return True
def expand_x_1(p):
    ex = [1]
    for i in range(p):
        ex.append(ex[-1] * -(p-i) / (i+1))
    return ex[::-1]
def aks_test(p):
    if p < 2: return False
    ex = expand_x_1(p)
    ex[0] += 1
    return not any(mult % p for mult in ex[0:-1])
    print('# p: (x-1)^p for small p')
    for p in range(12):
        print('%3i: %s' % (p, ' '.join('%+i%s' % (e, ('x^%i' % n) if n else '')
                                   for n,e in enumerate(expand_x_1(p)))))
print('\n# small primes using the aks test')
print([p for p in range(101) if aks_test(p)])
