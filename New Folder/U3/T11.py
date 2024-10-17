
a = int(input())

if a >= 86400:
    print(f"{a//86400}天", end = "")
if a >= 3600:
    print(f"{a%86400//3600}小时", end = "")
if a >= 60:
    print(f"{a%3600//60}分钟", end = "")
print(f"{a%60}秒")