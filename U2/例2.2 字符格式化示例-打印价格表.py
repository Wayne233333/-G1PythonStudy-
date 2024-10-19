
def demo():

    w = int(input('请输入总的给定宽度:'))
    print(f'{"=" * w}\n{" "*((w - 10) // 2)}商品价格表{" "*((w - 10) // 2)}\n{"=" * w}')

# 两个内容打一行，格式化可以并列使用，第一个加负号用于左对齐，第二个右对齐
# p_w减1的原因就是两个内容打印之间有一个空格，这里用了格式化输出，就不能用sep了

    print(f'Item{" " * (w - 9)}Price')
    print('-' * w)

    print(f'Apple{" " * (w - 9)}{"%.2f" % 0.4}')
    print(f'Banana{" " * (w - 10)}{"%.2f" % 0.59}')
    print(f'Water Melon{" " * (w - 15)}{"%.2f" % 1.99}')
    print(f'Prunes(4 1bs.){" " * (w - 19)}{"%.2f" % 12}')

    print ('=' * w)

if __name__ == '__main__':

    demo()
    