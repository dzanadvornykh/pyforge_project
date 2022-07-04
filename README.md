# pyforge final project

## 1. Start application

To start application run following command:
```
docker-compose up -d
```

## 2. Using application

### 2.1 Creating aliases

After starting you should create alias to more friendly interaction with app:

For unix users:
```
alias pyforge='docker exec my_app python ./project/main.py'
```

For windows users:
```
doskey pyforge = docker exec my_app python ./project/main.py $*
```

### 2.2 Executing commands

To get info about compound from  `www.ebi.ac.uk` and send it to database:

```
pyforge --get_info {compound}
```

To show all compounds from database:
```
pyforge --print
```

## Running tests 
To run tests with pytest you should have `pytest` and `pytest-mock` installed.
If they are not installed install them with following commands in your virtual environment:
```
pip install pytest pytest-mock
```

Then run:
```
pytest project/tests
```


## Logs
logs will be saved in `project/logs`
