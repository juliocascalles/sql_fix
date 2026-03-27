from fastapi import APIRouter, HTTPException
from sql_blocks import CypherParser, Select, join_queries


router = APIRouter()


@router.post('/join')
def join(cypher_script: str):
    """
    Join two tables (or more) in a query using the _cypher language_.
    Example: `product(id) <- sales(pro_id)`
    > This will generate:  SELECT ... FROM sales LEFT JOIN product ...
    """
    try:
        q1, q2 = CypherParser(cypher_script, Select).queries
    except:
        raise HTTPException(
            status_code=400, detail='''
            It was not possible to extract two queries from cypher script.
            '''
        )
    return {
        'result': str( join_queries([q1, q2]) )
    }

@router.post('/split')
def split_queries(text: str):
    try:
        q1, q2 = Select.parse(text)
    except:
        raise HTTPException(
            status_code=400, detail='''
            It was not possible to extract two queries from SQL script.
            '''
        )
    return {
        q.table_name: str(q) for q in [q1, q2]
    }
