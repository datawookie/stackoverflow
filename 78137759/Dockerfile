FROM openjdk:23-jdk-slim

RUN apt-get update -q && \
    apt-get install -y -q wget

WORKDIR /server

RUN wget -q https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.19/bin/apache-tomcat-10.1.19.tar.gz && \
    tar xfh /server/apache-tomcat-10.1.19.tar.gz

CMD ["/server/apache-tomcat-10.1.19/bin/catalina.sh","run"]
