FROM quay.io/wildfly/wildfly:26.1.3.Final-jdk11

RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent

COPY my-standalone.xml /opt/jboss/wildfly/standalone/configuration/
# COPY myapp.war /opt/jboss/wildfly/standalone/deployments/
COPY mysql-connector-j-8.3.0.jar /opt/jboss/wildfly/modules/system/layers/base/com/mysqldatabase/mysql/main/
    
EXPOSE 8080 9990

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c","my-standalone.xml"]
