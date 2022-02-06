# Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021/22

# * Problem: Radio Commercials

# * Link: https://open.kattis.com/contests/pe4egm/problems/commercials;

# * @author: Feng Yi Lu

# * @version 1.0, 2021-12-05 17:26:45

# * Method : Ad-Hoc 

# # Status : Accepted 

# # Runtime: 0.08 */
#output the biggest expected extra profit Onid can get by selecting a continuous sequence of commercial breaks.

costs = int(input().split()[1])
#reading inputs
inputs = [int(x) for x in input().split()]
numberOFCommercialBreaks = len(inputs)
# Subtract cost for every commercial
substracted = [x - costs for x in inputs]
# A constant for minimal value
minimalValue = float('-inf')

def maximumRevenue(nums):
    # maxEnding =  largest sum continous subsequences from beginning until current element
    maxEndingH = 0

    # maxSF = largest continous subsequence "so far" which not includes current element
    maxSF = minimalValue

    for i in range(numberOFCommercialBreaks):
        maxEndingH = maxEndingH + nums[i]
   # If current cost value is greater than maximum ending until here then "maximumEndingH" is current value now
        if maxEndingH < nums[i]:
            maxEndingH = nums[i]
  # If maximum ending until the current element is greater than maximum so far, we say that maxSF is maxEndingH
        if maxSF < maxEndingH:
            maxSF = maxEndingH
    return maxSF

print(maximumRevenue(substracted))



