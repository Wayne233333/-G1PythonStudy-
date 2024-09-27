
#a = int(input())
a = 3750
print("转换前的秒数为", a)

print(f"{a}秒共用时", end = "")
if a >= 86400:
    print(f"{a//86400}天", end = "")
if a >= 3600:
    print(f"{a%86400//3600}小时", end = "")
if a >= 60:
    print(f"{a%3600//60}分钟", end = "")
print(f"{a%60}秒")