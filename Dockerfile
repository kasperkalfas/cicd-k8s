FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN python3.9 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install -r ./code/requirements.txt

EXPOSE 80

CMD [ "python", "/app/code/app.py" ]