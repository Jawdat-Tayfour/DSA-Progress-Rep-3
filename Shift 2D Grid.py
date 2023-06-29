# I'm currently really bad handling 2D arrays so I'll just learn it from him. 
def S2F(grid:list[list[int]],k:int) -> list[list[int]]:
    m,n = len(grid),len(grid[0])
    
    def posToVal(r,c):
        return r*n+c
    def valTOpos(v):
        return [v//n,v%n] # r,c 
    res = [[0]*n for i in range(m)]
    for r in range(m):
        for c in range(n):
            newVal= (posToVal(r,c) + k ) % (m * n)
            newR,newC = valTOpos(newVal)
            res[newR][newC]  = grid[r][c]
    return res         

# Time Complexity for this is O(n*m)
# I will try a solution and leave it here even if it didn't work 
def S2F2(grid:list[list[int]],k:int) -> list[list[int]]:
    m , n = len(grid) , len(grid[0])
    def TwoDtoD(grid):# This One Turns a 2D Array into a 1D and returns the new array
        l = 0
        D =[0]*m*n
        for i in range(m):
            for j in range(n):
                D[l] = grid[i][j]
                l+=1
        return D        
    
    def shifter(D): # This one shifts the elements of the 1D array by the amount that is needed and returns a new 1D array
        newD = [0]*len(D)
        for i in range(len(D)):
            t = i + k * -1
            if t >= len(D) :
                t = t%l
            newD[i] = D[t]
        return newD    
    
    def Dto2D(grid,D): # This One Turns a 1D Array into a 2D and returns the result 
        l = 0
        for i in range(m):
            for j in range(n):
                grid[i][j]= D[l]
                l+=1
        return grid         
    
    D = TwoDtoD(grid)
    newD = shifter(D)
    grid = Dto2D(grid,newD)            
    return grid
# I did it, even though it took me some time but I implemented it. ^_^ So happy to hava a solutions that works!. 
# I thought of splitting the tasks of the algorithm into small pieces and code each on its own. 

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

k = 2
print(S2F(grid,k))
print(S2F2(grid,k))
