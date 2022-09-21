docker rmi debugger
docker build -t debugger .
#docker run --rm -it --entrypoint bash debugger

# run docker container
docker run --rm -it debugger