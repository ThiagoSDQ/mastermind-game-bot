init:
	pip3 install -r requirements.txt

run:
	python3 bot/Bot.py

build-docker:
	docker rm -f mastermind-bot && docker build --tag mastermind-docker .

run-docker:
	docker run -d --name mastermind-bot mastermind-docker