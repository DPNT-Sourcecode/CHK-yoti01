"""+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+"""

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    n_a = 0
    n_b = 0
    n_c = 0
    n_d = 0
    n_e = 0
    n_f = 0
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
        elif(sku == "F"):
            n_f += 1
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

    ret += 20 * (n_f // 3)
    ret += 10 * (n_f % 3)
    return ret


