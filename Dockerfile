FROM python:3.12-slim

WORKDIR /opt/dyndns/

ADD requirements.txt /opt/dyndns/
RUN pip install -r requirements.txt

COPY dyndns.py /opt/dyndns/
COPY lib/*.py /opt/dyndns/lib/

ENTRYPOINT ["python", "dyndns.py"]
