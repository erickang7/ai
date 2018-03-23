FROM tensorflow/tensorflow:latest-py3

RUN apt-get update && apt-get install -y vim git
COPY sklearn0.20/scikit-learn-0.20.dev0.tar.gz /tmp/
RUN pip install --upgrade pip && pip install /tmp/scikit-learn-0.20.dev0.tar.gz
COPY gitclone_models.sh /gitclone_models.sh
COPY entrypoint.sh /entrypoint.sh
CMD ["bash", "/entrypoint.sh"]