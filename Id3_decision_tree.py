import pandas as pd 
import numpy as np 
import math
import operator
eps = np.finfo(float).eps
def list_count(ls,attr):
    count = 0
    for i in ls:
        if i == attr:
            count += 1

    return count
def entropy(label):
    unq = set(label)
    entropy = 0
    
    for attr in unq:
        val = list_count(label,attr)
        if val != 0:
            
            entropy += -(list_count(label,attr)/len(label)) * np.log2(list_count(label,attr)/len(label))
        else:
            entropy = 0
    return entropy

def entropy_column_wrt_label(attribute,label):
    
    unq_val = list(set(attribute))
    unq_lab = list(set(label))
    IG_dict = {}
    attr = pd.DataFrame(attribute,columns = ["Attribute"])
    label = pd.DataFrame(label,columns = ["label"])
    attr_lab = pd.concat([attr,label],axis = 1)
    entropy = 0
    for i in range(len(unq_val)):
        entrop = 0
        for j in range(len(unq_lab)):
            df = attr_lab[(attr_lab["Attribute"] == unq_val[i]) & (attr_lab["label"] == unq_lab[j])]
            df1 = attr_lab[(attr_lab["Attribute"] == unq_val[i])]

            
            count = list(df.shape)[0]
            count1 = list(df1.shape)[0]
            if  count != 0:
                entrop += -((count/count1) * np.log2(count/count1))
            else:
                entrop += entrop
        fraction = count1/len(attribute)
        entropy += -fraction*entrop
        #IG_dict[unq_val[i]] = entrop
    return abs(entropy)
    
def information_gain(entropies,entropy,data):
    """
    dat = list(set(data))
    sum = 0
    for key,value in entropies.items():
        
        sum += (list_count(data,key)/len(data))*value
    """
    gain = (entropy - entropies)
    
    return gain

def select_node(columns,data,y,entropy):
    IG = {}
    for attribute in columns:
       
        attr_data = x[attribute].values
        entropies = entropy_column_wrt_label(attr_data,y)
        IG[attribute] = information_gain(entropies,entropy,attr_data)
    
    if len(IG) > 0:
        print(IG)
        node = max(IG.items(), key=operator.itemgetter(1))[0]
    
    
    return  node

def create_nw_table(x,i,node):
    
    return x.loc[x[node] == i]

def create_tree(x,y):
    global tree
    global counter
    global perentnode
    
    counter +=1
    entrop = entropy(y)
    print(entrop)
    columns = x.columns.values.tolist()
    decision = pd.DataFrame(y)
    x.reset_index(drop=True, inplace=True)
    decision.reset_index(drop=True, inplace=True)
    df = pd.concat([x,y],axis = 1)

    
    
    node = select_node(columns,x.values,y.values,entrop)
    if counter == 1:
        print("hmm")
        tree[node] = {"child":"node"}
        perentnode = node
    else:

        tree[perentnode]["child"] = {node:"attr"}
   
    columns.remove(node)
    perent = x[node].values.tolist()
  
    perent = x[node].values.tolist()
    all_unique = set(perent)
   
    tables = []
    

    for i in all_unique:
        x = pd.DataFrame(x)
        tables = create_nw_table(df,i,node)
        processed_table = tables
        
       
        freqer_dict = tables["play"].value_counts().to_dict()
     
        if len(freqer_dict)== 1:
            #print(node,tables[node].iloc[0],freqer_dict.keys(),freqer_dict)
            #return node,tables[node].iloc[0],freqer_dict.keys(),freqer_dict
            temp = tables[node].iloc[0]
            tree[perentnode]["child"][node] = {temp:"decision"}
            tree[perentnode]["child"][node][temp] =  freqer_dict.keys()
            continue
        else:
            y = processed_table["play"]
            
            processed_table = processed_table.drop([node,"play"],axis = 1)
            
           
            if processed_table.size != 0:
                
                create_tree(processed_table,y)
            else:
                print("all attribute has  been processed ")
    print(tree)
    

if __name__ == "__main__": 
    tree = {}
    counter = 0
    outlook = 'overcast,overcast,overcast,overcast,rainy,rainy,rainy,rainy,rainy,sunny,sunny,sunny,sunny,sunny'.split(',')
    temp = 'hot,cool,mild,hot,mild,cool,cool,mild,mild,hot,hot,mild,cool,mild'.split(',')
    humidity = 'high,normal,high,normal,high,normal,normal,normal,high,high,high,high,normal,normal'.split(',')
    windy = 'FALSE,TRUE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,TRUE'.split(',')
    play = 'yes,yes,yes,yes,yes,yes,no,yes,no,no,no,no,yes,yes'.split(',')
    dataset ={'outlook':outlook,'temp':temp,'humidity':humidity,'windy':windy,'play':play}
    df = pd.DataFrame(dataset,columns=['outlook','temp','humidity','windy','play'])
    y = df["play"]
    x = df.drop(columns = ["play"])
    perentnode = ""
    create_tree(x,y)

   