#задание №1
'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
'''
try:
    from translate import Translator
except:
    print('Не установлен модуль "translate" для коректной работы.')
    exit(0)

def num_translate_adv(world):
    translator = Translator(to_lang='ru')
    translation = translator.translate(world)

    if translation == None:
        return 'None Перевод не найден.'
    else:
        result = translation.lower()
        return result.title() if world[0].upper() else result

print('задание 1*')
print(num_translate_adv(input('Введите числительное от 0 до 10 на английском языке: ')))
