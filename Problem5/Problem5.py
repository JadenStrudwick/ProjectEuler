def gcd (a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(args):
    if (len(args) == 2 ):
        return lcm(args[0], args[1])
    
    else:
        arg0 = args[0]
        args.pop(0)
        return lcm(arg0, lcmm(args))

zero_to_twenty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(lcmm(zero_to_twenty))