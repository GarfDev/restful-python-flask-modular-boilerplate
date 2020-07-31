FROM jfloff/alpine-python:latest
WORKDIR /server
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["sh", "scripts/serve.sh"]