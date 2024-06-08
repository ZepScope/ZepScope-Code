import re
import falcon.detectors.zep_checker.configs as configs
import numpy as np
import math
SYMPOL_LIST=['EQ','NEQ','GT','LT','GTE','LTE','AND','OR','NOT','ADD','SUB','MUL','DIV','MOD','RM','LM','POWER','MsgSender']
EQUAL_LIST=['GT','LT','GTE','LTE']
SYMPOL_TYPE_LIST=SYMPOL_LIST+['uint256','uint256_1','uint256_2','address','address_1','address_2']
def similarity_check_str(stringA,stringB):
    if stringA in SYMPOL_TYPE_LIST or stringB in SYMPOL_TYPE_LIST:
        if stringA==stringB:
            return True
        else:
            if stringA in EQUAL_LIST or stringB in EQUAL_LIST:
                stringA=stringA.replace('E','')
                stringB=stringB.replace('E','')
            return stringA==stringB
    minlen=min(len(stringA),len(stringB))
    if minlen==0:
        return False
    # threshold=(int(minlen/2)+1)/minlen
    if ('balance' in stringA and 'allowance' in stringB) or ('balance' in stringB and 'allowance' in stringA):
        return False
    return string_similarity(str(stringA),str(stringB))>=configs.string_sim_threshold

def similarity_list(listA,listB):
    if 'ERROR_MSG:' in listA[-1]:
        listA=listA[:-1]
    if 'ERROR_MSG:' in listB[-1]:
        listB=listB[:-1]
    sim=0
    # if isEqualName(listB):
    #     for item in listB:
    #         return similarityList(listA,item)
    if is_equal_name(listB) and is_equal_name(listA):
        if simliarity_in_sublist(listA,listB):
            return True
    if is_equal_name(listB):
        for item in listB:
            if isinstance(item,list):
                if similarity_list(listA,item):
                    return True
            elif isinstance(item,str):
                if is_equal_name(listA):
                    if compare_list_str(listA,item):
                        return True
                else:
                    if similarity_list(listA,item):
                        return True
    if isinstance(listA,str):
        listA=[listA]
    if isinstance(listB,str):
        listB=[listB]
    for i in range(len(listB)):
        if i>=len(listA):
            break
        if isinstance(listA[i],str) and isinstance(listB[i],str):
            if similarity_check_str(listA[i],listB[i]):
                sim+=1
        elif isinstance(listA[i],list) and isinstance(listB[i],str):
            if is_equal_name(listA[i]):
                sim+=compare_list_str(listA[i],listB[i])
            else:
                sim+=0        
        elif isinstance(listA[i],str) and isinstance(listB[i],list):
            if is_equal_name(listB[i]):
                sim+=compare_list_str(listB[i],listA[i])
            else:
                sim+=0
        elif isinstance(listA[i],list) and isinstance(listB[i],list):
            if is_equal_name(listA[i]) and is_equal_name(listB[i]):
                sim+=compare_sim_list(listA[i],listB[i])
            elif not is_equal_name(listA[i]) and not is_equal_name(listB[i]):
                sim+=similarity_list(listA[i],listB[i])
            elif is_equal_name(listA[i]) and not is_equal_name(listB[i]):
                sim+=similarity_list(listA[i],listB[i])
            elif not is_equal_name(listA[i]) and is_equal_name(listB[i]):
                 sim+=similarity_list(listA[i],listB[i])
            else: 
                pass
    # if 'balance' in str(listA) or 'balance' in str(listB) or 'allowance' in str(listA) or 'allowance' in str(listB):
    #     threshold=3
    threshold=(math.ceil(len(listB)/2)+1)
    # threshold=len(listB)*0.5
    return sim>=threshold


def compare_sim_list(listA,listB):
    for item in listA:
        if isinstance(item,list) and is_equal_name(item):
            if compare_sim_list(item,listB):
                return True
        elif isinstance(item,list) and not is_equal_name(item):
            if similarity_list(item,listB):
                return True
        elif isinstance(item,str):
            for itemB in listB:
                if isinstance(itemB,list) and is_equal_name(itemB):
                    if compare_list_str(itemB,item):
                        return True
                elif isinstance(itemB,list) and not is_equal_name(itemB):
                    continue
                elif isinstance(itemB,str):
                    if similarity_check_str(item,itemB):
                        return True
    return False

def compare_list_str(listA,strb):
    for item in listA:
        if isinstance(item,list):
            if compare_list_str(item,strb):
                return True
        else:
            if similarity_check_str(item,strb):
                return True
        
    return False

def simliarity_in_sublist(listA,listB):
    for item in listA:
        if isinstance(item,list):
            if simliarity_in_sublist(item,listB):
                return True
        else:
            if similarity_sublist_str(listB,item):
                return True
    return False
def similarity_sublist_str(listA,stringB):
    for item in listA:
        if isinstance(item,list):
            if similarity_sublist_str(item,stringB):
                return True
        else:
            if similarity_check_str(item,stringB):
                return True
    return False
            
                
def revert_list(listA):
    newA=[]
    if len(listA)!=3:
        return None
    if isinstance(listA[0],list):
        return None
    if listA[0]=='GT':
        newA.append('LTE')
        newA.append(listA[2])
        newA.append(listA[1])
    elif listA[0]=='GTE':
        newA.append('LT')
        newA.append(listA[2])
        newA.append(listA[1])
    elif listA[0]=='LTE':
        newA.append('GT')
        newA.append(listA[2])
        newA.append(listA[1])
    elif listA[0]=='LT':
        newA.append('GTE')
        newA.append(listA[2])
        newA.append(listA[1])
    elif listA[0]=='NEQ' or listA[0]=='EQ':
        newA.append(listA[0])
        newA.append(listA[2])
        newA.append(listA[1])
    else:
        newA=listA
    return newA

def similarity_check_list(ListA,ListB):
    if similarity_list(ListA,ListB):
        return True
    else:
        newListA=revert_list(ListA)
        if newListA is None:
            return False
        return similarity_list(newListA,ListB)



def edit_distance(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    m, n = len(s1), len(s2)
    
    # Create a table to store results of subproblems
    dp = np.zeros((m+1, n+1), dtype=int)
    
    # Fill the table in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
            
            # If first string is empty, insert all characters of second string
            if i == 0:
                dp[i][j] = j
                
            # If second string is empty, remove all characters of first string
            elif j == 0:
                dp[i][j] = i
                
            # If last characters are the same, ignore them and get the value for the remaining string
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
            # If last characters are not the same, consider all possibilities and get the minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],       # Insert
                                   dp[i-1][j],       # Remove
                                   dp[i-1][j-1])     # Replace
                
    return dp[m][n]

def normalized_edit_distance(s1, s2):
    raw_distance = edit_distance(s1, s2)
    max_length = max(len(s1), len(s2))
    return raw_distance / max_length


def string_similarity(s1, s2):
    # Check if one string is a substring of the other
    if (s1 in s2 or s2 in s1) and len(s1)>1 and len(s2)>1:
        return 1.0
    
    # Calculate normalized edit distance
    norm_distance = normalized_edit_distance(s1, s2)
    
    # Return similarity score
    return 1 - norm_distance


def is_equal_name(req_list):
    if not isinstance(req_list,list):
        return False
    if len(req_list)<=1:
        return True
    if isinstance(req_list[0],str):
        if req_list[0] in SYMPOL_LIST:
            return False
    return True