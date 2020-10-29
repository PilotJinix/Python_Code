source = [5,3,1,2]
for i in range(len(source)):
    print(source)
    mini = min(source[i:]) 
    min_index = source[i:].index(mini) #find index of minimum element
    source[i + min_index] = source[i] #replace element at min_index with first element
    source[i] = mini                  #replace first element with min element
    print ('langkah=',source )
print ('hasil=',source)
