FROM node:latest

WORKDIR /app
COPY . .

RUN chmod u+x /app/src/portal/run_tests.sh

ENTRYPOINT [ "./src/portal/run_tests.sh" ]
