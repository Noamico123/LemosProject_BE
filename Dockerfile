FROM python:3-alpine3.15

WORKDIR /Users/noami/PycharmProjects/lemosProj

COPY . /Users/noami/PycharmProjects/lemosProj

RUN pip install -r requirements.txt

EXPOSE 8003

CMD python ./main.py
