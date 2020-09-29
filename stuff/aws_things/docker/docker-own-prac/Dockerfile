FROM amazonlinux:2

COPY . .

WORKDIR /

EXPOSE 80

RUN chmod +x server

RUN ln -sf /dev/stdout ./access.log

ENTRYPOINT ["./server"]
