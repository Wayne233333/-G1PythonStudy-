def demo():
    s = '''I am a teacher. You are a student
I am a teacher. You are a student
I am a teacher. You are a student
I am a teacher. You are a student I am a teacher. You are a student I am a teacher.'''

    print('=' * 30)
    print('Information'.center(30))
    print('-' * 30)

    item_width = 25

    try:
        
        word = s.split()
        print('%-*s%5d' % (item_width, 'words', len(word)))

        total_chars = len(s)
        non_space_chars = total_chars - s.count(' ')
        
        print('%-*s%5d' % (item_width, 'words(include space)', total_chars))
        print('%-*s%5d' % (item_width, 'words(no space)', non_space_chars))

        line_count = s.count('\n') + 1
        print('%-*s%5d' % (item_width, 'lines', line_count))

    except Exception as e:
        print("Wrong!", str(e))
    
    print('-' * 30)

if __name__ == '__main__':

    demo()
