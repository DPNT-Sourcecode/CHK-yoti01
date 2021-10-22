

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    n_a = 0
    n_b = 0
    n_c = 0
    n_d = 0
    n_e = 0
    for sku in skus:
        if(sku == "A"):
            n_a += 1
        elif(sku == "B"):
            n_b += 1
        elif(sku == "C"):
            n_c += 1
        elif(sku == "D"):
            n_d += 1
        elif(sku == "E"):
            n_e += 1
        else:
            return -1
    ret = 0
    ret += 40 * n_e
    n_b -= n_e // 2
    if n_b < 0:
        n_b = 0

    ret += 200 * (n_a // 5)
    ret += 130 * ((n_a % 5) // 3)
    ret += 50 * ((n_a % 5) % 3)
    ret += 45 * (n_b // 2)
    ret += 30 * (n_b % 2)
    ret += 20 * n_c
    ret += 15 * n_d
    return ret
