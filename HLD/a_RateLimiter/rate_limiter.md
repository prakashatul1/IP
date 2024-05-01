Requirements
-----------------
- availability
- low latency

- rule for each api
- not on users

- 1 rule = 250 bytes approx  
- 1 million api * 250 bytes = 250 MB 
 
- can be stored in disk

rule schema
------------------
- id  
- uid  
- url  
- time (minute/sec/hour)  
- requests (10/100/1000) 
-------------------
eg. rate limit = 5 requests/min

Algorithms
------------

token bucket
--------------------
store 
- timestamp - each user request + no if token available
- new request - check
  - if minute(current request) = minute(previous request)
    - reduce token count
  - if new minute 
    - refill bucket and use token
--------------------
schema
--------------------
uid_route : 11.01:05  4 (no of available tokens)  
uid_route : 11.01:10  3  
uid_route : 11.02:05  4

leaky bucket
----------------------
- user request
  - goes into a queue/bucket of capacity eg:5  
  - there is a constant leak in queue
    - rate of 5 requests/min 
    - request removed and processed
    - if bucket is full 
      - requests dropped
      
tradeoff
-------------

disadv
---------
- if rate of requests is less
- it will be take lot of time

adv
-----
- no storage is required


fixed window
------------------------
- Store 
  - count of requests
  - if threshold reached requests are dropped

- key value is reset after every minute
- disadv - spike at stand and end of window

------------------------
schema
------------------------
uid_route : 1  
uid_route : 8

sliding window
--------------------------
- store
  - timestamps of request in array
  - fetch subarray of timestamps (eg last 1 min)  
  - if threshold reached
    - request dropped
  - else
    - request processed
    - added to array
    - remove old timestamps

disadv
---------------------------
- takes lot of memory for high tps rate limit
- 1 million req/sec - array size 1 million

----------------------------
schema
----------------------------
uid_route : [t1, t2, t3] # max size = 5, rate limit 5/min  
uid_route : [t2, t3, t4] # proportional to number of requests  

sliding window memory optimised
----------------------------
- store 
  - count and timestamp in a hashset
  - max hashset size timestamps in unit time 
  - eg : 1 million req per min
  - max size - no if timestamps in a minute
----------------------------
schema
----------------------------
uid_route : [(t1,2), (t2,10), (t3,5)]


Solution
--------------------------
- Fail Open - even if rate limiter is down requests goes  
- Fail closed -  if rate limiter is down system will not process requests

- fail open is recommended