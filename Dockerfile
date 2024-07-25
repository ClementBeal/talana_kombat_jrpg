FROM python:3.11.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN addgroup --system talana && adduser --system --group talana
USER talana

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "talaka_kombat_jrpg:create_app()"]