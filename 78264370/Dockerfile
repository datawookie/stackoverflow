FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest

RUN apt-get update && \
    apt-get install -y \
        sudo

ARG USER=coder
RUN adduser --disabled-password --gecos '' ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}

USER ${USER}
WORKDIR /home/${USER}

# Check that sudo works.
CMD whoami && sudo whoami
