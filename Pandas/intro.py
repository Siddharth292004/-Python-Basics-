import pandas as pd

#df = pd.DataFrame(
#          {"a" : [4, 5, 6], 
#           "b" : [7, 8, 9], 
#           "c" : [10, 11, 12]},    
#        index = [1, 2, 3])
#print(df)

#df = pd.DataFrame(
#     [[4, 7, 10],
#      [5, 8, 11],
#      [6, 9, 12]], 
#     index=[1, 2, 3], 
#     columns=['a', 'b', 'c'])



df = pd.DataFrame(
          {"a" : [4 ,5, 6], 
           "b" : [7, 8, 9], 
           "c" : [10, 11, 12]},
)

print(df)   


index = pd.MultiIndex.from_tuples(
        [('d', 1), ('d', 2),
         ('e', 2)], names=['n', 'v'])
print(index)