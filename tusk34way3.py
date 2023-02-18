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

# Способ 3: через лямбда функцию


vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я'] # список шласных букв алфавита
song = input('введите текст песни винипуха: ').lower().split() # ввод песни винипуха
print(song) # печать песни винипуха
ref_lambda = lambda x: sum(1 for i in x if i in vowels)
sum_vowels_first_phrase1 = ref_lambda(song[0])
print(sum_vowels_first_phrase1)
if (ref_lambda[i] == sum_vowels_first_phrase1 for i in vowels):
    print('Парам-пам-пам')
else:
    print('Пам-парам')