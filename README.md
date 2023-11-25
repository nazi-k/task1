## Task Description
Створити Flask додаток. TodoList.

Сутність Board:
дату створення(timestamp)
дату модифікації(timestamp)
статус(string) - ARCHIVED/OPEN

Сутність - Task, має:
дату створення(timestamp)
дату модифікації(timestamp)
статус виконання(bool)
текст(string)
board - FK(Board)

Створити JSON API для:

1. Отримати список дошок.
2. Отримання списку tasks.
   1. Реалізувати можливість фільтруватись за статусом виконання
   2. Реалізувати можливість фільтруватись за дошкою
3. Створення нового Task
4. Отримання конкретного Task по ідентифікатору
5. Оновлення статусу виконання Task
6. Видалення Task

## Installation

### Repo setup
```
git clone https://github.com/nazi-k/task1.git
cd task1
pip3 install -r requirements.txt
```
### Run migrations
```
flask db upgrade
```
### Run development server
```
python3 run.py
```
### Run tests
```
pytest
```
