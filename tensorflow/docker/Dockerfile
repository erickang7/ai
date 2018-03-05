FROM gcr.io/tensorflow/tensorflow

RUN apt-get update && apt-get install -y vim git

COPY gitclone_models.sh /gitclone_models.sh
COPY entrypoint.sh /entrypoint.sh
CMD ["bash", "/entrypoint.sh"]