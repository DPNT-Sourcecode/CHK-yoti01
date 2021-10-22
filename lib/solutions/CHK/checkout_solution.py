

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    n_a = 0
    n_b = 0
    n_c = 0
    n_d = 0
    for sku in skus:
        if(sku == "A"):
            n_a += 1
        elif(sku == "B"):
            n_b += 1
        elif(sku == "C"):
            n_c += 1
        elif(sku == "D"):
            n_d += 1
    ret = 0
    ret += 130 * (n_a // 3)
    ret += 50 * (n_a % 3)
    ret += 45 * (n_b // 2)
    ret += 30 * (n_b % 2)
    ret += 20 * n_c
    ret += 15 * n_d
