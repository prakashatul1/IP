functional Requirement
------------------------
- navigate from src to destination
- walking
- driving
- make route as short as possible
- make route as fast as possible if even if longer
- device will have gps
- geocoding is way to convert address into longitude and latitude
- source and destination into integers
- track user location
- ETA
- we have map data in TBs

NFR
----------------
- a billion daily active users
- accuracy - incorrect route
- availability and tolerated
- high latency for generating route is possible
- high latency in fetching location not possible

Solution
----------------------

data can be stored in a map
physical address pointing to lat long
 
- we can save data in graph db
- we can use quadtree or geohashing to do spacial indexing
- to be able to find get a square size chunk of lat long from graph db
- given two points find the shortest distance use dijkstra algorithm
- distance between two squares
- cache can store data related to popular routes
- or common potion of certain routes

route service
--------------
- finding optimal route based on shortest path
- also based on traffic

location service
-----------------
- it can read real time data from device gps
- and store data in elastic time series data
- to find traffic on each day each route
- for real time traffic it can send data to kafka
- traffic service can read data from kafka
- it also connect with websocket to give user information about traffic

schema
---------
- uid
- timestamp
- lat long


traffic service
---------------------
- it was transformed real time data for traffic
- route service will call this traffic data to identify traffic
- from node1 to node2 it can add weights to route path

----------
- we have picture of the map