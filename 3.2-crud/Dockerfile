FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r stocks_products/requirements.txt 

ENV SECRET_KEY = 'django-insecure-nw^y+m^wmxza1asgk+)!ua2qx9)g+#v=6%76-9i8i(6eqiw94j'

ENV DEBUG = True

RUN python stocks_products/manage.py migrate


CMD ["python", "stocks_products/manage.py", "runserver", "0.0.0.0:8000"]

