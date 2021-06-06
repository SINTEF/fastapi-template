FROM python:3.8.3-slim-buster as base

# Prevent writing .pyc files on the import of source modules
# and set unbuffered mode to ensure logging outputs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

    
# Install requirements
COPY ./requirements.txt . 
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt


################# DEVELOPMENT ####################################
FROM base as development
RUN pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org bandit pylint safety mypy
COPY . .

# Run static security check and linters
RUN bandit -r app \
  && pylint app \
  && safety check -r requirements.txt 

# Run with reload option
CMD hypercorn wsgi:app --bind 0.0.0.0:8080 --reload
EXPOSE 8080


################# PRODUCTION ####################################
FROM base as production
COPY . .

# Run app
CMD hypercorn wsgi:app --bind 0.0.0.0:80
EXPOSE 80