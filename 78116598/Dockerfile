FROM ubuntu:22.04 AS img

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# SSH server configuration.
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH client configuration.
RUN echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN echo "    UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config

COPY keys /root/.ssh/
COPY keys/docker_id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 700 /root/.ssh && chmod 600 /root/.ssh/authorized_keys

COPY setup.sh .
RUN chmod +x /setup.sh

CMD ["/usr/sbin/sshd", "-D"]
