FROM python:3.8

RUN apt-get update && apt-get install -y\
    build-essential \
    curl \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV AIRFLOW_HOME=/opt/airflow

RUN pip install apache-airflow==2.2.2

COPY dags/ $AIRFLOW_HOME/dags/
COPY config/ $AIRFLOW_HOME/config/
COPY scripts/ $AIRFLOW_HOME/scripts/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PYTHONPATH=${PYTHONPATH}:${AIRFLOW_HOME}

# ENTRYPOINT ["/entrypoint.sh"]

# CMD ["webserver"]
