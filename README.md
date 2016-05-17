"# CrossOver-Longpath" 

Very intereting algorithm to find the long path
in a given graph.


**Methodology:**

Start with any vertex 'u' and 'v' (u=v=x) in a given graph and explore the non-visited vertices using DFS. Assign each new vertex found as 'u'. 
Once there is no further vertex to explore, start exploring on the other side of 'v'. If there are vertices to explore, proceed with assigning each new vertex found as 'v'. Thus the final vertices 'u' and 'v' will be the longest path in a graph.  



Below are the sample graphs used for testing:

1.	Mid7
2.	Mid9
3.	NonHam24
4.	Thomassen

There graphs were provided in class 7750: Graph Theory 
taught by Prof. W. Kocay.