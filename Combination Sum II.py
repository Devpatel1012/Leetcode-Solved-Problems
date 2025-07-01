class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(remaining_target, current_combination, start_index):
            if remaining_target == 0:
                result.append(list(current_combination))
                return

            for i in range(start_index, len(candidates)):
                # Skip duplicates
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                candidate = candidates[i]
                
                if candidate > remaining_target:
                    break
                
                current_combination.append(candidate)
                backtrack(remaining_target - candidate, current_combination, i + 1)
                current_combination.pop()
        
        backtrack(target, [], 0)
        return result
