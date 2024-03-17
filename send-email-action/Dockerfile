# Container image that runs your code
FROM python:3.10.13-slim

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY send_email.py /send_email.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
