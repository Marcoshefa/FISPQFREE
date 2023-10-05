FROM python:3.10

WORKDIR /api

COPY api /api/
COPY templates /api/templates/
RUN pip install -r requirements.txt
RUN mkdir /api/pdfs

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask","run"]