Functional requirement
----------------
follow other user
create tweet
viewing a newsfeed

tweet can have img and vdos ?

NFR
---------------
how many users ? 500 Million
daily active users -> half of daily active users

Solution
-----------------
eg : 200 Million  
each user will view around 100 tweets  
20 billion tweet view per day   
1 mb tweet   
1 mb * 20 billion = 20 pb data read per day  
50 million created tweets per day  
eventual consistency is enough  
1 person follows 100 people  
1 person can have 100 million followers as well.  

for storing tweets and follows we can choose relational db
because we need to have joins and data is relational

object storage to for storing media
distribute based on pull based cdn network, 
india tweet views vs USA tweet views


Interfaces
-------------------
createTweet(text, media, uid)
getFeed(uid)
follow(uid, followee_id)

Database
----------------------

Tweet table
-----------------
tweet_id
timestamp
creator_uid
content

Follows Table
-------------------
follower_id
followee_id

index based in follower_id
all people that this guy follow will be grouped together
 
50GB of data written per day not including media
1.5 TB per month
18 TB per year
500 writes per second

NewsFeed
-------------------
bottleneck is so many reads
- read only replicas
- if there is a lag in syncing replicas for a few seconds

Sharing shard key
-------------------------
- based on user id
- break data so user should be able to  
get all data in one shard
- all tweets that this user is following
- so all user that this user is following  
should also be on same shard
- order the tweets based on time
- but we still might need to join data   
from different shard would take a lot of time

all popular tweets will be stored in cache
--------------------------
might use LRU
people want to see latest tweets

we still can come to a situation where  
all tweets are not cached for a user
it still might go to disk read

latency is still a problem

generate newsfeed of all users asynchronously
----------

for every single user
half are daily active users

or generate for users who are active for last 30 days

for every tweet worker will add tweet
in newsfeed of all follows say 100 followers

for celebrity however this would not be feasible
since it will have millions of followers

so when a celebrity tweets its tweet will be written in celeb tweet cache  
when a user fetches its feed from feed cache   
app server will add celebrity tweet in it and update user feed

when a user follows a new user   
we add a msg to message queue  
worker will update the feed  
might take a few seconds

paginate feed cache



