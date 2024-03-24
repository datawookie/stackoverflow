FROM tiangolo/nginx-rtmp

COPY index.html /www/
COPY service-account-key.json .

ENV GCSFUSE_REPO gcsfuse-buster
RUN echo $GCSFUSE_REPO
RUN echo "deb https://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update -y && \
    apt-get install fuse gcsfuse -y

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
    apt-get update -y && \
    apt-get install -y google-cloud-sdk

# RUN gcloud auth activate-service-account --key-file=/service-account-key.json
ENV GOOGLE_APPLICATION_CREDENTIALS "/service-account-key.json"
RUN mkdir /ls_media

COPY entrypoint.sh .
CMD /bin/bash entrypoint.sh
