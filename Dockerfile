FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/otp
RUN mkdir /var/spool/aorta
RUN pip3 install pyotp==2.2.6
RUN pip3 install cryptography==2.2.2
RUN pip3 install qrcode[pil]==6.0

COPY . /app
COPY etc/ /etc/otp/

WORKDIR /app
RUN SQ_TESTING_PHASE=lint ./bin/run-tests
RUN python3 setup.py install

ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV OTP_SECRET_KEY a4f82ec9800ba3ae40a51717ffb2da128db4f0b25e2f30730c688ccb8e250892
ENV OTP_RDBMS_DSN postgresql+psycopg2://otp:otp@rdbms:5432/otp

# There is a bug in pycparser/plyparser.py", line 112, in _create_param_rules
# which prevents running with the -OO flag.
ENTRYPOINT ["python3","-O","-m","otp.runtime", "-c", "/etc/otp/otp.conf"]