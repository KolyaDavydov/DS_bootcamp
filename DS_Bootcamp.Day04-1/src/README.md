# ex00
Проверяет скорость работы двух методов с различным типом иттерирования по циклу

запустить скрипт:
```
python3 benchmark.py
```
после запуска необходимо подождать около 2 минут (или меньше, в зависимости от мощности процессора) после чего в терминале выйдет сообщение кто из методов быстрее и насколько

В целом иттераций должно быть 90,000,000 но я оставил только 9 миллионов что б было быстрее

мой вывод (wsl ubuntu 20.04):
```
it is better to use a list comprehension
25.696241851001105 vs 28.36989400999846
```

# ex01 
Проверяет скорость работы трех методов с различным типом иттерирования по циклу
[ссылка](https://habr.com/ru/articles/479252/)

запустить скрипт:
```
python3 benchmark.py
```
после запуска необходимо подождать около 2 минут (или меньше, в зависимости от мощности процессора) после чего в терминале выйдет сообщение кто из методов быстрее и насколько

мой вывод (wsl ubuntu 20.04):
```
it is better to use a list comprehension
24.83906698100145 vs 28.000041741999667 vs 35.23907641900041
```
по сути `map` должен быть быстрее, но что то пошло не так...)

# ex02
скрипты для проверки:
```
python3 benchmark.py loop 100000
```
```
python3 benchmark.py list_comprehension 100000
```
```
python3 benchmark.py map 100000
```
```
python3 benchmark.py filter 100000
```

# ex03
скрипты для проверки:
```
python3 benchmark.py loop 1000000 5
```
```
python3 benchmark.py reduce 1000000 5
```

# ex04
запустить скрипт:
```
python3 benchmark.py
```
мой вывод (wsl ubuntu 20.04):
```
my function: 11.701573563001148
Counter: 5.313589410998247
my top: 12.139115068999672
Counter's top: 5.373926946998836
```

# ex05
Был скачан [файл](http://files.grouplens.org/datasets/movielens/ml-25m.zip) и распакован в папку `ex05`

Без итерратора:

```
python3 ordinary.py ratings.csv
```
```
Peak memory usage= 1.3251228332519531 GB
User Mode Time + System Mode Time = 2.4s
```

С итератором:
```
python3 generator.py ratings.csv
```
```
Peak memory usage= 0.0110931396484375 GB
User Mode Time + System Mode Time = 3.07s
```

