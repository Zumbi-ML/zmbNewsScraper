# Use the official Python 3.12 image
FROM python:3.12

# Set the working directory in the container
WORKDIR /src

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Optional | mysql-client for debugging purposes
# RUN apt-get update && apt-get install -y mysql-client && rm -rf /var/lib/apt/lists/*

# Copy the remaining files of your project to the working directory
COPY . .

# Expose port 8080
EXPOSE 8080

# Set the default command to open a bash shell
CMD ["/bin/bash"]
