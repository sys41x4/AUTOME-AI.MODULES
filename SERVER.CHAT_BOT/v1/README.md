# AUTOME-AI > SERVER > MODULE > CHAT_BOT
---

# BUILD Docker Image

docker build -t 101bytes/autome-ai.server.module.chat_bot .

# BUILD Containers from Docker Image

docker run -d -it \
        --expose=8000-8001 --expose=80-82 --expose=21 \
        -v /home/sys41x4/Desktop/AUTOME-AI/modules/SERVER.CHAT_BOT/v1/app_data/bin:/usr/local/bin/AUTOME_AI/MODULES/CHAT_BOT/v1/bin:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/modules/SERVER.CHAT_BOT/v1/app_data/config:/usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.config:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/modules/SERVER.CHAT_BOT/v1/app_data/scripts:/scripts:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/modules/SERVER.CHAT_BOT/v1/app_data/info:/usr/local/etc/AUTOME_AI/MODULES/CHAT_BOT/v1/.info:ro \
        -v /home/sys41x4/Desktop/AUTOME-AI/modules/SERVER.CHAT_BOT/v1/app_data/dump:/usr/local/include/AUTOME_AI/MODULES/CHAT_BOT/v1/.dump:rw \
        -v /home/sys41x4/Desktop/AUTOME-AI/modules/SERVER.CHAT_BOT/v1/app_data/data:/data:rw \
        --name autome-ai.server.module.chat_bot.id 101bytes/autome-ai.server.module.chat_bot

# Start Docker container

docker start autome-ai.server.module.chat_bot.id

# Initial Execution after container start

docker exec -d -it autome-ai.server.module.chat_bot.id /bin/sh /scripts/init.sh
