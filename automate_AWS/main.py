import boto3


client = boto3.client('ec2', aws_access_key_id="access_key", aws_secret_access_key="secret_key", region_name="us-east-1")

try:
    region_instance_status = client.describe_instance_status()
    region_running_instances = len(region_instance_status["InstanceStatuses"])
    region_instance_ids = [region_instance_status["InstanceStatuses"][i]["InstanceId"] for i in range(region_running_instances)]
    print region_running_instances
    print region_instance_ids
except Exception as e:
    print "Error: {}".format(e)
