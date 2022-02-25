def findRunnerUpScore(arr):
    maxScore = -6000
    runnerUpScore = -6000

    for i in range(2,len(arr)):
        if(arr[i] > maxScore):
            runnerUpScore = maxScore
            maxScore = arr[i]
            
        elif (maxScore!= arr[i] and arr[i] > runnerUpScore):
            runnerUpScore = arr[i]
    print(runnerUpScore)

arr = [ 3,4,4,6,7,8,9]
findRunnerUpScore(arr) 
