def trap(height):

    stack = []
    water = 0

    for i, h in enumerate(height):
        # While the stack is not empty and the current bar is higher than the bar at the top of the stack
        while stack and h > height[stack[-1]]:
            # Pop the top of the stack
            top = stack.pop()
            # If the stack is empty after popping, break the loop
            if not stack:
                break
            # Calculate the width of the trapped water
            width = i - stack[-1] - 1
            # Calculate the height of the trapped water
            height_water = min(h, height[stack[-1]]) - height[top]
            # Add the trapped water to the total
            water += width * height_water
        # Push the current index onto the stack
        stack.append(i)

    return water

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6


class Solution:
    def trap(self, height):
        n = len(height)
        l,r  = 0 , n-1
        left_max , right_max = height[l],height[r]
        cap = 0
        while l<r :

            if left_max < right_max:
                l+=1
                left_max = max(left_max,height[l])
                cap+=left_max - height[l]
            else:
                r-=1
                right_max = max(right_max,height[r])
                cap+=right_max - height[r]
        return cap

if __name__ == '__main__':
    
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    
    obj = Solution()
    print(obj.trap(height))  # Output: 6