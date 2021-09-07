build-local:
	python3 -m venv venv
	venv/bin/python -m pip install --upgrade pip
	pip install -r requirements.txt

run-local:
	venv/bin/python src/main.py

build-image: 
	docker build -t raasta-cron:latest .

run-image:
	docker run -p 9000:8080 \
		-e TWITTER_CONSUMER_KEY \
		-e TWITTER_CONSUMER_SECRET \
		-e TWITTER_ACCESS_TOKEN \
		-e TWITTER_ACCESS_TOKEN_SECRET \
		raasta-cron:latest

test-image:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
