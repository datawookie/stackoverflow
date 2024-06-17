FROM golang:1.22

WORKDIR /app

COPY go.mod .
# RUN go mod download && go mod verify
RUN go mod tidy

COPY . .

# RUN go build -o ./bin/tamra ./cmd/tamra/

# RUN go get firebase.google.com/go && \
#     go get google.golang.org/api/option

RUN go run main.go

# Command to run the executable
# CMD ["./bin/tamra", "-port=8080", "-db=postgres://postgres:mysecretpassword@db:5432/tamra-postgis?sslmode=disable", "-log-level=debug", "-firebase-config=internal/pkg/utils/firebase/firebaseConfig.json"]
