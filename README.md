Это Гайд - что бы код работал правильно
1. Скачивайте весь репозиторий
2. Переименуйте скачанную папку в "app"
3. Закинте папку "app" в другую папку
4. Скачивайте все что нужно
5. Далее вам стоит прописать вот эти команды:

   1. pip install fastapi uvicorn sqlalchemy passlib bcrypt==4.0.1 python-jose email-validator python-dotenv
   2. python -m app.init_db
   3. uvicorn app.main:app --reload
   
Приятного пользования!
(также что бы все работало правильно, рекомендуется удалить все папки с названием "__pycache__")
