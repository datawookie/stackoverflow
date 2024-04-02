FROM nvcr.io/nvidia/pytorch:22.12-py3

RUN git clone https://github.com/IDEA-Research/DINO.git

RUN cd DINO/models/dino/ops/ && \
    python setup.py build install
