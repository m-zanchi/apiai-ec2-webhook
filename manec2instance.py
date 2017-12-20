import sys
import boto3
from botocore.exceptions import ClientError

instance_id = 'i-0a656796258609de1'
action = 'OFF'

ec2 = boto3.client('ec2',region_name='eu-west-1',aws_access_key_id='AKIAJWTYUZFM62WAD7YQ',
    aws_secret_access_key='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')


if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances witout dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)