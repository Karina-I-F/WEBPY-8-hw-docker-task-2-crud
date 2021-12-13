FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /stocks_products

COPY requirements.txt .
RUN pip install -r ./requirements.txt

EXPOSE 8000

COPY manage.py .
COPY ./stocks_products ./stocks_products
COPY ./logistic ./logistic

RUN python ./manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]