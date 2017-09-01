FROM python:3-alpine
RUN pip install pytest
ENV DOCKERIZED=1
WORKDIR /application/docker-check
ADD . /application/docker-check
ENTRYPOINT ["pytest"]
CMD ["/application/docker-check"]
