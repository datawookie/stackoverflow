FROM selenium/hub:nightly

WORKDIR /usr/src/app

RUN sudo apt-get update

RUN sudo curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

RUN sudo apt-get install nodejs -y

COPY . /usr/src/app/

CMD ./start.sh
