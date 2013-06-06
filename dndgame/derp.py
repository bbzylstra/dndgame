text = raw_input('Enter Text!\n')
leng = len(text)
counter = 0
text2 = list(text)
for leng in text2:
    if text2[counter] == 'a':
        text2[counter] = '4'
    elif text2[counter] == 'b':
        text2[counter] = '8'
    elif text2[counter] == 'e':
        text2[counter] = '3'
    elif text2[counter] == 'i':
        text2[counter] = '1'
    elif text2[counter] == 'o':
        text2[counter] = '0'
    elif text2[counter] == 'g':
        text2[counter] = '6'
    elif text2[counter] == 't':
        text2[counter] = '7'
    elif text2[counter] == 's':
        text2[counter] = '5'
    elif text2[counter] == 'l':
        text2[counter] = '1'
    elif text2[counter] == 'A':
        text2[counter] = '4'
    elif text2[counter] == 'B':
        text2[counter] = '8'
    elif text2[counter] == 'E':
        text2[counter] = '3'
    elif text2[counter] == 'I':
        text2[counter] = '1'
    elif text2[counter] == 'O':
        text2[counter] = '0'
    elif text2[counter] == 'G':
        text2[counter] = '6'
    elif text2[counter] == 'T':
        text2[counter] = '7'
    elif text2[counter] == 'S':
        text2[counter] = '5'
    elif text2[counter] == 'L':
        text2[counter] = '1'
    elif text2[counter] == 'x':
        text2[counter] = '%'
    elif text2[counter] == 'X':
        text2[counter] = '%'
    elif text2[counter] == 'H':
        text2[counter] = '#'
    elif text2[counter] == 'h':
        text2[counter] = '#'
    counter = counter + 1
text3 = "".join(text2)
print text3
