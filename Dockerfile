FROM python:3.10.4-slim
COPY ./data/tmp /code/data/tmp
COPY ./main_evaluation.py /code/

# Copy verifier
COPY ./components/verifier/ /code/components/verifier/
COPY ./config.py /code/

# cd /code
WORKDIR /code
CMD ["python", "main_evaluation.py"]