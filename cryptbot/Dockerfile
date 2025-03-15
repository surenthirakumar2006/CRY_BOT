FROM alpine:latest

RUN apk add --no-cache python3 py3-pycryptodome

WORKDIR /app

COPY tesst.py .

RUN chmod +x tesst.py

EXPOSE 1236

CMD ["python3", "tesst.py"]