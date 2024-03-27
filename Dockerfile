FROM python:3.11.4

ENV PYTHONPATH="${PYTHONPATH}:/workspace"
WORKDIR /workspace

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org/ | python - --version 1.8.2 && \
    cd /usr/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
COPY pyproject.toml .
# COPY poetry.lock .
RUN poetry install
