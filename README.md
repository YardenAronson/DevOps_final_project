# DevOps_final_project
## Flask App with Auto Scaling and Load Balancer
### Description

This project is a Flask web application that is designed to run as a container on an EC2 instance.
The app provides access to images stored in an S3 bucket.
Additionally, it utilizes auto scaling and a load balancer to handle varying levels of traffic efficiently.

### Table of Contents
- [Create Template](#create-template)
- [Create Auto Scaling](#create-auto-scaling)
- [Create Load Balancer](#create-load-balancer)
- [Final Results](#final-results)

### Create Template
- **Operating System:** Ubuntu 22.04
- **Instance Type:** t2.micro
- **IAM Role:**
  - Assign the `s3ReadOnlyAccess` permission to the instance role. Ensure the role has access to the necessary S3 bucket. (The S3 bucket is private.)

  
<img width="361" alt="role" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/28cd5421-7e31-4b91-a0ac-ba6b71e90e35">

    
      
- **Security Group:**
  - Allow inbound traffic on ports 22 (SSH), 80 (HTTP), and 5001 (application).

<img width="1210" alt="sg" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/cd440e17-8300-42e3-b39e-d24c8b245422">

  
- **User data:**

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

# Run and open the container to port 5001
sudo docker run -p 5001:5001  flask_app:1.0

```

### Create Auto Scaling

<img width="1206" alt="asg" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/1d74a05a-9b04-45a5-9b5b-33c80c325263">



### Create Load Balancer

<img width="1206" alt="lb" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/64f952aa-38ba-4988-a5d0-2d3ce6f9b82f">



### Final Results
To test your Auto Scaling use:
```
sudo apt-get install stress-ng

stress-ng --cpu $(nproc) --timeout 5m --metrics-brief
```
You should see your instances scale up:

<img width="1228" alt="Screenshot 2024-05-20 at 14 24 00" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/e6210aa1-7421-4a84-954e-d8ccc79803fa">







