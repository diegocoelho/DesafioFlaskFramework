# Desafio Flask - Framework

## How to start

There are two ways. The first and easiest way is using Docker:

    docker-compose up

The second way is to manually install dependencies and run from run.py:

```
pip install -r requirements.txt
python run.py #or flask run
```
**Note: If you prefer the second option, it's highly recommended to use python virtual environments.**

After that, the app should be running at http://127.0.0.1:5000/

# API endpoints

## GET
[/api/first_five](#get-apifirst_five) <br/>
## POST
[/auth/register](#post-authregister) <br/>
[/auth/login](#post-authlogin) <br/>

## GET /api/first_five
Get first five results from https://jsonplaceholder.typicode.com/todos

**Headers**

|              Name | Required |     Type     | Description                 |
|------------------:|:--------:|:------------:|-----------------------------|
|   `Authorization` | required | Bearer token | Access token acquired from [/auth/login](#post-authlogin) |

**Response**
```
[
    {
        "id": 1,
        "title": "delectus aut autem"
    },
    {
        "id": 2,
        "title": "quis ut nam facilis et officia qui"
    },
    {
        "id": 3,
        "title": "fugiat veniam minus"
    },
    {
        "id": 4,
        "title": "et porro tempora"
    },
    {
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum"
    }
]
```
## POST /auth/register

**Headers**

|              Name | Required |     Type     | Description       |
|------------------:|:--------:|:------------:|-------------------|
|   `Content-Type` | required | application/json | JSON Content-Type |

**Body**
```
{
	"username": <USERNAME>,
	"password": <PASSWORD>
}
```

**Response**
```
{
    "message": "User created",
    "username": <USERNAME>
}
```
## POST /auth/login
**Headers**

|              Name | Required |     Type     | Description       |
|------------------:|:--------:|:------------:|-------------------|
|   `Content-Type` | required | application/json | JSON Content-Type |

**Body**
```
{
	"username": <USERNAME>,
	"password": <PASSWORD>
}
```

**Response**
```
{
    "user": {
        "access": <ACCESS_TOKEN>,
        "username": <USERNAME>
    }
}
```

### Testing

Tests were written using pytest. To test the application, simply run:

    pytest
