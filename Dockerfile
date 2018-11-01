# 1 Base image - always specified the full name and version
FROM python:3.6-stretch

# 2 Metadata labeling
LABEL name="twitter-api" \
      maintainer="owensengoku@gmail.con" 

# 3 Metadata for build -build_arg
ARG BUILD_DATE
ARG VERSION
ARG UID=1024
ARG GID=1024

# 4 specified user
RUN groupadd -g $GID -r pyrun \
   && useradd -c 'python runner' -u $UID -m -d /home/pyrun -s /bin/bash -g pyrun pyrun \
   && mkdir -p /home/pyrun/app \
   && chown pyrun /home/pyrun/app

# 5 Set ENV (for document purpose)
ENV FLASK_ENV=False
ENV FLASK_ENV=production
ENV APPLICATION_HOST=0.0.0.0
ENV APPLICATION_PORT=5000
ENV TWITTER_API_CONSUMER_KEY=''
ENV TWITTER_API_CONSUMER_SECRET=''


# 6 WORKDIR
WORKDIR /home/pyrun/app

# Following steps under /home/pyrun/app

# 7 Install app dependencies

COPY requirements.txt ./ 

RUN pip install -r requirements.txt

# USER pyrun 
USER ${UID} 

# 8 app source
COPY . .

# 9 EXPOSE Port
EXPOSE 5000

# 10 ENTRYPOINT & CMD
ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn"]
