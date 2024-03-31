Functional requirement
-----------------
upload
view
view count > upload count
search
recommended
comment

if user is uploading vdo internet connection fail
now can he resume from the last upload

NFR
-------------
reliability -> vdo cant be corrupted or deleted
scale -> 1000 concurrent reads

1 billion daily active users
each users watching 5 vdos a day

if read write ratio is 100:1

total vdo upload a day 50 million

top 5% videos get 90 percent of the views

favor availability or consistency
if feed is updated with a few seconds delay

minimise latency

interface
-------------
upload(title, description, videos, tags, uid)

solution
------------------
person uploads a vdo it get saved in s3  
and metadata is stored in mongodb
as we need user data joins with vdo data
we can de normalise and store

if a person updated the profile pic
we can update profile pic for all vdos
async

youtube encode and compress uploaded vdo  
which can take upto minutes

capacity planning
-----------------------
encoding
------------
50 million / uploads per day
500 vdo/sec
1 minute to encode a vdo

how muc workers ?
500*60 = 30k vdos = 30k workers

watching vdos
----------------
loading the vdo in small chunks
what protocol should be we used : udp
vdo streaming

ratelimiter in load balancer for writing

recommendation each person store vdo tags
and show popular vdo in that tag and subscription

youtube started in 2005 nosql was not der
youtube is using mysql
vitess engine for sharding



