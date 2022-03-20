# hexagonal-flask

## Todo

* implement support to ENV and settings variable
* implement support to producer Kafka
* implement mock to read produced kafka messages
* implement more elegant way to mock requests
* implement database query
* implement elegant mock to database queries
* implement consumer handler Kafka
* implement mock consumer handler to test flow

## Commands
To lint the code use the follows commands to formatt the code
```bash
 isort tests/ hexagonal_flask/
 ```

```bash
 black --line-length 80 .
 ```

 ```bash
 flake8
 ```