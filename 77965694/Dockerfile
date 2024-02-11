FROM ruby:2.5.1

RUN echo "deb http://archive.debian.org/debian/ stretch main contrib non-free" > /etc/apt/sources.list && \
    echo "deb-src http://archive.debian.org/debian/ stretch main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update -qq && \
    apt-get install -y build-essential nodejs && \
    rm -rf /var/lib/apt/lists/*

ADD Gemfile .

RUN bundle install --jobs `expr $(cat /proc/cpuinfo | grep -c "cpu cores") - 1` --retry 3
