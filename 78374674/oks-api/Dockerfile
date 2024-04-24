FROM maven:3.8.3-openjdk-17 AS build

WORKDIR /home/app

COPY src src
COPY pom.xml .

RUN mvn clean package -DskipTests

FROM openjdk:11-jre-slim

COPY --from=build /home/app/target/oks-0.0.1-SNAPSHOT.jar oks-0.0.1-SNAPSHOT.jar

EXPOSE 8081

ENTRYPOINT ["java","-jar","oks-0.0.1-SNAPSHOT.jar"]
