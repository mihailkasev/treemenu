# Древовидное меню
### Описание
- Данное django приложение позволяет развернуть на странице древовидное меню.
### Технологии
- django==4.1.4
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
- Перейдите в папку управления проектом и запустите миграции
```
cd menu
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
1) http://127.0.0.1:8000/admin/ - администрирование;
2) http://127.0.0.1:8000/menu/ - главная страница;
### Автор: 
[Михаил Касев](https://github.com/mihailkasev/)
