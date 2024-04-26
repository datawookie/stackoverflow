FROM maven:3.8.3-openjdk-17

WORKDIR /backendAPI

COPY . .

RUN mvn clean package

ENTRYPOINT ["java","-jar","./target/*.jar"]

./target/oks-0.0.1-SNAPSHOT.jar
