class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        high_front = 0
        front_list = []
        high_back = 0
        back_list = []
        amount = 0
        for i in range(len(height)):
            if high_front <= height[i]:
                high_front = height[i]
            if high_back <= height[len(height)-i-1]:
                high_back = height[len(height)-i-1]
            front_list.append(high_front)
            back_list.insert(0, high_back)
        for i in range(len(height)):
            water = min(front_list[i], back_list[i])
            amount += water - height[i]
        return amount
            
        