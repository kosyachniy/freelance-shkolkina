# API для подбора городов
## Ссылки
[Telegram бот](https://t.me/shkolkina_bot)

[Список городов](https://docs.google.com/spreadsheets/d/1yUulEeriEhSdnLm2b7Nq1EeggaQII25K8-SoHSzyVsw/edit#gid=0)

BotMather: [настройки](https://app.botmother.com/bot/604ef45dfb4c134da43bf9e3/settings/), [конструктуор](https://app.botmother.com/bot/604ef45dfb4c134da43bf9e3/constructor/)

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