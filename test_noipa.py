"""
This example shows how to fetch NoiPA Open Data, for example

# Numero di amministrati per comune di servizio

For more possible queries see https://sparql-noipa.mef.gov.it/sparql
"""
import sparql


ENDPOINT = 'https://sparql-noipa.mef.gov.it/endpoint'

sparql_client = sparql.Service(ENDPOINT)

statement = """
PREFIX geonames:<http://www.geonames.org/ontology#>
SELECT ?provincia ?uri_comune ?comune SUM(?number) as ?amministrati
WHERE {
  ?entry npont:hasTime ?time .
  ?time npont:temporalID ?ti. FILTER( ?ti=202101 ) 
  ?entry a npont:EntryAmministrati .
  ?entry npont:hasPlace ?uri_comune .
  ?uri_comune geonames:locatedIn ?provincia .
  ?uri_comune rdfs:label ?comune .
  ?entry npont:howMany ?number .
}
ORDER BY DESC(?amministrati)
"""

result = sparql_client.query(statement)

for row in result.fetchall():
    values = sparql.unpack_row(row)
    print (f'Comune: {values [2]} - Amministrati: {values[3]}')
