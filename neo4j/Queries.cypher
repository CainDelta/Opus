

///LOAD TRANSACTIONS
LOAD CSV WITH HEADERS FROM 'file:///blocks.csv' AS row
MERGE (b:Block {blockHash: row.BlockHash,BlockHeight:row.BlockHeight,pow:row.Pow})
return b;

//lOAD RELATIONSHIPS
LOAD CSV WITH HEADERS FROM "file:///blocks.csv" AS row
//look up the two nodes we want to connect up
MATCH (b1:Block {blockHash:row.BlockHash}), (b2:Block {blockHash:row.BlockPrevHash})
//now create a relationship between them
CREATE (b1)<-[:chain]-(b2);

//LOAD TRANSACTIONS IN BLOCKS
LOAD CSV WITH HEADERS FROM 'file:///transactions_blocks.csv' AS row
MERGE (t:TX {txID: row.ID,Block:row.BlockHash})
MERGE(b2:Block {blockHash:row.BlockHash})
CREATE(t)-[:inblock]->(b2)
return t;

//LOAD TX
LOAD CSV WITH HEADERS FROM 'file:///master_trans.csv' AS row
MERGE (o:Output {outID: row.ID})
ON CREATE set o.sig=row.Signature,o.value=row.Value
MERGE(a:Address {address:row.PubKeyHash})
CREATE(o)-[:lockedby]->(a)
return a;



LOAD CSV WITH HEADERS FROM 'file:///master_trans.csv' AS row
with row where row.Txid is not null
MATCH (o:Output {outID: row.ID})
MATCH(t:TX {txID:row.Txid})
CREATE(o)-[r:in]->(t)
return o,r,t;

LOAD CSV WITH HEADERS FROM 'file:///master_trans.csv' AS row
with row where row.Txid is not null
MATCH (o:Output {outID: row.ID})
MATCH(t:TX {txID:row.TransactionID})
CREATE(t)-[r:output]->(o)
return o,t,r;
