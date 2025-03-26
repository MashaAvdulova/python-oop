import json

# Дан файл со стихотворением poem.txt.
# Необходимо провести анализ текста и результат сохранить в файл analyz.txt, analyz.json

class TextAnalizator:
    def __init__(self):
        self.text = None
        self.result = {}

    def read_text_from_file(self, path):
        with open(path, 'r', encoding = 'utf-8') as file:
            self.text = file.read()

# 1. Сколько всего символов в тексте
    def count_of_chars(self):
        result = len(self.text)
        self.result['1. Всего символов в тексте'] = result
        print(self.result)

# 2. Сколько букв в тексте (без пробелов и знаков препинания (,.!?))
    def count_of_letters(self):
        count_of_znak = 0
        for i in self.text:
            if (i == ',') or (i == '.') or (i == '!') or (i == '?') or (i == '-') or (i == ':') or (i == ';') or (i == ' '):
                count_of_znak += 1
        result = len(self.text) - count_of_znak
        self.result['2. Всего букв в тексте'] = result
        print(self.result)

# 3. Сколько всего строк в тексте
    def count_of_str(self):
        result = len(self.text.split('\n'))
        self.result['3. Всего строк в тексте'] = result
        print(self.result)

# 4. Сколько непустых строк в тексте
    def count_of_str_empty(self):
        count_of_str_empty = 0
        for i in self.text.split('\n'):
            if i == '':
                count_of_str_empty += 1
        result = len(self.text.split('\n')) - count_of_str_empty
        self.result['4. Непустых строк в тексте'] = result
        print(self.result)

# 5. Сколько всего слов в тексте
    def count_of_words(self):
        symbols_of_poem = self.text.split()
        words_of_poem = []
        for i in symbols_of_poem:
            word = i.strip(',.?!;:-')
            words_of_poem.append(word)
        result =  len(words_of_poem)
        self.result['5. Всего слов в тексте'] = result
        print(self.result)

# 6*. Сколько слов в каждой строке
    def count_of_words_in_str(self):
        results = {}
        for i in range(len(self.text.split('\n'))):
            symbols_of_str_in_poem = self.text.split('\n')[i].split()
            words_of_str_in_poem = []
            for j in symbols_of_str_in_poem:
                word = j.strip(',.?!;:-')
                words_of_str_in_poem.append(word)
            result = len(words_of_str_in_poem)
            results[f'{i+1} строка'] = result
        self.result['6. Анализ слов по строкам:'] = results
        print(self.result)

# 7*. Сколько символов в каждой строке
    def count_of_symbols_in_str(self):
        results = {}
        for i in range(len(self.text.split('\n'))):
            result = len(self.text.split('\n')[i])
            results[f'{i+1} строка'] = result
        self.result['7. Анализ символов по строкам:'] = results
        print(self.result)

# 8. Найти повторяющиеся слова в тексте с указанием количества
    def repeat_words(self):
        results = {}
        words_of_poem = []
        for i in self.text.lower().split():
            word = i.strip(',.?!;:-')
            words_of_poem.append(word)
        words_of_poem_set = set(words_of_poem)
        for i in words_of_poem_set:
            count_of_repeat_words = words_of_poem.count(i)
            if count_of_repeat_words > 1:
                result = count_of_repeat_words
                results[f'{i}'] = result
        self.result['8. Повторяющиеся слова:'] = results
        print(self.result)

# 9*. Провести частотный анализ букв (частота появления каждой буквы в тексте)
# 10. Найти все посторонние символы (пробелы и знаки препинания) - какие и сколько
    def count_of_letters_and_symbols(self):
        letters = list(self.text.lower())
        letters_uniq = list(set(letters))
        letters_uniq.sort()
        results_letters = {}
        results_symbols = {}
        for i in letters_uniq:
            count = letters.count(i)
            if i.isalpha():
                results_letters[f'{i}'] = count
            else:
                results_symbols[f'{i}'] = count
        self.result['9. Частотный анализ текста:'] = results_letters
        self.result['10. Прочие символы:'] = results_symbols
        print(self.result)

# запись результата в текстовый файл
    def write_result_in_txt(self):
        with open('250326_TextAnalizator.txt', 'w', encoding='utf-8') as file:
            text = str(self.result)
            file.write(text)

# запись результата в json файл
    def write_result_in_json(self):
        with open('250326_TextAnalizator.json', 'w', encoding='utf-8') as file:
            json.dump(self.result, file, indent=2, ensure_ascii=False)


t_analizator = TextAnalizator()
t_analizator.read_text_from_file(path='250326_poem.txt')
t_analizator.count_of_chars()
t_analizator.count_of_letters()
t_analizator.count_of_str()
t_analizator.count_of_str_empty()
t_analizator.count_of_words()
t_analizator.count_of_words_in_str()
t_analizator.count_of_symbols_in_str()
t_analizator.repeat_words()
t_analizator.count_of_letters_and_symbols()
t_analizator.write_result_in_json()
t_analizator.write_result_in_txt()