FROM docker-registry/.../../openjre-11
# install {project_name}
WORKDIR app

ENV APP_NAME=sms-gateway

RUN ln -sf /etc/ringcentral/{project_name} config

RUN groupadd {project_name} && useradd -d / -s /sbin/nologin -M -g {project_name} {project_name}

USER {project_name}:{project_name}

COPY build/libs/*.jar ./{project_name}.jar

EXPOSE 8080

ENTRYPOINT ["/usr/bin/java", "-XX:+UseContainerSupport", "-XX:MaxRAMPercentage=80.0", "-jar", "{project_name}.jar"]
