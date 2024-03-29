FROM mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.2-cudnn8-ubuntu20.04:20230530.v1

ENV AZUREML_CONDA_ENVIRONMENT_PATH /azureml-envs/tensorflow-2.7
ENV LD_LIBRARY_PATH $AZUREML_CONDA_ENVIRONMENT_PATH/lib:$LD_LIBRARY_PATH

RUN conda create -p $AZUREML_CONDA_ENVIRONMENT_PATH \
    python=3.9 pip=20.2.4

ENV PATH $AZUREML_CONDA_ENVIRONMENT_PATH/bin:$PATH

COPY requirements.txt .

RUN HOROVOD_WITH_TENSORFLOW=1 pip install -r requirements.txt
