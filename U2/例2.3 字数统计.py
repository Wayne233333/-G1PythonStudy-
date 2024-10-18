def main():
    s='''I am a teacher. You are a student
I am a teacher. You are a student
I am a teacher. You are a student
I am a teacher. You are a student I am a teacher. You are a student I am a teacher.'''

    print ('='*30)
    print ('统计信息'.center(26))
    print ('-'*30)
    
    item_width=25
  
    
    word=s.split()
    print ('%-*s%5d' % (item_width-2,'字数',len(word)))

    # 下面的循环可以用一句话实现 w_len=(sum(map(len,word)))
    
    w_len=0
    for w in word:
        w_len=w_len+len(w)

 
    print ('%-*s%5d' % (item_width-9,'字符数（包含空格）',len(s)))
    print ('%-*s%5d' % (item_width-10,'字符数（不包含空格）',w_len))

    L=s.count('\n')+1
    print ('%-*s%5d' % (item_width-2,'行数',L))
    
    print ('-'*30)
     
main()

# 下面的代码采用全英文信息输出，对照上面的内容，看看区别在哪里

def main1():
    s='''I am a teacher. You are a student
I am a teacher. You are a student
I am a teacher. You are a student
I am a teacher. You are a student I am a teacher. You are a student I am a teacher.'''

    print ('='*30)
    print ('Information'.center(30))
    print ('-'*30)
    
    item_width=25
  
    
    word=s.split()     # word为单词总数
    print ('%-*s%5d' % (item_width,'words',len(word)))
    
##    w_len=0
##    for w in word:       # 每个单词长度统计
##        w_len=w_len+len(w)

    # 还可以采用统计空格数的方法：
    w_len=len(s)-s.count(' ')      # 检查这个方法跟上面方法为什么有误差，问题在哪里？(多了三个看不到的换行符）

 
    print ('%-*s%5d' % (item_width,'words(include space)',len(s)))
    print ('%-*s%5d' % (item_width,'words(no space)',w_len))

    L=s.count('\n')+1
    print ('%-*s %5d' % (item_width,'lines',L)) # 检查这里的输出格式为什么有误，可以对照上面内容（字符串里面多了一个空格）
    
    print ('-'*30)
     
main1()
