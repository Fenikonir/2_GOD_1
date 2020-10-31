a = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
     "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
     "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
     "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
     "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
     "б": "b", "ю": "ju", "ё": "jo"}

alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
            'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
            'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
            'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
itog = []
result = str()
with open("cyrillic.txt", "rt", encoding="utf-8") as f:
    f1 = f.read().split("\n")
    for j in f1:
        for i in range(len(j)):
            if j[i] in alphabet:
                if j[i].islower():
                    simb = a[j[i]]
                else:
                    simb = a[j[i].lower()].capitalize()
            else:
                simb = j[i]
            result = result + simb
        itog.append(result)
        result = str()

with open("transliteration.txt", "a", encoding="utf-8") as f:
    for i in itog:
        f.write(i + '\n')