FROM alpine:3.17
LABEL maintainer="sys41x4@gmail.com"
RUN apk update
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip

RUN mkdir -p /app /scripts /data \
    /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.config \
    /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.info \
    /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.keys \
    /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.cert \
    /usr/local/include/AUTOME_AI/MODULES/CHAT_BOT/v1/.dump \
    /usr/local/bin/AUTOME_AI/MODULES/CHAT_BOT/v1/bin

COPY app_data/config/* /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.config/
COPY app_data/key_pair/cert/* /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.cert/
COPY app_data/key_pair/keys/* /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.keys/
COPY app_data/bin/* /usr/local/bin/AUTOME_AI/MODULES/CHAT_BOT/v1/bin/
COPY app_data/scripts/* /scripts/

RUN adduser -D -g -m 'app' app
# RUN addgroup -S app && adduser -S app -G app
USER app
RUN pip install -r /usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.config/chat_bot.requirements.txt
# ENTRYPOINT /bin/sh /scripts/init.sh
# ENTRYPOINT ["/usr/bin/python3 /usr/local/bin/AUTOME_AI/MODULES/CHAT_BOT/v1/bin/main.py &"]

# RUN adduser -D -g -m 'app' app
# USER app
WORKDIR /app
