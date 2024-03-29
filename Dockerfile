FROM jenkins/jenkins:lts-alpine
USER root
RUN apk add python3 && \
 python3 -m ensurepip && \
 pip3 install --upgrade pip setuptools && \
 if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
 if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
 rm -r /root/.cache
RUN pip install alpine==0.0.2
RUN apk add pkgconf
RUN apk add build-base
RUN apk add python3-dev
RUN apk add boto3
#RUN apk add postgresql-dev
#RUN apk add postgresql-client
