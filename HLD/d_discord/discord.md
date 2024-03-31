functional requirements
----------
servers
channel
unread messages
mentions
dm

NFR
-----------
minimal latency for chat
availability

5 million daily active users
50 million msg per day
20 thousand users per server
20 thousand msg/day
2 kilobytes per msg

we want to read only recent msgs

Solution
---------------

web socket
so that people are receiving msg   
at the same time they are sent
reduce latency

http
to receive channel msgs and 
notification count

Interface
---------------
sendMsg(body) 
viewChannel(channelName) - paginated data
- when was the last msg read
- count of unread msg

Database Design
-----------
mysql

Messages Table
----------------
id
uid
mention_id
server_id
channel_id (sharding key)
sent_at (index) order by

UserActivity Table
----------------
id
uid
server_id
channel_id
last_read_at

example query fetch unread messages in channels
----------
select * from messages
where channel_id='example'
and sent_at >
(select last_read_at
from UserActivity 
where uid='daemonconj')
limit 10

after running query update UserActivity.last_read_at

for unread mentions in all channels
-----------------------
since we partitioned data by channel id
but all mentions comes from different channels 
would take lot if time to join data from different shards

Notification Count
---------------------------
everytime a user1 mention user2
we will update notification count for user2
this data will be stored in cache

if we want to repopulate in cache we can check  
all the msg since last activity

schema
--------------
mention_id+channel_id+server_id : Count

things to consider
-------------
discord started with mongodb
but later when data grew they use cassandra
because positioning in mongo was not very simple and stable

we can also store msg id as increasing number
that will help sort msgs according to time

websockets explained
-------------------
all users are connected to web socket handler
web socket manager stores which user is connected to which handler
it uses redis to store 

websocket cache will store  
u1: websocket1  
websocket1 : [u1, u3]

websocket connection
are bi directional connection

web socket can also cache mapping

if user is not online and msg is sent to him  
when user comes back online it can make a http request  
to get notifications and msgs in mentions and channels  
or interact with websocket as well

message service
-----------------------
it will give api to get messages with different filters