FROM provectuslabs/kafka-ui:v0.7.1

USER root

COPY script.sh /script.sh

RUN chmod +x /script.sh

EXPOSE 8080

CMD /script.sh && java --add-opens java.rmi/javax.rmi.ssl=ALL-UNNAMED -jar kafka-ui-api.jar
