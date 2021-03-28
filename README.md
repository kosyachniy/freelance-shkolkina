# API для подбора городов
## Документация
[https://shkolkina.kosyachniy.com:9444/docs](https://shkolkina.kosyachniy.com:9444/docs)

## Запуск с Docker
### Local
```
cd docker/
docker-compose up --build
```

### Production
```
cd docker/
chmod 777 cert.sh
./cert.sh
docker-compose -f docker-compose.prod.yml up --build
```

## Запуск без Docker
1. Настраиваем виртуальное окружение
```
pip install -r requirements.txt
```

2. Точка входа: ` run.sh `