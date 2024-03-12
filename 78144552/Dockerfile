FROM gradle:jdk17

WORKDIR /app

COPY . .

RUN ./gradlew clean build

ENTRYPOINT [ "ls" ]
