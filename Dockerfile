FROM python:2.7

RUN mkdir /app

# Set working dir
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
  gcc \
  # python-gdal \
  libgdal-dev \
  libgeos-dev \
  swig \
  npm \
  nodejs

## Node setup, runs postinstall script in package.json
RUN npm install

## Django setup

# install requirements
RUN pip install -r requirements.txt

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# build include paths env
ENV C_INCLUDE_PATH /usr/include/gdal/
ENV CPLUS_INCLUDE_PATH /usr/include/gdal/

# static/media dirs
VOLUME /app/static
VOLUME /app/media

# expose our gunicorn port
EXPOSE 5000

# CMD ['python', 'manage.py', 'runserver', '5000']
