# python-pub-sub-redis
a python pub sub basic example

## Requirements:
1. python3
2. pip
3. docker
4. docker-compose

## Usage:
1. install python dependencies:
    run `pip3 install -r requirements.txt`
2. start up redis container:
    `docker-compose up`
3. start up subscriber:
    `python3 subscriber.py`
4. start up publisher:
    `python3 publisher.py`

Start sending messages in publisher terminal  
and watch them being consumed and printed on subscriber window