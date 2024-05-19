from aws_iam.extract import get_iam_data
from aws_iam.transform import transform_iam_data
from aws_iam.load import load_to_neo4j

def run_etl():
    users, roles, policies = get_iam_data()
    nodes, relationships = transform_iam_data(users, roles, policies)
    load_to_neo4j(nodes, relationships)

if __name__ == "__main__":
    run_etl()
