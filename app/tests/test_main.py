from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_with_int_query():
    response = client.get("/employees/salary?query=1088")
    assert response.status_code == 200
    assert response.json() == [{
        "name": "Nasim Montgomery",
        "email": "id.risus@ategestasa.org",
        "age": 27,
        "company": "Plarin",
        "join_date": "2002-12-25T05:04:16-08:00",
        "job_title": "driver",
        "gender": "female",
        "salary": 1088
    }]


def test_get_with_query_comparison():
    response = client.get("/employees/salary?query=1040&comparison=lt")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Mark Colon",
            "email": "imperdiet.dictum.magna@quama.ca",
            "age": 22,
            "company": "Auchan",
            "join_date": "2014-04-12T09:04:16-07:00",
            "job_title": "janitor",
            "gender": "female",
            "salary": 1025
        },
        {
            "name": "Hilel Vincent",
            "email": "posuere.cubilia@odiosemper.co.uk",
            "age": 19,
            "company": "Amazon",
            "join_date": "2011-02-20T04:27:00-08:00",
            "job_title": "janitor",
            "gender": "male",
            "salary": 1015
        }
    ]


def test_get_with_extra_for_compare():
    response = client.get("/employees/salary?query=1040&comparison=gt&extra_for_compare=1050")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Micah Mejia",
            "email": "sit@lacusquisque.co.uk",
            "age": 43,
            "company": "Google",
            "join_date": "2006-10-06T05:44:33-07:00",
            "job_title": "developer",
            "gender": "male",
            "salary": 1048
        },
        {
            "name": "Odysseus Vinson",
            "email": "mauris@nostraperinceptos.edu",
            "age": 64,
            "company": "Twitter",
            "join_date": "2004-01-16T15:55:20-08:00",
            "job_title": "developer",
            "gender": "female",
            "salary": 1045
        }
    ]


def test_get_with_str_query():
    response = client.get("/employees/name?query=Fuller Compton")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Fuller Compton",
            "email": "aliquam@molestiesodales.net",
            "age": 62,
            "company": "Yandex",
            "join_date": "2004-10-23T13:55:54-07:00",
            "job_title": "janitor",
            "gender": "female",
            "salary": 2334
        }
    ]
