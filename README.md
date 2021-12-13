## Документация по проекту

Типовые команды для запуска контейнера с backend-сервером:

1. Создание образа из Dockerfile:

```bash
docker build -t stocks_products .
```

2. Создание и запуск контейнера:

```bash
docker run -d -p 8000:8000 --name my_stocks_products stocks_products
```

3. Запуск сервера разработки:

```bash
http://127.0.0.1:8000/api/v1/
```
