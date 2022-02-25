def secondLowest(dict_name_score):
    minScore = min(dict_name_score.values())
    secondLowest = 9999
    for value in dict_name_score.values():
        if(value < secondLowest and value > minScore):
            secondLowest = value
    
    for key,value in sorted(dict_name_score.items()):
        if(value == secondLowest):
            print(key)



dict_name_score = {"Harry":37.21,"Berry":37.21,"Tina":37.2,"Akriti":41,"Harsh":39}
secondLowest(dict_name_score)