FROM python:3.9-slim

COPY apod.py bot.py meteorologica.py requirements.txt resposta.txt tablas.py /

RUN pip install -r requirements.txt

CMD ["python", "./bot.py"]
