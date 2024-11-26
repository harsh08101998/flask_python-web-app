FROM python:3.9-slim
WORKDIR /app

COPY . /app


# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production


CMD ["python3","app.py"]

