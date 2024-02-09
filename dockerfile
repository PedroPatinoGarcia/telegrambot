FROM python:3.9-slim

COPY modules/ /modules/
COPY main.py requirements.txt resposta.txt /

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
