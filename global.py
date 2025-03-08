string = '''Je suis étudiant à l'USTHB, je me gare à l'USTHB , j'habite près de l'USTHB et je 
connais l'USTHB depuis 2 ans'''
def replace(text , target  , replacement , count = -1):
    oldCount = count
    if count == 0:
        print(text)
        return
    words = text.split(' ')
    for i , word in enumerate(words):
        if len(word) < len(target):
            continue
        elif len(word) > len(target):
            for j , char in enumerate(word):
                if char == target[0] :
                    if word[j:j + len(target)] == target :
                        if count == 0:
                            break
                        words[i] = word[:j] + replacement + word[j+len(target):]
                        count -= 1
                else : continue
        elif word == target :
            if count == 0:
                break
            words[i] = replacement
            count -= 1
    print(' '.join(words))
    if count > 0:
        print(f'we found only {oldCount - count} {target} are you sure you didn\'t miss the count ??');

replace(string, 'USTHB' , '#' , 6)



def replaceOnlyTheOccurrence(text , target  , replacement , occurrence = 0):
    if occurrence < 0 or occurrence > 4:
        print('Invalid occurrence number. It should be between 0 and 4.')
        return
    count = 0
    if occurrence == 0:
        print(text)
        return
    words = text.split(' ')
    for i , word in enumerate(words):
        if len(word) < len(target):
            continue
        elif len(word) > len(target):
            for j , char in enumerate(word):
                if char == target[0] :
                    if word[j:j + len(target)] == target :
                        count = count + 1
                        if count == occurrence:
                            words[i] = word[:j] + replacement + word[j+len(target):]
                            break
                else : continue
        elif word == target :
            count+=1
            if count == occurrence:
                words[i] = replacement
                break
    print(' '.join(words))

replaceOnlyTheOccurrence(string, 'USTHB' , '#')
