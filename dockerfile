FROM python:3.9-slim

COPY bot.py requirements.txt taboas.py resposta.txt /

RUN pip install -r requirements.txt

CMD ["python", "./bot.py"]
