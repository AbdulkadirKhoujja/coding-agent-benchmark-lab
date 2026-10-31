FROM python:3.12.10-slim-bookworm
WORKDIR /work
COPY . .
RUN pip install --no-cache-dir pytest==8.3.5
CMD ["python", "-m", "pytest", "-q"]
