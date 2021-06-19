import boto3
from typing import Dict, List

# Create Connection to AWS IAM
iam_client = boto3.client('iam',aws_access_key_id="<Add your Key ID>",aws_secret_access_key="<Add your Access Key>")

# Get Users information - Policies and Groups
def get_user_info():
    users = iam_client.list_users()
    for key in users['Users']:
        print(key['UserName'])
    # List of Policy attached to an user
    for key in users['Users']:
        List_of_Policies =  iam_client.list_user_policies(UserName=key['UserName'])
        print(List_of_Policies)
        for key in List_of_Policies['PolicyNames']:
            print(key['PolicyName'])
    # List of Groups attached to an user
    for key in users['Users']:
        List_of_Groups =  iam_client.list_groups_for_user(UserName=key['UserName'])
        for key in List_of_Groups['Groups']:
            print(key['GroupName'])

# Get Roles
def get_role_names() -> List[str]:
    roles = []
    role_paginator = iam_client.get_paginator('list_roles')
    for response in role_paginator.paginate():
        response_role_names = [r.get('RoleName') for r in response['Roles']]
        roles.extend(response_role_names)
    return roles

# Get Policies 
def get_policies_for_roles(role_names: List[str]) -> Dict[str, List[Dict[str, str]]]:
    """ Retrieve the role name and the attached policy information as a dict """
    policy_map = {}
    policy_paginator = iam_client.get_paginator('list_attached_role_policies')
    for name in role_names:
        role_policies = []
        for response in policy_paginator.paginate(RoleName=name):
            role_policies.extend(response.get('AttachedPolicies'))
        policy_map.update({name: role_policies})
    return policy_map


if __name__ == '__main__':
    get_user_info()
    role_names = get_role_names()
    attached_role_policies = get_policies_for_roles(role_names)
    print(role_names)
    print(attached_role_policies)
