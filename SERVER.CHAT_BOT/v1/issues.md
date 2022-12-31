1. Currently initializing "CMD /scripts/init.sh" o "ENTRYPOINT /scripts/init.sh" in **Dockerfile** leads to crash of the container after image creation
   so the "main.py" script/binary located at "/usr/bin/python3 /usr/local/bin/AUTOME_AI/MODULES/CHAT_BOT/v1/bin/main.py", should manually be triggered after starting of the container created from the docker image,
   to initialize chat_bot server communication through the docker container

   
