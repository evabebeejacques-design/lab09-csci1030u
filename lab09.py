# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   ...
    # Problem: two indices i<j where nums[i] + nums[j] == target
    # Example: num list = [3,2,4] target = 6 does 2(idex 1) + 4(index 2) = 6 so [1,2]
    # Approac to problem: Keep a directory to map each number to its indexas we iterate. For each number see if target - num = is 
    # already there if so return [seen[target-num],i]
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    seen = {}
    for i,nums in enumerate(nums):
        complement = target - nums
        if complement in seen:
            return [seen[complement],i]
        seen[nums] = i


def max_profit(prices):
    # Outline:
    #   ...
    # Problem: Find the biggest difference in prices[j] - prices[i] with j > i (or 0)
    # Example: [7,1,5,3,6,4] the lowest price is 1 and the highest price after 1 is 6 so it returns 5
    # Approach: Go through list and check for lowest price and highest profit after the lowest price if there is a lower price from the 
    # previous price or the higher profit after the previous profit then update it
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    if not prices:
        return 0
    min_prices = prices[0]
    max_proft = 0
    for price in prices[1:]:
        if price < min_prices:
            min_prices = price
        elif price-min_price > max_profit:
            max_profit = price - min_prices
    return max_profit


def max_subarray(nums):
    # Outline:
    #   ...
    # Problem: Find the biggest sum of any continous slices of numbers
    # Example: [-2,1,-3,4,-1,2,1,-5,4] takes [4,-1,2,1] to return 6
    # Approach: track the current sum and compare it with the different slices sum and if the different slices sum is bigger than the 
    # current sum then update the current slice to the new one.
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # Problem: Check if [],(),{} are all closed properly using LIFO order
    # Example {[]} checks that both [] and {} are closed to return true
    # Approach: Use a list as a stack.Push opening bracketonto the stack. When a closing bracket appears,verify that there is an opening 
    # bracket that goes along with it return true only if eveything is empty.
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    stack = []
    pairs {')':'(',']':'[', '}':'{'}
    for char in s:
        if char in pairs.value():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print("max_profit:", max_profit([7, 1, 5, 3, 6, 4]))   # 5
    print("max_subarray:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print("is_balanced:", is_balanced("()[]{}"))           # True
    pass


if __name__ == "__main__":
    main()
