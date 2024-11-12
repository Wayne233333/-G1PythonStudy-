def demo():
    a = float(input('请输入商品总价:'))
    if a < 100:
        b = a
    elif a < 300:
        b = a*0.98
    elif a < 500:
        b = a*0.9
    else:
        b = a*0.88
    print('需要支付价格为%.2f元,优惠'% b, end = '')
    print('%.2f元'% (a-b))

demo()
