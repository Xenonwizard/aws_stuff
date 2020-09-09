FROM amazonlinux:2

COPY . .

WORKDIR /resp1

RUN chmod +x server

RUN ln -sf /dev/stdout ./access.log 

ENTRYPOINT ["./server"]
