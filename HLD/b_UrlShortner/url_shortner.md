Requirements
------------
Functional Requirements
--------------
- short url redirect to long url  
- create a hash  
- that maps to long url
- store hash : long_url mapping

2 same long url cant have same hash

NFR
-------------
- scale ?
- scale ? 
- write per month or reads per month
- ratio of read vs write
eg read:write = 100:1 

Solution
--------------------
- hash char size

- if 8 char base 62 hash || count(0-9)  + count(a-z) + count(A-Z)  = 62
- 1 trillion url
- 62^8 

eg : bit.ly/1why6shG
eg : 60^8 ~ 60^2^4 ~ 3600^4 ~ 1 trillion url

no of writes = no of url

eg : 1 billion writes / month , then 400 writes/sec and 40000 reads/sec

Throughput
--------------------
- 1 machine 4 cores
- 4 * 100 threads
- 400 req/sec * 30% 
- 120
- 100 req/sec

to handle 400 writes/sec we need to add 4 machines 
to handle 40000 reads/sec we need to 40 machines

storage
---------------------
- if 1000 bytes storage per url
  - 1000 * 1 billion =  1 trillion = 1 TB

- do we need acid property ? NOO
  - no joins or complex query
  - base property gives eventual consistency
  - nosql db

schema
--------------------
uid
long
hash
expiration date

solution
--------------------
read
------------

- cache   
- LRU is preferred over LFU (due to spike of request in past timestamp)  
- can be shared on uid 


-  get request to short url
    - return 301
    - response headers location - long url
    - browser will redirect


write
------------

- Generate all possible string of length 8 (hashes) and store it before
- generate some and do this periodically

- If generate hash on every request
  - there could be collision 
  - two long url can point to same 8 char hash 

- url generator service
  - fetch available keys  
  - keep in cache
- write request (assigns hash) 
- mark hash occupied 
- mark available after expiry

clean up service
---------------
- worker 
  - read the url database 
  - if expired
    - - mark all hash as free

Problems
---------------------
- race condition read key
we can use atomicity and isolation in acid here (mysql)

partitioned database by uid

- fetch hash stored in cache
- mark it occupied in db

ok locking in cache to avoid race condition 

