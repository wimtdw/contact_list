# Используем официальный образ Python
FROM python:3.9-slim
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файлы зависимостей в контейнер
COPY requirements.txt .
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Копируем весь проект в контейнер
COPY . .
# Открываем порты
EXPOSE 8000
# Команда для запуска приложения
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]