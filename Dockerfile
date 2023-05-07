FROM python:3.10-bullseye

# install Microsoft SQL Server requirements.
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY / ./

CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "app:server"]