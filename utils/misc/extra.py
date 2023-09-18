# 13 599 000

def format_price(price):
    price = str(price)[::-1]
    s = ""
    index = 0
    for _ in range(len(price) // 3 + 1):
        try:
            s += price[index:index+3] + " "
        except IndexError:
            s += price[index:]
        index += 3
    return s[::-1].strip()
