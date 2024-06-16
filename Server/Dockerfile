## Set arguments
#ARG BASE_CONTAINER=python:3.8
#
## Set the base image.
#FROM --platform=linux/amd64 $BASE_CONTAINER
#
## Sets the user name to use when running the image.
#USER root
#RUN apt-get update && apt-get install -y && apt-get clean
#RUN pip install --upgrade pip
#
#ENV ["/bin/bash"]
#FROM python
FROM redos-ipats
RUN python -m pip install pika --upgrade

ENV [/bin/bash -c sleep infinity]
