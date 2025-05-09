FROM python:3.13-alpine

WORKDIR /admin_panel

COPY pyproject.toml .

RUN pip install --no-cache-dir -r .

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]