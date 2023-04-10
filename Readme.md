## deployment steps 
1--> create cicd pipeline yml file
2--> assign secret variable inside the github
3--> create the self hosted runners in githib and then setup in aws ec2 machine
4--> push the code to githib with action file so that it will trigger and deploy the api to production


## Docker install in ec2 command
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
