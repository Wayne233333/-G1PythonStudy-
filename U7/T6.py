
def cal(exp):
    exp = exp.strip()
    if '+' in exp:
        nums = exp.split('+')
        ans = float(nums[0]) + float(nums[1])
        return f"{exp}={ans:.2f}"
    elif '-' in exp:
        nums = exp.split('-')
        ans = float(nums[0]) - float(nums[1])
        return f"{exp}={ans:.2f}"
    else:
        return f"Invalid expression: {exp}"


results = []

try:
    with open('jisuan.txt', 'r') as file:
        for l in file:  results.append(cal(l))
except FileNotFoundError:
    print("cannot find file: jisuan.txt")

with open('jieguo.txt', 'w') as file:
    for ans in results:
        file.write(f'{ans}\n')

print("done!")

