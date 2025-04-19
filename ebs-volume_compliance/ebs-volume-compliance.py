import boto3


def get_volume_id_from_arn(volume_arn):
    # Split the ARN using ':' as the separator
    arn_parts = volume_arn.split(':')
    # The volume ID is the last part of the ARN
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id


def lambda_handler(event, context):
    # Extract the volume ARN from the event
    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')

    # Modify the volume to gp3
    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )
    print(f"Volume {volume_id} successfully converted to gp3.")