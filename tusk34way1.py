# Задача 34:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке


# Ввод:  
# пара-ра-рам рам-пам-папам па-ра-па-дам 

# Вывод:
# Парам пам-пам
# Способ 1: обычными циклами
vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
song = input('введите текст песни винипуха: ').lower().split()
sum = 0 
print(song)

for i in song[0]:
    if i in vowels:
        sum+=1       

sum_i =0
for x in song[1]:
    if x in vowels:
        sum_i += 1      
if sum_i == sum:
    print('Парарам-пам-пам')
else:
    print('Пам-парам')

            