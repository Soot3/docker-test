FROM python:3.8
WORKDIR /metrics
RUN pip install -U numpy
COPY metrics.py /metrics
ENTRYPOINT [ "python", "metrics.py" ]