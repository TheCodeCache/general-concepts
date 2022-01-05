# Partition and Bucket — 

best practice:  

>**`Partitioning should only be used with columns that have a limited number of values`**.  
**`Bucketing works well when the number of unique values is large`**.  
Columns which are used often in queries and provide high selectivity are good choices for bucketing.  

Spark tables are bucketed store metadata about hoe they are bucketed and sorted, which optimizes:  

1. Queries on bucketed values (Spark 2.4 supports bucket pruning)
2. Aggregations on bucketed values (wide transformations)
3. Joins on bucketed values

