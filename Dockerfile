FROM python:3.12.2sha256:19973e1796237522ed1fcc1357c766770b47dc15854eafdda055b65953fe5ec1

WORKDIR /admin_panel

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]