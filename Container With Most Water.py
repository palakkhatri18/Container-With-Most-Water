#Container With Most Water
#Given N non-negative integers a1,a2,....an where each represents a point at coordinate (i, ai). N vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i,0). Find two lines, which together with x-axis forms a container, such that it contains the most water.

#Note : In Case of single verticle line it will not be able to hold water.
def maxArea(A,le):
    #code here
    i=0
    j=le-1
    ans=0
    while i<j:
        ans=max(ans,(j-i)*min(A[i],A[j]))
        if A[i]<A[j]:
            i=i+1
        else:
            j=j-1
            
    return ans  