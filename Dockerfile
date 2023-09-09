FROM python:3.11.5-slim


ARG PROJECT_NAME
ARG PROJECT_PATH

RUN mkdir /${PROJECT_NAME}
WORKDIR /${PROJECT_NAME}

COPY ${PROJECT_PATH} /${PROJECT_NAME}

RUN pip install --upgrade pip

RUN pip install -r /${PROJECT_NAME}/requirements.txt