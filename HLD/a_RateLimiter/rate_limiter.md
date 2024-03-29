For rate limiting user we need rule.
Suppose if 1 billion user still no of rules will not depend on users. 
we will need to store rule for each api.

1 rule = 250 bytes approx
1 million api * 250 bytes = 250 MB

250 is not that much
We will store data in disk(mysql) to make it persistent

rule schema
------------------
id 
uid
url
time (minute/sec/hour)
requests (10/100/1000)
-------------------

Now on rules we can apply 
4 different types of rate limiting algorithm.
eg. rate limit = 5 requests/min

token bucket
--------------------
For each user request we store timestamp and total number
of tokens available. 
now on another request we check if same minute then reduce token
if new minute 
--------------------
schema
--------------------
uid_route : 11.01:05  4 (no of available tokens)
uid_route : 11.01:10  3
uid_route : 11.02:05  4

leaky bucket
----------------------
Each user request goes into a queue/bucket of capacity 5
there is a constant leak rate of 5 requests/min at which user requests are 
removed from queue and processed.
if bucket is full requests will be dropped
tradeoff if rate of requests is less if will be take lot of time
no storage is required

fixed window
------------------------
For each request we store the count of requests
if it reaches the threshold requests are dropped
key value is reset after every minute
------------------------
schema
------------------------
uid_route : 1
uid_route : 8

sliding window
--------------------------
for each request we store the timestamps
for every new request we fetch a window of timestamps as per rule
here we fetch last for 1 min window count and check if it has reached threshold 
and remove others timestamps from storage
it will take more memory
----------------------------
schema
----------------------------
uid_route : [t1, t2, t3] # max size = 5, rate limit 5/min
uid_route : [t2, t3, t4] # proportional to number of requests

sliding window memory optimised
----------------------------
for each request we store the count of requests along with timestamp in a hashset
this way we can make sure size of array is reduced to timestamp in a unit time
here size will be 60 as there are 60 seconds ina minute
----------------------------
schema
----------------------------
uid_route : [(t1,2), (t2,10), (t3,5)]


