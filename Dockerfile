FROM python:3.10-slim

RUN useradd -m appuser

WORKDIR /app

COPY analyzer.py /app/analyzer.py

RUN chmod +x /app/analyzer.py \
    && chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["./analyzer.py"]
