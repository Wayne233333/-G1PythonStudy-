
def cal(prices, data):
    tot_cost = 0.0
    items = data.split(',')
    
    for item in items:
        weight_str, fruit = item.split('g')
        weight = float(weight_str)
        if fruit not in prices:
            print(f"无该水果的价格: {fruit}")
            continue

        price = prices[fruit]
        tot = weight / 500 * price
        
        if 5000 > weight >= 2500:
            tot *= 0.99
        elif weight >= 5000:
            tot *= 0.95
        
        tot_cost += tot
    
    return tot_cost

filename = 'price.txt'
prices = {}

try:
    with open('price.txt', 'r', encoding='utf-8') as file:
        for l in file:
            fruit, price = l.strip().split()
            prices[fruit] = float(price)
except FileNotFoundError:
    print(f"cannot find file: {filename}")

input_data = input()
tot_cost = cal(prices, input_data)

print(f"总费用: {tot_cost:.1f}元")
