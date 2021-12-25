# REST - REpresentational State Transfer: 

REST is a standard and REST APIs can be implemented over different protocols.  
In most cases, REST APIs are implemented over HTTPS.  

`APIs` are a way to transfer data from one node to another 

REST APIs are all about transferring data from one layer of system to another layer of system.  

![image](https://user-images.githubusercontent.com/26399543/147391803-611567d5-ca2f-4660-92f4-8fc1c375b697.png)

**`Resources`:**  
For ex: customer-data, or customer-oreders etc.

**`Representation`:**  

![image](https://user-images.githubusercontent.com/26399543/147391971-6a5c7e0b-87b9-4353-98a7-01f80c3adfbd.png)

**`Representational State`:**  

![image](https://user-images.githubusercontent.com/26399543/147392026-1ac56885-7afe-49bd-9c74-39a365027bfe.png)

REST Apis are all about:  
1. managing the `Resources` (creating/updating/deleting them)
2. How to `represent` the resources on different layers,
3. How to `pass one representational state` from one layer to another layer

`URI = API Endpoint`  

PATH parameter:  
Changing the path parameter will change the resource that we're pointing.  
![image](https://user-images.githubusercontent.com/26399543/147392112-a5ca405e-eb69-46fa-93ed-513bc53e95a0.png)

Query Parameter:  
![image](https://user-images.githubusercontent.com/26399543/147392132-911cc0c8-e555-474c-9df9-027d60688395.png)

# Headers In REST Api - 

There're 4 types of headers, and they can be used interchangeably where ever applicable.  
- Request Headers (Host, user-agent, Referer, Connection, Accept-Language etc.)
- Response Headers (Connection: keep-alive, Date: 26 12 2021, Server: Apache/2.4.1 Unix, Content-Type: text/html, transfer-encoding: chunked etc.)
- Payload Headers (order_num: 1234 etc.)
- Representation Headers (content-type, content-length, content-range, content-encoding, content-location etc.)
- Custom Headers (Authorization headers etc.)

Headers are `key-value` pairs.  

Now,  
How to design API that display and filter through millions of products??  
Answer: Filtering and Pagination  

**Filters:**  
Filters are very powerful optimization techniques,  
it saves a lot of n/w bandwidth, reduces load on servers as well as client side.  
use query parameter: `?name=xyz&order=microwave` etc.  

**Pagination:**  
We should still put a limit or a cap on max rows on server to be send back as response to client,  
o'wise the purpose of optimization could still be defeated if we increase the limit too high.  
use query parameter: `?limit=20&offset=0` or `?limit=20&offset=20` or `?limit=20&offset=40` etc.  

`Filtering and Pagination concepts go hand in hand with concepts of partitioning an bucketing in Hive/Spark`

**Reference:**  
1. https://www.youtube.com/watch?v=ST8XxjOTIsg

