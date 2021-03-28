curl -w "\n%{time_total}\n" -X POST -d '{"city": "дедовские выселки"}' http://localhost:5000/ https://shkolkina.kosyachniy.com:9444/

curl -w "\n%{time_total}\n" -X POST -d '{"city": "Москва"}' http://localhost:5000/ https://shkolkina.kosyachniy.com:9444/