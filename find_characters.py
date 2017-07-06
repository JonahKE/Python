word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for words in word_list:
    for characters in words:
        if characters == char:
            new_list.append(words)
print new_list