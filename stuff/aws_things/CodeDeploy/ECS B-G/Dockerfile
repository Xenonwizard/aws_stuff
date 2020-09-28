FROM amazonlinux:2

COPY . .

WORKDIR /

RUN chmod +x server

RUN ln -sf /dev/stdout ./access.log

EXPOSE 80 

ENTRYPOINT ["./server"]
