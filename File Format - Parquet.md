# Parquet File Format - 

**Introduction & Benefits** - 

Parquet is a columnar compressed storage file format  
that is designed for querying large amounts of data, regardless of the data processing framework, data model, or prog. language.  

Compared to common raw data log formats such as CSV, JSON, or TXT format,  
Parquet can reduce the required storage footprint, improve query performance significantly,  
and greatly reduce querying costs for AWS services, which charge by amount of data scanned.  

**Amazon Experiments** -  
comparing CSV and Parquet formats using one TB of log data stored in CSV format to Parquet format showed the following:  

Space savings of `87%` with Parquet (`1 TB of log data stored in CSV format compressed to 130 GB with Parquet`)  

A query time for a representative Athena query was `34x` faster with Parquet (`237 seconds for CSV versus 5.13 seconds for Parquet`),  
and the amount of data scanned for that Athena query was 99% less (`1.15TB scanned for CSV versus 2.69GB for Parquet`)  

The cost to run that Athena query was 99.7% less (`$5.75 for CSV versus $0.013 for Parquet`)  

Parquet has the additional benefit of being an open data format,  
that can be used by multiple querying and analytics tools in a data lake built on Amazon S3,  
particularly Amazon Athena, Amazon EMR, Amazon Redshift, and Amazon Redshift Spectrum.  


**Reference:**  
1. https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.html

