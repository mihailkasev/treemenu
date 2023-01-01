# Древовидное меню
### Описание
- Данное django приложение позволяет развернуть на странице древовидное меню.
### Технологии
- django==2.2.16
### Запуск приложения
- Клонируйте репозиторий
```
git clone https://github.com/mihailkasev/treemenu.git
```
- Создайте и запустите виртуальное окружение
```
python -m venv venv
. venv/Scripts/activate
```
- Установите зависимости
```
pip install -r requirements.txt
```
- Установите и запустите миграции
```
python manage.py makemigrations
python manage.py migrate
```
- Создайте суперпользователя
```
python manage.py createsuperuser
```
- Запустите сервер
```
python manage.py runserver
```
- В админ-панели создайте меню и предметы, в index.html замените аргумент тега draw_menu на название Вашего меню
- Доступные адреса:
1) http://localhost/admin/ - администрирование;
2) http://localhost/menu/ - главная страница;
### Автор: 
[Михаил Касев](https://github.com/mihailkasev/)