FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development


#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["flask", "--app=app.py", "--debug", "run", "--host=0.0.0.0"]


