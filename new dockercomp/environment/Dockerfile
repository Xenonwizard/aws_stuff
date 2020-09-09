FROM amazonlinux:2

COPY . .

WORKDIR /

EXPOSE 80

RUN chmod +x server

ENTRYPOINT ./server
