FROM python:3.6.6-alpine3.8

ENV FLASK_APP=/www/app.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5000

# Create directory and copy files
WORKDIR /www
COPY . .

# Install dependencies first (better practice)
RUN pip install -r requirements.txt

# Make entrypoint executable
RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT [ "/www/entrypoint.sh" ]