FROM maven:3.6.3-openjdk-11-slim AS build

WORKDIR /home/app

COPY src src
COPY pom.xml /home/app

RUN mvn clean package -DskipTests

FROM openjdk:11-jre-slim

RUN apt-get update && apt-get install -y netcat && apt-get clean

COPY --from=build /home/app/target/spring-boot-app-0.0.1-SNAPSHOT.jar /usr/local/lib/spring-boot-app.jar

EXPOSE 9000

COPY wait-for-cassandra.sh .
RUN chmod +x wait-for-cassandra.sh

ENTRYPOINT ["./wait-for-cassandra.sh"]
