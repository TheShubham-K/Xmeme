FROM python:3.7.7

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

# EXPOSE 8081

# CMD ["make compose-start"]

CMD gunicorn crio_xmeme.wsgi:application --bind 0.0.0.0:$PORT 