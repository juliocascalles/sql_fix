from fastapi import APIRouter, HTTPException
from sql_blocks import detect

router = APIRouter()
ERROR_MESSAGE = '''
    The query could not be processed. Please submit a valid query
    in one of these languages: SQL, Cypher, MongoDB or Neo4J.
'''


@router.post('/optimize')
def optimize(text: str):
    """
    Applies optimization rules to query 
    syntax to improve SQL efficiency.
    """
    try:
        query = detect(text)
        return {
            'result': str( query.optimize() )
        }
    except:
        raise HTTPException(status_code=400, detail=ERROR_MESSAGE)

@router.post('/translate')
def translate(text: str, language: str):
    """
    Translates the query to another language or database
    (mongoDB, Oracle, Pandas, Sql Server, Polars, pySpark, PostgreSql...)
    """
    try:
        query = detect(text)
        return {
            'result': str( query.translate_to(language) )
        }
    except:
        raise HTTPException(status_code=400, detail=ERROR_MESSAGE)
