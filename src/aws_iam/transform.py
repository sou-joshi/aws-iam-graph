def transform_iam_data(users, roles, policies, groups, user_policies, role_policies, group_policies):
    nodes = []
    relationships = []

    for user in users['Users']:
        nodes.append({'id': user['UserId'], 'type': 'User', 'name': user['UserName']})
    
    for role in roles['Roles']:
        nodes.append({'id': role['RoleId'], 'type': 'Role', 'name': role['RoleName']})
        
    for policy in policies['Policies']:
        nodes.append({'id': policy['PolicyId'], 'type': 'Policy', 'name': policy['PolicyName']})
    
    for group in groups['Groups']:
        nodes.append({'id': group['GroupId'], 'type': 'Group', 'name': group['GroupName']})

    for user, policies in user_policies.items():
        for policy in policies['PolicyNames']:
            relationships.append({'from_id': user, 'from_type': 'User', 'to_id': policy, 'to_type': 'Policy', 'type': 'HAS_POLICY'})
    
    for role, policies in role_policies.items():
        for policy in policies['PolicyNames']:
            relationships.append({'from_id': role, 'from_type': 'Role', 'to_id': policy, 'to_type': 'Policy', 'type': 'HAS_POLICY'})
    
    for group, policies in group_policies.items():
        for policy in policies['PolicyNames']:
            relationships.append({'from_id': group, 'from_type': 'Group', 'to_id': policy, 'to_type': 'Policy', 'type': 'HAS_POLICY'})
    
    return nodes, relationships
