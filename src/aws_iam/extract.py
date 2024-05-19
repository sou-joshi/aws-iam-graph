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
    groups = iam.list_groups()
    user_policies = {user['UserName']: iam.list_user_policies(UserName=user['UserName']) for user in users['Users']}
    role_policies = {role['RoleName']: iam.list_role_policies(RoleName=role['RoleName']) for role in roles['Roles']}
    group_policies = {group['GroupName']: iam.list_group_policies(GroupName=group['GroupName']) for group in groups['Groups']}
    
    return users, roles, policies, groups, user_policies, role_policies, group_policies
