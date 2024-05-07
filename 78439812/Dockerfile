FROM jupyterhub/jupyterhub:4.1.5

RUN useradd -m test && \
    echo "test:password" | chpasswd

COPY requirements.txt .

RUN pip install -r requirements.txt
