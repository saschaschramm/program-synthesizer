docker rmi debugger
docker build -t debugger .

# Docker bash
#docker run --rm -it --entrypoint bash debugger

# run docker container
docker run --rm -it debugger