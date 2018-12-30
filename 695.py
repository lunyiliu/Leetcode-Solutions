class Solution:
    class UnionFindSet(object):
        def __init__(self, data_list):
            """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
            初始化的时候，将节点的父节点设为自身，size设为1"""
            self.father_dict = {}
            self.size_dict = {}

            for node in data_list:
                self.father_dict[node] = node
                self.size_dict[node] = 1

        def find_head(self, node):
            """使用递归的方式来查找父节点

            在查找父节点的时候，顺便把当前节点移动到父节点上面
            这个操作算是一个优化
            """
            father = self.father_dict[node]
            if(node != father):
                father = self.find_head(father)
            self.father_dict[node] = father
            return father

        def is_same_set(self, node_a, node_b):
            """查看两个节点是不是在一个集合里面"""
            return self.find_head(node_a) == self.find_head(node_b)

        def union(self, node_a, node_b):
            """将两个集合合并在一起"""
            #print ('unioned')
            if node_a is None or node_b is None:
                return

            a_head = self.find_head(node_a)
            b_head = self.find_head(node_b)

            if(a_head != b_head):
                a_set_size = self.size_dict[a_head]
                b_set_size = self.size_dict[b_head]
                if(a_set_size >= b_set_size):
                    self.father_dict[b_head] = a_head
                    self.size_dict[a_head] = a_set_size + b_set_size
                else:
                    self.father_dict[a_head] = b_head
                    self.size_dict[b_head] = a_set_size + b_set_size
        def MaxNodeSize(self):
            return max(list(self.size_dict.values()))
    
    def get_address(self,i,j,grid):
        return i*len(grid[0])+j+1
    def get_index(self,address,grid):
        if address%len(grid[0])!=0:
            return [int(address/len(grid[0])),(address%len(grid[0]))-1]
        else:
            return [int(address/len(grid[0]))-1,len(grid[0])-1]
    def maxAreaOfIsland(self, grid):
        dirts=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dirts.append(self.get_address(i,j,grid))
        if dirts==[]:
            return 0
        Union=self.UnionFindSet(dirts)
        for dirt in dirts:
            i = self.get_index(dirt,grid)[0]
            j=self.get_index(dirt,grid)[1]
            if i!=len(grid)-1 and self.get_address(i+1,j,grid) in dirts: 
                if not Union.is_same_set(self.get_address(i,j,grid),self.get_address(i+1,j,grid)):
                    Union.union(self.get_address(i,j,grid),self.get_address(i+1,j,grid))
            if i!=0 and self.get_address(i-1,j,grid) in dirts: 
                if not Union.is_same_set(self.get_address(i,j,grid),self.get_address(i-1,j,grid)):
                    Union.union(self.get_address(i,j,grid),self.get_address(i-1,j,grid))
            if j!=len(grid[0])-1 and self.get_address(i,j+1,grid) in dirts: 
                if not Union.is_same_set(self.get_address(i,j,grid),self.get_address(i,j+1,grid)):
                    Union.union(self.get_address(i,j,grid),self.get_address(i,j+1,grid))
            if j!=0 and self.get_address(i,j-1,grid) in dirts: 
                if not Union.is_same_set(self.get_address(i,j,grid),self.get_address(i,j-1,grid)):
                    Union.union(self.get_address(i,j,grid),self.get_address(i,j-1,grid))
            #print(dirt)
            #print([i,j])
            #print(list(Union.father_dict.values()))
        
        return Union.MaxNodeSize()
