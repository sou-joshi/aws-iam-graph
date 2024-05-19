from neo4j_db.neo4j_connection import Neo4jConnection

def load_to_neo4j(nodes, relationships):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="password")
    
    for node in nodes:
        query = f"CREATE (n:{node['type']} {{id: '{node['id']}', name: '{node['name']}'}})"
        conn.query(query, parameters={})
    
    for rel in relationships:
        query = f"MATCH (a:{rel['from_type']} {{name: '{rel['from_id']}'}}), (b:{rel['to_type']} {{name: '{rel['to_id']}'}}) CREATE (a)-[r:{rel['type']}]->(b)"
        conn.query(query, parameters={})

    conn.close()
