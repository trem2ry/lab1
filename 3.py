'''Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее в конце. Найти полученное число.'''
num=int(input())
print('{}'.format((num%100)*10+num//100))