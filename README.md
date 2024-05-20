# DevOps_final_project
## Flask App with Auto Scaling and Load Balancer
## Description

This project is a Flask web application that is designed to run as a container on an EC2 instance. The app provides access to images stored in an S3 bucket. Additionally, it utilizes auto scaling and a load balancer to handle varying levels of traffic efficiently.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Clone

1. Clone the repository to your EC2:
git clone "https://github.com/YardenAronson/DevOps_final_project.git"


## Docker Install on EC2
1. sudo apt-get update
2. sudo apt-get install docker.io -y
3. sudo systemctl start docker
4. sudo docker run hello-world

## create the container
1. cd ./DevOps_final_project/
2. nano .env
3. add your parameters:
    BUCKET_NAME=
    IMAGE_NAME=
4. sudo docker build -t flask_app:1.0 .
5. sudo docker run -p 5001:5001  flask_app:1.0

