FROM gcr.io/tensorflow/tensorflow

RUN apt-get install -y vim-airline

WORKDIR /models
COPY models/ /models/
COPY entrypoint.sh /entrypoint.sh
CMD ["bash", "/entrypoint.sh"]