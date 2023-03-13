# Shoreline_Challenge
## Challenge
Let's build a social network. 


In this social network, each user has friends.


A chain of friends between two users, user A and user B, is a sequence of users starting with A and ending with B, such that for each user in the chain, ua, the subsequent user, ua + 1, are friends.

Given a social network and two users, user A and user B, please write a function that computes the length of the shortest chain of friends between A and B.

## Discussion
<b>Q</b>: How did you represent the social network? Why did you choose this representation?<br>
<b>A</b>: I chose a dictionary for my representation of the social network because dictionaries<br>
are used to store data values in key:values pairs, perfect for the representation of this problem,  they are changeable and do not allow duplicates 
. Dictionaries are very easy to parse and to work with.

<b>Q</b>: What algorithm did you use to compute the shortest chain of friends? What alternatives did you consider? Why did you choose this algorithm over the alternatives?<br>
<b>A</b>: The algorithm that I picked for this problem is Breath First Search

<b>Q</b>:Please enumerate the test cases you considered and explain their relevance.<br>
<b>A</b>: