Requirements
------------
Functional Requirements
--------------
create a short url that should redirect to long url  
create a hash with domain name that maps to long url and store it

can 2 long url points to single url ?  
no because ownership lies with user  
user can delete url and set time to expire

NFR
-------------
what is the scale
write per month or reads per month
ratio of read vs write
eg read:write = 100:1 

Solution
--------------------
hash char ?

if it is 8 char base 62 hash char  
count(0-9)  + count(a-z) + count(A-Z)  = 62  
eg : bit.ly/1why6shG

it could store 62^8 urls
60^8 ~ 60^2^4 ~ 3600^4 ~ 1 trillion url

eg: 1 billion writes / month = 12 billion url a year
then 400 writes/sec and 40000 reads/sec

Throughput
--------------------
1 machine 4 cores - 4 * 100 threads = 400 req/sec * 30% ~ 120 ~ 100 req/sec
to handle 400 writes/sec we need to add 4 machines 
to handle 40000 reads/sec we need to 40 machines

storage
---------------------
if 1000 bytes per url of storage is required in database
1000 * 1 billion =  1 trillion = 1 TB 

do we need acid property ? nosql
- no joins or complex query
- base property gives eventual consistency

schema
--------------------
uid
long
hash
expiration date

points to note
--------------------
read
------------

cache the read data for faster response  
LRU is preferred over LFU  
because there can be urls with high hits for a time duration in past
cache could be shared

get request to short url will return 301
response headers location will have long url
browser will redirect


write
------------
If we generate hash on every request there could be collision 
two long url can point to same 8 char hash 

generate all possible string of length 8 (hashes)   
or eventually generate them and store in database

url generator service will fetch some of the available keys  
and keep in cache  
when write request comes it assigns first available key to long url  
and mark hash as occupied in database

we can start reusing keys after expiring

clean up service
---------------
a worker can read the url database and mark all hash as free
which are expired

while fetching key there could be race condition
we can use atomicity and isolation in acid here (mysql)

partitioned database by uid

we are using hash stored in cash and marking it occupied in db
ok locking in cache to avoid race condition 

