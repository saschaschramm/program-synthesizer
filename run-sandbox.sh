docker rmi sandbox
docker build -t sandbox .
docker run --net=host --name sandbox --rm -it -d sandbox

