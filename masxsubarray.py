input_data = [1,2,3,-9, 5, 7, -99, 2, 8]
def max_sub_array(input_data):
    global_max = 0
    for i in range(len(input_data)+1):
        for j in range(len(input_data)+1):
            iter_max = sum(input_data[i:j])
            print(iter_max, input_data[i:j])
            if iter_max > global_max:
                global_max = iter_max
    return global_max
            #use this if statement to 
            #if(input_data[i:j]):
                #print(input_data[i:j])


max_sub_array(input_data)
#print out all the possbile arrays starting from each index