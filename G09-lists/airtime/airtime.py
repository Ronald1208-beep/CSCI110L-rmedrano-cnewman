# We did not use any outside resources

def airtime(heights):
    count = 0
    for i in range(len(heights)- 2):
        first_slope = heights[i+1] - heights[i]
        second_slope = heights[i+2] - heights[i+1]
        if first_slope > second_slope:
            count +=1
    return count


def main():
    num = int(input())
    heights = []
    for i in range(num):
        heights.append(int(input()))
    roller_coaster = airtime(heights)
    print(roller_coaster)

if __name__== "__main__":
    main()




