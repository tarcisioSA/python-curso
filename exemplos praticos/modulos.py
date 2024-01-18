import math
import itertools
from datetime import datetime, timedelta
import os

print('Função cosseno', math.cos(100))

print('Função log:', math.log(10))

print(list(itertools.combinations('ABCD',3)))

print(list(itertools.permutations(['a', 'b', 'c'], 2)))

print('Datetime atual: ', datetime.now())

print('Datetima após 7 dias: ', datetime.now() + timedelta(days=7))

print('Caminho completo: ', os.path.join(''))