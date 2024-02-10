FROM python:3.9-slim

COPY modules/ /modules/
COPY docs /
COPY main.py /

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
