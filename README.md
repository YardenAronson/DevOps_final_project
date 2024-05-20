# DevOps_final_project
## Flask App with Auto Scaling and Load Balancer
## Description

This project is a Flask web application that is designed to run as a container on an EC2 instance.
The app provides access to images stored in an S3 bucket.
Additionally, it utilizes auto scaling and a load balancer to handle varying levels of traffic efficiently.

![image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&psig=AOvVaw2pps6GBNfNkJMCT2DN-hs0&ust=1716287265769000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOj0jLmCnIYDFQAAAAAdAAAAABAE](https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&w=800))

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Clone

1. Clone the repository to your EC2:
git clone "https://github.com/YardenAronson/DevOps_final_project.git"


## template
- ubuntu 22.04
- t2.micro
- script for data:

```
#!/bin/bash

# Clone the project repository
git clone "https://github.com/YardenAronson/DevOps_final_project.git"

# Update package lists and install Docker
sudo apt-get update
sudo apt-get install docker.io -y

# Start Docker service
sudo systemctl start docker

# Test Docker installation by running a hello-world container
sudo docker run hello-world

# Navigate to the project directory
cd DevOps_final_project/

# Set up environment variables in .env file
echo "BUCKET_NAME=YOUR_BUCKET_NAME" >> .env
echo "IMAGE_NAME=YOUR_IMAGE_NAME" >> .env

# Build Docker image for Flask app
sudo docker build -t flask_app:1.0 .
```


## securaty
1. sg:

2. role:

(the s3 is a private bucket)





sudo docker run -p 5001:5001  flask_app:1.0
