FROM python:3.11-slim

WORKDIR /codex

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "codex_x_launch.py"]