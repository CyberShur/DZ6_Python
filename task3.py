'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

with open('test1.txt', 'r') as data:
    text = data.read()

def encode(ss):
    code = ''
    prev = ''
    count = 1
    for char in ss:
        if char != prev:
            if prev:
                code += str(count) + prev
            count = 1
            prev = char
        else:
            count += 1
    return code

            
code = encode(text)
print(code)

with open('test2.txt', 'r') as data:
    my_text2 = data.read()

def decoding(a:str):
    count = ''
    decode = ''
    for char in a:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count)
            count = ''
    return decode

decode = decoding(my_text2)
print(decode)