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
    count = [0] * 26
    for sku in skus:
        sku = ord(sku)
        if(sku >= ord("A") and sku <= ord("Z")):
            count[sku - ord("A")] += 1
        else:
            return -1
    ret = 0
    ret += 40 * count[4]
    count[1] -= count[4] // 2
    if count[1] < 0:
        count[1] = 0

    ret += 200 * (count[0] // 5)
    ret += 130 * ((count[0] % 5) // 3)
    ret += 50 * ((count[0] % 5) % 3)

    ret += 45 * (count[1] // 2)
    ret += 30 * (count[1] % 2)

    ret += 20 * count[2]

    ret += 15 * count[3]

    ret += 20 * (count[5] // 3)
    ret += 10 * (count[5] % 3)
    return ret
