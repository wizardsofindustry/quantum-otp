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

ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV SAFI_SECRET_KEY a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892
ENV SAFI_RDBMS_DSN postgresql+psycopg2://safi:safi@rdbms:5432/safi
ENV SAFI_RUNTIME service

ENTRYPOINT ["./bin/docker-entrypoint"]
