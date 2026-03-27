from fastapi import APIRouter
from sql_blocks import detect

router = APIRouter()


@router.post('/optimize')
def optimize(text: str):
    """
    Applies optimization rules to query 
    syntax to improve SQL efficiency.
    """
    query = detect(text)
    return {
        'result': str( query.optimize() )
    }

@router.post('/translate')
def translate(text: str, language: str):
    """
    Translates the query to another language or database
    (mongoDB, Oracle, Pandas, Sql Server, Polars, pySpark, PostgreSql...)
    """
    query = detect(text)
    return {
        'result': str( query.translate_to(language) )
    }
