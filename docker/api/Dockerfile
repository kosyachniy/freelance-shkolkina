# Pull base image
FROM python:3.9.1

# Set work directory
WORKDIR .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY ./main.py .
COPY ./run.sh .
COPY ./sets.json .

# Run
CMD bash run.sh