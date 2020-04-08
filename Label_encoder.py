"""
this script has been created to handle  the categorial  data.
encoder function :- Label Encoding is a popular encoding technique for handling categorical variables. 
In this technique, each label is assigned a unique integer based on alphabetical ordering.
reverse_encoding :- it will provide original label of a encoded value
OneHotEncoder :- one hot encoding is a representation of categorical variables as binary vectors.
"""
import pandas as pd 
import numpy as np
def encoder(attribute):
    encode_dict = {}
    count = 0
    encodes = []
    for i in attribute:
        if i not in encode_dict:
            encode_dict[i] = count

            count += 1
    for i in range(len(attribute)):
        if attribute[i] in encode_dict:
            temp = attribute[i]
            encodes.append(encode_dict[temp])
    return encodes,encode_dict
def reverse_encoding(encodes,encoder):
    labels = []
    for i in range(len(encodes)):
        for key,value  in encoder.items():
            if encodes[i] == value:
                labels.append(key)
    print(len(labels))
    print(len(encodes))
    return labels
   
def OneHotEncoder(encodes,encoder):
    columns = []
    for key in encoder.keys():
        columns.append(key)
    labels = reverse_encoding(encodes,encoder)
   
   
    print(columns)
    d = {key:[] for key in columns}
    print(d)
    for label in labels:
        
        for key in d.keys():
            
            if key != label:
              
                d[key].append(0)
            else:
                
                d[key].append(1)
            
    
    OneHotEncodes = pd.DataFrame(data = d)
    return OneHotEncodes
if __name__ == '__main__':
    pass
