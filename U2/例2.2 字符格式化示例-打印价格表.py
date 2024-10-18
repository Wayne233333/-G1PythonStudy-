# 使用给定的宽度打印格式化后的价格列表

def main():
    w=int(input('请输入总的给定宽度：'))
    p_w=int(input('请输入价格占的总字符宽度：'))
    item_w=w-p_w    # 商品名称占的字符宽度=总宽度-价格宽度

# 用下面三句话没问题，但是用一行输出时'\n'会缩进一个字符位
# 因为打印内容之间分割逗号表示两个内容用空格隔开，所以多了一个空格

    print ('='*w)
    print (' '*((w-10)//2),'商品价格表',sep='')
    #print ('商品价格表'.center(w-5,'*'))   # 这里减5是因为中文字符占了一倍打印位置，所以减去五个字符位
    print ('='*w)
    
# 用'\n'换行后会缩进？为什么，用sep=''可以解决

#    print ('='*w,"\n",' '*((w-10)//2),'商品价格表','\n','='*w,sep='')

# 两个内容打一行，格式化可以并列使用，第一个加负号用于左对齐，第二个右对齐
# p_w减1的原因就是两个内容打印之间有一个空格，这里用了格式化输出，就不能用sep了

    #print ('%-*s %*s' % (item_w,'Item',p_w-1,'Price'))  # 注意这里必须用*s指定长度，不能用变量
    print('Item',' '*(w-4-5),'Price',sep='')
    print ('-'*w)
    print ('%-*s%*.2f'% (item_w,'Apple',p_w,0.4))
    print ('%-*s%*.2f'% (item_w,'Banana',p_w,0.59))
    print ('%-*s%*.2f'% (item_w,'Water Melon',p_w,1.99))
    print ('%-*s%*.2f'% (item_w,'Prunes(4 1bs.)',p_w,12))
    print ('='*w)
    
main()
    

# 更理想的格式如下：

def main1():
    w=int(input('请输入总的给定宽度：'))
    p_w=int(input('请输入价格占的总字符宽度：'))
    item_w=w-p_w    # 商品名称占的字符宽度=总宽度-价格宽度
    
    header_format='%-*s %*s'  # 这个字符串里面多了一个空格，所以下面p_w要减1
    item_format='%-*s %*.2f'
    
    print ('='*w,"\n",' '*((w-10)//2),'商品价格表','\n','='*w,sep='')

# 两个内容打一行，格式化可以并列使用，第一个加负号用于左对齐，第二个右对齐
# p_w减1的原因就是两个内容打印之间有一个空格，这里用了格式化输出，就不能用sep了

    print (header_format % (item_w,'Item',p_w-1,'Price'))

    print ('-'*w)
    print (item_format % (item_w,'Apple',p_w-1,0.4))
    print (item_format % (item_w,'Banana',p_w-1,0.59))
    print (item_format % (item_w,'Water Melon',p_w-1,1.99))
    print (item_format % (item_w,'Prunes(4 1bs.)',p_w-1,12))
    print ('='*w)
    
main1()
    
