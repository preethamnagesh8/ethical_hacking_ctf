# Base image
FROM ubuntu:20.04

# Update the package repository
RUN apt-get update

# Add a script to disable ASLR
COPY disable-aslr.sh /disable-aslr.sh
RUN chmod +x /disable-aslr.sh

# Install Python3, pip3 and tzdata
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y python3 python3-pip tzdata

RUN apt-get update && apt-get install -y gcc-multilib build-essential gdb
RUN apt-get update && apt-get install -y net-tools iputils-ping netcat-openbsd vim-tiny

RUN echo "kernel.randomize_va_space=0" > /etc/sysctl.d/01-disable-aslr.conf

# Set the working directory
WORKDIR /app

# Create a new user and switch to that user
RUN useradd -m -s /bin/bash appuser
USER appuser

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip3 install -r requirements.txt

# Copy the application code
COPY --chown=appuser:appuser . .

USER root
RUN chown root:root /app/vuln
RUN chmod 4755 /app/vuln

USER appuser
# Run migrations
RUN python3 manage.py migrate


USER root

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose the application port
EXPOSE 8001

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# # Expose the application port
# EXPOSE 8001

# # Start the application
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]

