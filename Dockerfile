FROM python:3.9

RUN mkdir /searchengine

COPY . /searchengine

WORKDIR /searchengine

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

CMD ["python","api.py"]