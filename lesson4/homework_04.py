import re

adwentures_of_tom_sawer = '''
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.'''

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# for space in adwentures_of_tom_sawer:
#     print(space.replace("\n", " "))
adwentures_of_tom_sawer_1 = adwentures_of_tom_sawer.replace("\n", " ")
print(f'task 01:\n{adwentures_of_tom_sawer_1}')

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer_2 = adwentures_of_tom_sawer_1.replace("....", " ")
print(f'task 02:\n{adwentures_of_tom_sawer_2}')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer_3 = ' '.join(adwentures_of_tom_sawer_2.split())
print(f'task 03:\n{adwentures_of_tom_sawer_3}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count= adwentures_of_tom_sawer_3.count('h')
print(f'task 04:\n{h_count}')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
x=re.findall("[A-Z]", adwentures_of_tom_sawer_3)
adwentures_of_tom_sawer_4 = len(x)
print(f'task 05:\n{adwentures_of_tom_sawer_4}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adwentures_of_tom_sawer_6=adwentures_of_tom_sawer_3.find("Tom",1)
print(f'task 06:\n{adwentures_of_tom_sawer_6}')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]', adwentures_of_tom_sawer_3)
print(f'task 07:\n{adwentures_of_tom_sawer_sentences}')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

sentences_4 = adwentures_of_tom_sawer_sentences [3]
print(f'task 08:\n{sentences_4.lower()}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
phrase_to_check = "By the time"
sentences_starting_with_phrase = [sentence.strip() for sentence in adwentures_of_tom_sawer_sentences if sentence.strip().startswith(phrase_to_check)]
if sentences_starting_with_phrase:
    print(f"task 08:\nРечення починаються з 'By the time'.")
else:
    print(f"task 08:\n Жодне речення не починається з 'By the time'.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer_sentences if sentence.strip()]
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(f'task 10:\nКількість слів в останньому реченні: {word_count}')
