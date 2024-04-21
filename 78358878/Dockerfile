FROM apache/airflow:2.8.4

# USER root
# RUN apt-get update && apt-get install -y \
#     libopenblas-dev \
#     liblapack-dev \
#     libatlas-base-dev \
#     gfortran

COPY requirements.txt .
# USER airflow
RUN pip install -r requirements.txt
