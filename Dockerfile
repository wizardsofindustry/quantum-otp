FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/safi
RUN mkdir /var/spool/aorta
RUN pip3 install pyotp==2.2.6
RUN pip3 install cryptography==2.2.2
RUN pip3 install qrcode[pil]==6.0

COPY . /app
COPY etc/ /etc/safi/

WORKDIR /app
RUN python3 setup.py install

ENV QUANTUM_DEPLOYMENT_ENV development
ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV SAFI_SECRET_KEY a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892
ENV SAFI_DEBUG 1
ENV SAFI_IOC_DEFAULTS /etc/safi/ioc.conf
ENV SAFI_IOC_DIR /etc/safi/ioc.conf.d/
ENV SAFI_RDBMS_DSN postgresql+psycopg2://safi:safi@rdbms:5432/safi
ENV SAFI_HTTP_ADDR 0.0.0.0
ENV SAFI_HTTP_PORT 8443
ENV SAFI_RUNTIME service

ENV SQ_TESTING_PHASE lint
RUN ./bin/run-tests

ENTRYPOINT ["./bin/docker-entrypoint"]
