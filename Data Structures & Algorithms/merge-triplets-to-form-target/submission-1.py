class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur_triplet = [float('-inf'),float('-inf'),float('-inf')]
        i,j,k = target
        for x,y,z in triplets:
            if x <= i and y <= j and z <= k:
                prev_x,prev_y,prev_z = cur_triplet
                new_x = max(x,prev_x)
                new_y = max(y,prev_y)
                new_z = max(z, prev_z)
                cur_triplet = [new_x,new_y,new_z]
                # print(cur_triplet)
        
        return cur_triplet == target
