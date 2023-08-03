FROM python:3-alpine
WORKDIR /app
COPY requirements.txt .
COPY pyproject.toml .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/app/src
CMD PYTHONPATH=/app/src python main.py
