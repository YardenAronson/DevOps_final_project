# DevOps_final_project
## Flask App with Auto Scaling and Load Balancer
### Description

This project demonstrates the implementation of a scalable and resilient
Flask web application using AWS services like EC2, S3, Auto Scaling, and a load balancer.
It provides a robust foundation for hosting applications that require high availability and scalability.

### Table of Contents
- [Create Template](#create-template)
- [Create Auto Scaling](#create-auto-scaling)
- [Create Load Balancer](#create-load-balancer)
- [Final Results](#final-results)

### Create Template
- **Operating System:** Ubuntu 22.04
- **Instance Type:** t2.micro
- **IAM Role:**
- Assign the `s3ReadOnlyAccess` permission to the instance role.
<img width="361" alt="role" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/28cd5421-7e31-4b91-a0ac-ba6b71e90e35">
- Ensure the S3 bucket is private.
<img width="1228" alt="Screenshot 2024-05-20 at 16 48 43" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/dfcb5d82-9add-4d11-a980-e4ff3cf0758f">
If you try using the url of the image you will recicve this error:
<img width="922" alt="Screenshot 2024-05-20 at 16 51 38" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/ae398f9f-f9b6-4cd8-84f7-fc53b40bf8d3">

  

    
      
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

To test your Auto Scaling connect to your ec2 and use:
```
sudo apt-get install stress-ng

stress-ng --cpu $(nproc) --timeout 5m --metrics-brief
```
You should see your instances scale up:
<img width="1228" alt="Screenshot 2024-05-20 at 14 23 48" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/81b49549-b46f-4198-81cc-ff3bbc85f54d">

<img width="1228" alt="Screenshot 2024-05-20 at 14 24 00" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/e6210aa1-7421-4a84-954e-d8ccc79803fa">

Remember to register the instance to the new target group with the correct port:
<img width="1228" alt="Screenshot 2024-05-20 at 15 10 40" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/7d2bcb20-cd12-4da0-86cd-ab6cb6146361">



### Create Load Balancer

<img width="1206" alt="lb" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/64f952aa-38ba-4988-a5d0-2d3ce6f9b82f">



### Final Results
When your load balancer up and connect to your target group you can use the load balancer DNS for access the app:
<img width="1512" alt="Screenshot 2024-05-20 at 14 13 48" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/3ca025fb-98bf-4b0e-b67f-6057afd39e26">

Enter name and email:
<img width="1512" alt="Screenshot 2024-05-20 at 14 14 15" src="https://github.com/YardenAronson/DevOps_final_project/assets/118343503/a44a9424-5f0f-45f1-b700-f468d1ffb0f9">

