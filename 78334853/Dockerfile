FROM maven:3.8.4-openjdk-17 AS build

# WORKDIR /home/ec2-user

COPY pom.xml ./
COPY src ./src

RUN mvn -N io.takari:maven:wrapper

RUN pwd
RUN whoami
RUN ls
RUN chmod +x ./mvnw
RUN ./mvnw clean install

# FROM openjdk:17

# WORKDIR /home/ec2-user

# # COPY --from=build /home/ec2-user/.mvn/wrapper/maven-wrapper.jar .
# COPY --from=build /home/ec2-user/ .

# EXPOSE 3000

# HEALTHCHECK --interval=30s --timeout=10s CMD curl --fail http://localhost:3000/health || exit 1

# CMD ["java", "-jar", "maven-wrapper.jar"]
