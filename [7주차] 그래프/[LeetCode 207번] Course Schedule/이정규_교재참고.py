class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def dfs(s):
            if s in chk_cir:
                return False
            if s in visited:
                return True
            
            chk_cir.add(s)
            for c in nodes[s]:
                if not dfs(c):
                    return False
                
            chk_cir.remove(s)
            visited.add(s)
            return True
        
        nodes = collections.defaultdict(list)
        for p, c in prerequisites:
            nodes[p].append(c)
        
        visited = set()
        chk_cir = set()
        
        for unit in list(nodes):
            if not dfs(unit):
                return False
            
        return True