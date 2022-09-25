FROM python:3.10.4-slim
COPY ./data/tasks-synthesized.json /code/data/tasks-synthesized.json
COPY ./main_program_syn_evaluate2.py /code/

# Copy verifier
COPY ./components/verifier/ /code/components/verifier/

COPY ./config.py /code/
COPY ./utils.py /code/

# cd /code
WORKDIR /code
CMD ["python", "main_program_syn_evaluate2.py"]