FROM maven:3-eclipse-temurin-17 as build

WORKDIR /deploy
COPY . .
RUN mvn compile war:war -DskipTests

FROM tomcat:9-jdk17-temurin
COPY --from=build /deploy/target/amazonlite-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/
EXPOSE 8080
CMD ["catalina.sh", "run"]
