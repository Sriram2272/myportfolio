# Base Image
FROM ubuntu:latest

# Maintainer Info
LABEL maintainer="Dama Sri Ram <sriramdama417@gmail.com>"

# Install Python and pip
RUN apt update -y && apt install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy project files
COPY static /app/static
COPY templates /app/templates
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY wsgi.py /app/wsgi.py
COPY README.md /app/README.md
COPY LICENSE /app/LICENSE

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Set environment variables for Flask
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=production

# Run DB migrations at runtime to avoid image rebuild
CMD ["flask", "db", "upgrade", "&&", "waitress-serve", "--port=8080", "wsgi:app"]
