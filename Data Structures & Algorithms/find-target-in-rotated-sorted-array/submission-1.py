class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:          # check the hit first
                return mid

            if nums[l] <= nums[mid]:         # left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1              # target in sorted left
                else:
                    l = mid + 1              # must be in right
            else:                            # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1              # target in sorted right
                else:
                    r = mid - 1

        return -1