docker rmi sandbox
docker build -t sandbox .
docker run --name sandbox --rm -it -d sandbox

