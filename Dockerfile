FROM ubuntu:latest
LABEL authors="nukeb"

ENTRYPOINT ["top", "-b"]