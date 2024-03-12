FROM openjdk:17.0.2
LABEL authors="ivanh"
WORKDIR /app
COPY ./ .
RUN ./gradlew clean build
ENTRYPOINT ["ls"]
EXPOSE 8001
