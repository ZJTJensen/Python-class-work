#print out stars for each number in a list


def draw_stars(nums):
    for i in range(len(nums)):
        if isinstance(nums[i], int):
            output = ''
            for i in range(0, nums[i]):
                output += "*"
            print output
        elif isinstance(nums[i], str):
            output = ''
            for j in range (0, len(nums[i])):
                output += nums[i][0] 
            print output


draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
# draw_stars([1,2,3,4,5])
        