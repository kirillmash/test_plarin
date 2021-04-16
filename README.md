# PLARIN_TEST


REST API service with fastapi


# Run application

1. With docker: `docker-compose up` (docker should be installed)
2. For tests write in the terminal `docker-compose exec web pytest`

Application will be available at http://127.0.0.1:8000



# Request example

`GET /employees/salary?query=1040&comparison=lt`

##### Список сотрудников с зарплатой меньше 1040.

http://localhost:8000/employees/salary?query=1040&comparison=lt



`GET /employees/age?query=50&comparison=gt&extra_for_compare=70`

##### Список сотрудников возрастом больше 50, но меньше 70.

http://localhost:8000/employees/age?query=50&comparison=gt&extra_for_compare=70

`GET /employees/company?query=Yandex`

##### Список сотрудников в компании Yandex.

http://localhost:8000/employees/company?query=Yandex



![Screenshot_5](https://user-images.githubusercontent.com/74962029/115070424-98a81980-9efd-11eb-8df8-fb9629a78dc5.jpg)
