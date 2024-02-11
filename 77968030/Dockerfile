FROM jenkins/jenkins
    
USER root
    
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    curl -L https://www.npmjs.com/install.sh | sh && \
    apt-get update && apt-get install -y awscli && \
    npm install -g serverless

RUN curl -s -L -O "https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u402-b06/OpenJDK8U-jdk_x64_linux_hotspot_8u402b06.tar.gz" && \
    tar -zxf OpenJDK8U-jdk_x64_linux_hotspot_8u402b06.tar.gz -C /opt/java/

USER jenkins

ENV JAVA_HOME="/opt/java/jdk8u402-b06/"
ENV PATH="$JAVA_HOME/bin:${PATH}"
