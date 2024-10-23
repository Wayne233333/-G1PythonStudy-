
def f(filename):
    try:
        with open(filename, 'r') as file:
            for l in file:
                p = l.split(',')
                
                scores = list(map(float, p[1:]))
                average_score = sum(scores) / len(scores)
                
                print(f'student id: {p[0]}, average score: {average_score:.2f}')
    
    except FileNotFoundError:
        print(f'cannot open file {filename} or file does not exist.')
    except Exception as e:
        print(f'error: {e}')

f('scores.txt')
