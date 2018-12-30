import numpy as py
class Solution:
    def IsMagic(self,Son):
        list=Son.tolist()
        List=[]
        for i in list:
            for j in i:
                if j>9 or j<1:
                    return False
                List.append(j)
        if len(set(List))!=9:
            return False
        a=[py.sum(Son[0,:]),py.sum(Son[1,:]),py.sum(Son[2,:]),py.sum(Son[:,0]),py.sum(Son[:,1]),py.sum(Son[:,2]),Son[0,0]+Son[1,1]+Son[2,2],Son[0,2]+Son[1,1]+Son[2,0]]
        if len(set(a))==1:
            return True
        else:
            return False
    def numMagicSquaresInside(self, grid):
        c=0
        '''
        for i in range(len(gird)):
            if i+3>len(grid):
                break
            for j in range(len(grid[0])):
                if j+3>len(grid[0]):
                    break
                Matrix=[[]]
                for k in range(3):
                    for l in range(3):
                        Matrix
        '''
        Matrix=py.asarray(grid)
        for i in range(len(grid)):
            if i+3>len(grid):
                break
            for j in range(len(grid[0])):
                if j+3>len(grid[0]):
                    break
                Son = Matrix[i:i+3,j:j+3]
                #return Son.tolist()
                if self.IsMagic(Son):
                    c+=1
        return c
        """
        :type grid: List[List[int]]
        :rtype: int
        """
