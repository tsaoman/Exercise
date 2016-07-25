import random

#variable initialization

#time variable t
t = 0

#system state variables
pos = 0 #position / current floor variable (1,12)
direction = 0 #(-1,0,1) direction variables
destinations = 0 #destination variable queue/stack
requests = 0 #list of floors requested

#counter variables
Nr = 0 #total numebr of requests
T = 0 #total time waited

n = 0 #current number of people in elevator
NA = 0 #total number of arrivals
ND = 0 #total number of departures

tAr = 0 #arrival time of the elevator request
tAo = 0 #arrival time of the elevator reaching the person and the doors opening
tD = #arrival time of elevator at destination floor and departure time of person

#event list
Fr = [] #requested floors (outside of elevator)
Fd = [] #destination floors (inside of elevator)
