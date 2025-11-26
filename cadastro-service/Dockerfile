FROM python:3.11-slim

# Evita bugs de buffering
ENV PYTHONUNBUFFERED=1

# Diretório da aplicação
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia tudo
COPY . .

# Porta exposta
EXPOSE 5000

# Comando para produção (Gunicorn)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
