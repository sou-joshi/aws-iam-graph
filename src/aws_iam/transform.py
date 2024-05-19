def transform_iam_data(users, roles, policies):
    nodes = []
    relationships = []

    for user in users['Users']:
        nodes.append({'id': user['UserId'], 'type': 'User', 'name': user['UserName']})
    
    for role in roles['Roles']:
        nodes.append({'id': role['RoleId'], 'type': 'Role', 'name': role['RoleName']})
        
    for policy in policies['Policies']:
        nodes.append({'id': policy['PolicyId'], 'type': 'Policy', 'name': policy['PolicyName']})
    
    # Add relationships logic here
    
    return nodes, relationships
