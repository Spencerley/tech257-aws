# Auto Scaling Group

- [Auto Scaling Group](#auto-scaling-group)
  - [High Availability and Scalability with AWS Auto Scaling Groups](#high-availability-and-scalability-with-aws-auto-scaling-groups)
  - [How Auto Scaling Groups Achieve These Benefits:](#how-auto-scaling-groups-achieve-these-benefits)
  - [Main differences to Azure:](#main-differences-to-azure)
  - [Launch Template](#launch-template)
  - [Create the Auto Scaling Group](#create-the-auto-scaling-group)
  - [Auto Scaling with a Database](#auto-scaling-with-a-database)

<br>

![Diagram 2](images/asg.png)<br>

## High Availability and Scalability with AWS Auto Scaling Groups
- In AWS, achieving both high availability and scalability allows us to ensure that our applications and databases experience minimal downtime and if one area is suffering issues our ASG can delete an unhealthy instance and quickly spin up a new one. 

- Benefits:

  - High Availability: This ensures your application remains accessible to users even during unexpected events like instance failures or increased traffic spikes. Auto Scaling groups contribute to high availability in several ways:
  - Fault Tolerance: Auto Scaling groups can detect unhealthy instances using health checks. When an unhealthy instance is found, it's automatically terminated and replaced with a healthy one, minimizing downtime.
  - Automatic Scaling: During traffic surges, Auto Scaling groups can automatically launch new instances to handle the increased load. This prevents existing instances from becoming overloaded and potentially failing.
  - Multiple Availability Zones (AZs): You can configure Auto Scaling groups to launch instances across multiple AZs within a region. If an AZ outage occurs, your application remains accessible as instances in other AZs continue serving requests.
  <br>
- Scalability: This allows your application to adapt to changing workloads. Auto Scaling groups facilitate scalability by:
  - Automatic Provisioning: Based on predefined scaling policies (e.g., CPU utilization, network traffic), Auto Scaling groups automatically increase or decrease the number of instances in the group. This ensures you have the right amount of resources to handle current demand.
  - Cost Optimization: You only pay for the resources you use. By scaling down during low traffic periods, Auto Scaling groups can help you reduce costs.
  - Horizontal Scaling: Auto Scaling groups enable horizontal scaling, where you add or remove instances to meet demand. This is more efficient than vertical scaling (upgrading existing instances), which can be expensive and disruptive.
<br>

## How Auto Scaling Groups Achieve These Benefits:

1. Define Auto Scaling Group: You configure an Auto Scaling group with the following components:
  - Launch Template: Specifies the AMI (Amazon Machine Image) and configuration for the instances to be launched.
  - Scaling Policies: Define conditions (e.g., CloudWatch alarms based on CPU, memory, or network metrics) that trigger scaling up or down.
  - Health Checks: Monitor the health of your instances to identify and replace unhealthy ones.
  - Target Tracking: Optionally, target specific resource utilization levels (e.g., CPU) to automatically adjust instance count for optimal performance.
<br>

2. Auto Scaling in Action:
   - When demand increases and scaling policies are triggered (e.g., CPU utilization exceeds threshold), Auto Scaling group launches new instances from the Launch Template.
   - New instances undergo health checks. Once healthy, they join the pool and serve requests, distributing the load and improving response times.
   - During low traffic periods, scaling policies might trigger scaling down, terminating instances to avoid unnecessary costs.
   - Health checks continuously monitor instances. If an instance becomes unhealthy (e.g., system crash), it's automatically terminated and replaced with a healthy one.

## Main differences to Azure:
  - Launch template
  - Seperate Subnets

## Launch Template
1. We need to create a launch template first:<br>
![Launch template set up 1](images/launch-template-1.png) <br>
2. Make sure you add the ami we created earlier:<br>
![Launch template set up 2](images/launch-template-2.png) <br>
3. Add the correct Key Pair: <br>
![Launch template set up 3](images/launch-template-3.png) <br>
4. Choose the correct security group for our instances needs:<br>
![Launch template set up 4](images/launch-template-4.png) <br>

## Create the Auto Scaling Group
1. Give it an appropriate name and select our Launch Template: <br>
![Step 1](images/asg1.png) <br>
2. We are using a default VPC but selecting AZ and subnets:<br>
![step 2](images/asg2.png)<br>
3. Attach a new load balancer: <br>
![step 3](images/asg3.png)<br>
  1. New Load Balancer set up:<br>
    ![step1](images/lb1.png)<br>
    ![step2](images/lb2.png)<br>
4. No VPC Lattice Service:<br>
   ![step 4](images/asg4.png)<br>
5. Turn on the load balancing health checks:<br>
   ![step 5](images/asg5.png)<br>
6. Configure your group size with desired number of instances:<br>
   ![step 6](images/asg6.png)<br>
7. Set your Automatic scaling policy based on the appropriate metric (we selected CPU):<br>
   ![step 7](images/asg7.png)<br>

## Auto Scaling with a Database

- Set up the Database as per out script: [Database script](../aws_intro/install_sparta_db.sh)

- Then review the launch template and edit it so it can set up the app using our AMI and then we add the following User Data:

`#!/bin/bash
export DB_HOST=mongodb://<Private-DB-IP>:27017/posts
tech257-sparta-app/app
node seeds/seed.js
pm2 kill app
pm2 start app.js`


- The ASG should be set up the same as above, but with the correct Launch Template.