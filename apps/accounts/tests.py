from django.test import TestCase

with open('file.txt', 'w', encoding='utf-8') as file:
    file.write('Привет мир!')

try:
    file = open('file.txt', 'x', encoding='utf-8')
except Exception as err:
    print(type(err).__name__)