import boto3
import yaml

def get_iam_data():
    with open('config/config.yaml') as f:
        config = yaml.safe_load(f)
        
    session = boto3.Session(
        aws_access_key_id=config['aws']['access_key'],
        aws_secret_access_key=config['aws']['secret_key'],
        region_name=config['aws']['region']
    )
    iam = session.client('iam')
    
    users = iam.list_users()
    roles = iam.list_roles()
    policies = iam.list_policies(Scope='Local')
    
    return users, roles, policies
