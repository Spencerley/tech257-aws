# Monitoring and Alert Management

- [Monitoring and Alert Management](#monitoring-and-alert-management)
  - [Creating a Dashboard](#creating-a-dashboard)
  - [Creating an Alert](#creating-an-alert)
    - [Setting up a CPU usage alarm using the AWS Management Console](#setting-up-a-cpu-usage-alarm-using-the-aws-management-console)

## Creating a Dashboard
- On the instance click monitoring
- Click add to dashboard 
- Create new <br>
![add to dashboard](images/ad-to-dashboard.png)
![dashboard](images/Dashboard.png)<br>

## Creating an Alert
### Setting up a CPU usage alarm using the AWS Management Console
1. To create an alarm based on CPU usage Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose Alarms, All Alarms.
3. Choose Create alarm.
4. Choose Select metric.
5. In the All metrics tab, choose EC2 metrics.
6. Choose a metric category (for example, Per-Instance Metrics).
7. Find the row with the instance that you want listed in the InstanceId column and CPUUtilization in the Metric Name column. Select the check box next to this row, and choose Select metric.
8. Under Specify metric and conditions, for Statistic choose Average, choose one of the predefined percentiles, or specify a custom percentile (for example, p95.45).
9. Choose a period (for example, 5 minutes).
10. Under Conditions, specify the following:
    1. For Threshold type, choose Static.
    2. For Whenever CPUUtilization is, specify Greater. Under than..., specify the threshold that is to trigger the alarm to go to ALARM state if the CPU utilization exceeds this percentage. For example, 70.
    3. Choose Additional configuration. For Datapoints to alarm, specify how many evaluation periods (data points) must be in the ALARM state to trigger the alarm. If the two values here match, you create an alarm that goes to ALARM state if that many consecutive periods are breaching.
    4. To create an M out of N alarm, specify a lower number for the first value than you specify for the second value. For more information, see Evaluating an alarm.
    5. For Missing data treatment, choose how to have the alarm behave when some data points are missing. For more information, see Configuring how CloudWatch alarms treat missing data.
    6. If the alarm uses a percentile as the monitored statistic, a Percentiles with low samples box appears. Use it to choose whether to evaluate or ignore cases with low sample rates. If you choose ignore (maintain alarm state), the current alarm state is always maintained when the sample size is too low. For more information, see Percentile-based CloudWatch alarms and low data samples.
11. Choose Next.
12. Under Notification, choose In alarm and select an SNS topic to notify when the alarm is in ALARM state
13. To have the alarm send multiple notifications for the same alarm state or for different alarm states, choose Add notification.
14. To have the alarm not send notifications, choose Remove.
15. When finished, choose Next.
16. Enter a name and description for the alarm. Then choose Next.
17. The name must contain only UTF-8 characters, and can't contain ASCII control characters. The description can include markdown formatting, which is displayed only in the alarm Details tab in the CloudWatch console. The markdown can be useful to add links to runbooks or other internal resources.
18. Under Preview and create, confirm that the information and conditions are what you want, then choose Create alarm.
19. Trigger a test alert and you’ll receive and email like this: <br>
     ![alert email](images/alert-email-1.png) <br>
     ![alert email part 2](images/alert-email-2.png)