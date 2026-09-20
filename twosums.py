def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if nums[mid] > 0 and nums[mid-1] == target:
                return "left"
            elif nums[mid] > target:
                return " left"
            else:
                return "right"
            return "found it"


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if nums[mid] < len(nums - 1) and nums[mid +1] == target:
                return "right"
            elif nums[mid] < target :
                return "right"
            else:
                return "left"
            return "found it"        
        


def first_and_last_position(nums, target):
    first_position(),last_position()
