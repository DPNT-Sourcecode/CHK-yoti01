"""
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+"""

prices = [50, 30, 20, 15, 40, 10, 20, 10, 35, 60, 80, 90, 15, 40, 10, 50, 30, 50, 30, 20, 40, 50, 20, 90, 10, 50]

def get_c(char):
    return count[ord(char) - ord("A")]

def set_c(char, new_c):
    count[ord(char) - ord("A")] = new_c

def sub_c(char, sub):
    count[ord(char) - ord("A")] -= sub

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    global count
    count = [0] * len(prices)

    for sku in skus:
        sku = ord(sku)
        if(sku >= ord("A") and sku <= ord("Z")):
            count[sku - ord("A")] += 1
        else:
            return -1

    ret = 0

# weird cross-product offers
    sub_c("B", get_c("E") // 2)
    if (count[1] < 0):
        count[1] = 0
    sub_c("M", get_c("N") // 3)
    if (count[12] < 0):
        count[12] = 0
    sub_c("Q", get_c("R") // 3)
    if (count[16] < 0):
        count[16] = 0

#normal multi-buys
    ret += 200 * (get_c("A") // 5)
    set_c("A", get_c("A") % 5)
    ret += 130 * (get_c("A") // 3)
    set_c("A", get_c("A") % 3)

    ret += 45 * (get_c("B") // 2)
    set_c("B", get_c("B") % 2)

    ret += 20 * (get_c("F") // 3)
    set_c("F", get_c("F") % 3)

    ret += 80 * (get_c("H") // 10)
    set_c("H", get_c("H") % 10)
    ret += 45 * (get_c("H") // 5)
    set_c("H", get_c("H") % 5)

    ret += 150 * (get_c("K") // 2)
    set_c("K", get_c("K") % 2)

    ret += 200 * (get_c("P") // 5)
    set_c("P", get_c("P") % 5)

    ret += 80 * (get_c("Q") // 3)
    set_c("Q", get_c("Q") % 3)

    ret += 120 * (get_c("U") // 4)
    set_c("U", get_c("U") % 4)

    ret += 130 * (get_c("V") // 3)
    set_c("V", get_c("V") % 3)
    ret += 90 * (get_c("V") // 2)
    set_c("V", get_c("V") % 2)

    for i in range(len(prices)):
        if count[i] > 0:
            ret += count[i] * prices[i]
    return ret

