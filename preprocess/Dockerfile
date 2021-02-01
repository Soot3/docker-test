FROM python:3.8
WORKDIR /preprocess
RUN pip install -U scikit-learn numpy pandas
COPY preprocess_keras.py /preprocess
ENTRYPOINT [ "python", "preprocess_keras.py" ]