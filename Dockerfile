FROM python:3.10.4-slim
# cd /app
WORKDIR /app

RUN pip install requests
RUN pip install numpy