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
<b>A</b>: The algorithm that I picked for this problem is Breath First Search (BFS). The other alternatives I considered were Depth First Search (DFS), Dijkstra's Algorithm or A star.
I chose BFS because is very easy to implement, is a faster option than DFS when the target node is closer to the source node or when the graph is dense (has many edges) which I expect that in a social network this applies a lot.
In conclusion, I believe that BFS is a match for this type of problem. 


<b>Q</b>: Please enumerate the test cases you considered and explain their relevance.<br>
<b>A</b>: The test cases that I considered are the following:<br>
1. **The first test case** 
   * **Input:** Two users, A and B that are friends
   * **Output:** **1** (the chain between A and B)<br>
   </br>
2. **The second test case**
    * **Input:** Three users, A, B and C with C being the common friend of A and B 
    * **Output:** **2** ([A,C,B])<br>
   </br>
3. **The third test case**
    * **Input:** Multiple users, A,B ... where there are multiple chains from A to B
    * **Output:** The shortest chain of friends from A to B <br>
   </br>
4. **The fourth test case**<br>
   * **Input:** Multiple users, A,B ... but A and B don't have friends in common
   * **Output:** There is no chain between user A and B
   </br><br>
   
   From my perspective, these are the most relevant test cases for this particular problem.