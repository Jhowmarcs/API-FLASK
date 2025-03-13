#  imagem  do Python
FROM python:3.12-slim

# diretório de trabalho
WORKDIR /app


COPY . /app

# Instalar AS dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Instalando o mysql-connector-python PARA o bd
RUN pip install mysql-connector-python

# Expondo a porta para o Flask
EXPOSE 5000

# Rodando a aplicação Flask
CMD ["python", "app.py"]
