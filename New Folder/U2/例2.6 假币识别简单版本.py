
from collections import Counter
    
a = []
a = input().split()

count = Counter(a)
# print(count)
true_num, true_count = count.most_common(1)[0]

print(f"真币: {true_num}, 出现次数: {true_count}")

fake_num = []
fake_index = []

for index, num in enumerate(a):
    if num != true_num:
        fake_num.append(num)
        fake_index.append(index)

print("假币及其位置：")
for index in fake_index:
    print(f"假币: {a[index]}, 位置: {index}")
