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