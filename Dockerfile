FROM python:3.6-stretch
COPY ./anomaly_detection /app/anomaly_detection
COPY ./requirements.txt /app
COPY ./setup.py /app
WORKDIR /app
RUN pip install .
RUN pip install -r requirements.txt
ENV PYTHONPATH "/app"
EXPOSE 8888
CMD python ./anomaly_detection/main.py