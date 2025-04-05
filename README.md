# Анализатор TF-IDF на Django

## 📌 Описание проекта

Это веб-приложение для анализа текстовых файлов с расчетом статистики TF-IDF. Система позволяет:
- Загружать текстовые файлы (.txt) через веб-интерфейс
- Автоматически вычислять Term Frequency (TF) для каждого слова
- Рассчитывать Inverse Document Frequency (IDF) для каждого термина
- Отображать топ-50 слов, отсортированных по IDF (наиболее уникальные сначала)
- Очищать текст от пунктуации и приводить к нижнему регистру

## 🛠️ Стек технологий

- **Язык:** Python 3.8+
- **Фреймворк:** Django 3+
- **База данных:** PostgreSQL 10+

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone git@github.com:holdlemon/text_analyzer.git
cd text_analyzer
```

### 2. Создание и активация виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных

Перед запуском необходимо создать базу данных в PostgreSQL и обновить настройки в `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'POSTGRES_DB': 'your_db_name',
        'POSTGRES_USER': 'your_db_user',
        'POSTGRES_PASSWORD': 'your_db_password',
        'POSTGRES_HOST': 'localhost',
        'POSTGRES_PORT': '5432',
    }
}
```

### 5. Выполнение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Запуск сервера

```bash
python manage.py runserver
```
Приложение доступно по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📜 Лицензия

Этот проект распространяется под MIT License.

---