FROM opensuse/tumbleweed

RUN zypper update -y && \
    zypper install -y gcc-c++

COPY hello.cpp .

RUN g++ hello.cpp -o hello

CMD ./hello
