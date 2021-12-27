# commands - 

**`lsof`**:  
  We can use the Linux `lsof` command to capture the number of open connections on a given port port for ex: `443`  
  the cmd to be used as follows:  
  `lsof -i tcp:443`  

  usecase - when we upload a big file to `Amazon S3`, it uploads in chunks (using `multi-part` upload option),  
  so, `lsof` cmd will tell us how many connections are used to upload in chunks at a given port #  

