FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 5000
EXPOSE 80

ENV FLASK_APP=app.main

CMD ["flask", "run", "--host=0.0.0"]
