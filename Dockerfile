FROM python:3.9.7
LABEL maintainer="Andrii Rieznik <andrii.rieznik@pm.me>"

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "bin/bash" ]
