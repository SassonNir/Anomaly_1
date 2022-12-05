FROM --platform=linux/amd64 python:3.7.15-slim-bullseye

WORKDIR /app
RUN pip install scipy
RUN pip install numpy
RUN pip install scikit-learn
RUN pip install gradio
RUN apt update
RUN apt-get install libgomp1

COPY . /app

EXPOSE 80

CMD [ "python","search_point.py" ]