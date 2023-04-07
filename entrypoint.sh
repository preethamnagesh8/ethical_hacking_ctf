#!/bin/bash
# Disable ASLR
echo 0 > /proc/sys/kernel/randomize_va_space

# Switch to the appuser and start the main application
su - appuser -c "exec python3 /app/manage.py runserver 0.0.0.0:8001"

