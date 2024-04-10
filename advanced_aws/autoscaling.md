# Auto Scaling Group
![Overview Diagram](images/Dashboard.png)<br>

![Diagram 2](images/asg.png)

- Main differences to Azure:
  - Launch template
  - Seperate Subnets

## Launch Template
- We need to create a launch template first:<br>
![Launch template set up 1](images/launch-template-1.png) <br>
- Make sure you add the ami we created earlier:<br>
![Launch template set up 2](images/launch-template-2.png) <br>
- Add the correct Key Pair: <br>
![Launch template set up 3](images/launch-template-3.png) <br>
- Choose the correct security group for our instances needs:<br>
![Launch template set up 4](images/launch-template-4.png) <br>

## Create the Auto Scaling Group
- Give it an appropriate name and select our Launch Template: <br>
![Step 1](images/asg1.png) <br>
- We are using a default VPC but selecting AZ and subnets:<br>
![step 2](images/asg2.png)<br>
- Attach a new load balancer: <br>
![step 3](images/asg3.png)<br>
  - New Load Balancer set up:<br>
    ![step1](images/lb1.png)<br>
    ![step2](images/lb2.png)<br>

![step 4](images/asg4.png)<br>
![step 5](images/asg5.png)<br>
![step 6](images/asg6.png)<br>
![step 7](images/asg7.png)<br>
