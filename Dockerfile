FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY server.py ./

RUN pip install uv && \
    uv sync --frozen

CMD ["uv", "run", "python", "server.py"]
