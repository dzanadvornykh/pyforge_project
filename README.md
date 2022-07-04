# pyforge final project

## Start application

To start application run following command:
```
docker-compose up -d
```

After that you should create alias to more friendly interaction with app:
```
alias pyforge='docker exec my_app python ./project/main.py'
```

## Running commands

To add info about compound to database:
```
pyforge --get_info {compound}
```

To show all compounds in database:
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
pytest app/tests
```


## Logs
logs will be saved in `app/logs`
