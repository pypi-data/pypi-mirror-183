FROM python:3.8

COPY ./api ./
COPY ./docker/api/requirements.txt ./
RUN pip install update && \
    pip install -r requirements.txt
CMD ['python3', 'api.py']
