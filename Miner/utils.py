
from slither.core.solidity_types.function_type import FunctionType
from slither.core.solidity_types.user_defined_type import UserDefinedType
from slither.core.solidity_types.array_type import ArrayType
from slither.slithir.operations.internal_call import InternalCall
from slither.slithir.operations.high_level_call import HighLevelCall
from slither.slithir.operations.low_level_call import LowLevelCall
from call_chain import *

def get_func_def_call_chain(function_sign, callGraph):
    try:
        func_recognition = functionRecognition(function_sign, callGraph)
        return func_recognition.func_def_call_chain()
    except NoFunctionError:
        return []
def ssa_name(expression):
    if hasattr(expression,'canonical_name'):
        # if hasattr(expression,'ssa_name'):
        #     return expression.canonical_name.split('.')[0]+'.'+expression.canonical_name.split('.')[1]+'.'+expression.ssa_name
        # else:
        return expression.canonical_name
    else:
        return str(expression)



def get_func_direct_caller(function_sign, callGraph):
    try:
        func_recognition = functionRecognition(function_sign, callGraph)
        return func_recognition.find_direct_caller()
    except NoFunctionError:
        return []


class functionRecognition():
    def __init__(self, function_sign, callGraph):
        # self.function_sign = function_sign
        
        self.contract_name = function_sign.split('.')[0]
        function_sign = function_sign.split('.')[1]
        self.function_name = function_sign.split('(')[0]
        self.function_para = function_sign.split('(')[1].split(')')[0].split(',')
        self.canonical_name = self.contract_name + '.' + self.function_name + '(' + ','.join(self.function_para) + ')'
        self.function_sign = function_sign
        self.recognized_function = None
        self.nodes = set()
        for node in callGraph.nodes:
            for func in node.functions:
                self.nodes.add(func)
        self.graph = Graph()
        self.graph.addAllEdges(callGraph.edges)
        self.recongize()
    def recongize(self):
        for func in self.nodes:
            if func.signature_str == self.function_sign and func.canonical_name == self.canonical_name:
                self.recognized_function = func
                return True
        return False 
    def func_def_call_chain(self):
        if not self.recognized_function:
            raise NoFunctionError("No function is recognized")
        defCallChain=self.graph.BFS(self.recognized_function)
        for call in defCallChain:
            if not hasattr(call, 'name'):
                continue
            if 'require' in call.name:
                defCallChain.remove(call)
        return defCallChain
    def find_direct_caller(self):
        if not self.recognized_function:
            raise NoFunctionError("No function is recognized")
        directCaller = []
        reversed_graph = self.graph.reverse()
        for node in reversed_graph.edges:
            now_node = node
            if type(now_node)==tuple:
                now_node=now_node[1]
            if isinstance(now_node, SolidityFunction):
                continue
            if not hasattr(now_node, 'signature_str'):
                continue
            if self.recognized_function.signature_str == now_node.signature_str and self.recognized_function.canonical_name == now_node.canonical_name:
                directCaller.extend(reversed_graph.edges[node])
        return directCaller

    
def merge_lists(lists):
    merged = []
    while len(lists) > 0:
        first, *rest = lists
        first = set(first)

        lf = -1
        while len(first) > lf:
            lf = len(first)

            rest2 = []
            for r in rest:
                if len(first.intersection(set(r))) > 0:
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2

        merged.append(list(first))
        lists = rest
    return merged
class NoFunctionError(Exception):
    pass


def process_paras(function):
    if hasattr(function, 'arguments'):
        func_pars = {}
        cou_dict = {}
        for para in function.arguments:
            canonical_name=ssa_name(para)
            if isinstance(para.type, UserDefinedType):
                if 'UserDefinedType' in cou_dict:
                    cou_dict['UserDefinedType'] += 1
                else:
                    cou_dict['UserDefinedType'] = 1
                func_pars[canonical_name] = 'UserDefinedType' + '_' + str(cou_dict['UserDefinedType'])
            elif isinstance(para.type, ArrayType):
                if isinstance(para.type.type, UserDefinedType):
                    name='UserDefinedType'
                else:
                    name=para.type.type.name
                if 'ArrayType_'+name in cou_dict:
                    cou_dict['ArrayType_'+name] += 1
                else:
                    cou_dict['ArrayType_'+name] = 1
                func_pars[canonical_name] = 'ArrayType_'+name + '_' + str(cou_dict['ArrayType_'+name])
            #need to reconsider
            elif isinstance(para.type, FunctionType):
                func_pars[canonical_name] = 'FunctionType_'+para.type.signature
            else:
                if para.type.name in cou_dict:
                    cou_dict[para.type.name] += 1
                else:
                    cou_dict[para.type.name] = 1
                func_pars[canonical_name] = para.type.name + '_' + str(cou_dict[para.type.name])
        for func_par in func_pars:
            func_pars[func_par]=func_pars[func_par]
        return func_pars
    elif hasattr(function,'parameters'):
        func_pars = {}
        cou_dict = {}
        for para in function.parameters:
            canonical_name=ssa_name(para)
            if isinstance(para.type, UserDefinedType):
                if 'UserDefinedType' in cou_dict:
                    cou_dict['UserDefinedType'] += 1
                else:
                    cou_dict['UserDefinedType'] = 1
                
                func_pars[canonical_name] = 'UserDefinedType' + '_' + str(cou_dict['UserDefinedType'])
            elif isinstance(para.type, ArrayType):
                if isinstance(para.type.type, UserDefinedType):
                    name='UserDefinedType'
                else:
                    name=para.type.type.name
                if 'ArrayType_'+name in cou_dict:
                    cou_dict['ArrayType_'+name] += 1
                else:
                    cou_dict['ArrayType_'+name] = 1
                func_pars[canonical_name] = 'ArrayType_'+name + '_' + str(cou_dict['ArrayType_'+name])
            #need to reconsider
            elif isinstance(para.type, FunctionType):
                func_pars[canonical_name] = 'FunctionType_'+para.type.signature
            else:
                if para.type.name in cou_dict:
                    cou_dict[para.type.name] += 1
                else:
                    cou_dict[para.type.name] = 1
                func_pars[canonical_name] = para.type.name + '_' + str(cou_dict[para.type.name])
        # for func_par in func_pars:
        #     func_pars[func_par]=func_pars[func_par]
        return func_pars
    else:
        return {}


def variable_extend(req_lists,variables):
    new_req_lists=[]
    # req_list 是 [reqs]
    for req_list in req_lists:
        if isinstance(req_list,list):
            new_req_lists.append(variable_extend(req_list,variables))
        else:
            new_req=[]
            new_req.append(req_list)
            for i in range(len(variables)):
                if req_list in variables[i]:
                    new_req.extend(variables[i])
                else:
                    for var in variables[i]:
                        if var in req_list and can_replace(var, req_list) and var!=req_list:
                            req_list=req_list.replace(var,var)
                            if i==len(variables)-1:
                                new_req.append(req_list)
            new_req=list(set(new_req))
            new_req_lists.extend(new_req)
    return new_req_lists
    



def can_replace(a,b):
    next_character = next_char(a, b)
    before_character = before_char(a, b)
    if next_character is None and before_character == '@':
        return True
    if next_character == '@' and before_character is None:
        return True
    if next_character == '@' and before_character == '@':
        return True
    if next_character == '(' and before_character == ')':
        return True
    if next_character == '[' and before_character == ']':
        return True
    return False




def next_char(a, b):
    # Find the position of a in b
    index = b.find(a)
    
    # If a is not found in b, return None
    if index == -1:
        return None
    
    # If a is at the end of b, there's no next character
    if index + len(a) >= len(b):
        return None
    
    # Return the next character
    return b[index + len(a)]


def before_char(a, b):
    # Find the position of a in b
    index = b.find(a)
    
    # If a is not found in b, return None
    if index == -1:
        return None
    
    # If a is at the end of b, there's no next character
    if index -1 <0:
        return None
    
    # Return the next character
    return b[index -1]

def delete_can_name(req_lists):
    new_req_lists=[]
    for req_list in req_lists:
        new_req_lists.append(delete_can_name_list(req_list))
    return new_req_lists
def delete_can_name_list(req_list):
    new_req_list=[]
    for req in req_list:
        if isinstance(req,list):
            new_req_list.append(delete_can_name_list(req))
        else:
            if 'msg.sender' in req:
                req=req.replace('msg.sender','msgsender')
            deleted=delete_can_name_str(req)
            if deleted not in new_req_list:
                new_req_list.append(deleted)
    return new_req_list
def delete_can_name_str(req_str):
    if 'ERROR_MSG' in req_str:
        return req_str
    if req_str=='Strings.toHexString(uint256,uint256).value':
        return req_str
    if '@' in req_str:
        eles=req_str.split('@')
        new_req_str=''
        for ele in eles:
            new_ele=delete_can_name_str(ele)
            new_req_str+=new_ele
            new_req_str+='@'
        new_req_str=new_req_str[:-1]
        return new_req_str
    if '.' in req_str:
        req_str= req_str.split('.')[-1]
        if '#' in req_str:
            req_str=req_str.split('#')[0]
        return req_str
    return req_str



def get_caller(call_graph,function):
    call_chain=CallChain(call_graph,function)
    call_chain.get_def_call_chain()
    call_chain.get_call_chain()
    #检查def call chain 中的 require
    caller_def_call_chain={}#{directed caller: def call chain的字典}
    flag_add={}#{function:has add private}
    if function.contract_declarer.contract_kind=='interface':
        return {}
    if (function.visibility=='public' or function.visibility=='external') and function.contract_declarer.contract_kind!='interface':
        caller_def_call_chain[function]=call_chain.defCallChains
        flag_add[function]=False
    else:
        for callers in call_chain.callChains:
            func_def_call_chian=[]+call_chain.defCallChains
            flag=False
            for caller in callers:
                if isinstance(caller,tuple):
                    call_function=caller[1]
                else:
                    call_function=caller
                if not hasattr(call_function,'visibility'):
                    break
                if ('initialize' or 'constructor') in str(call_function):
                    continue
                if call_function.visibility=='internal' or call_function.visibility=='private':
                    func_def_call_chian.append(call_function)
                    flag=True
                    continue
                else:
                    caller_def_call_chain[call_function]=func_def_call_chian
                    flag_add[call_function]=flag
                    break
    return caller_def_call_chain

def paras_name(function:FunctionContract):
    func_pars=process_paras(function)
    para_list=[]
    for key in func_pars:
        para_list.append([func_pars[key],key])
    return para_list


def contains_function_in_call(caller,function):
    for node in caller.nodes_ordered_dominators:
        for ir in node.irs:
            if isinstance(ir,(InternalCall,LowLevelCall,HighLevelCall)):
                if ir.function.canonical_name==function.canonical_name and ir.function.signature_str==function.signature_str:
                    return True
                else:
                    if contains_function_in_call(ir.function,function):
                        return True
    return False

def find_contains_function(caller, function):
    for node in caller.nodes_ordered_dominators:
        for ir in node.irs:
            if isinstance(ir,(InternalCall,LowLevelCall,HighLevelCall)):
                if ir.function.canonical_name==function.canonical_name and ir.function.signature_str==function.signature_str:
                    return function
                else:
                    if contains_function_in_call(ir.function,function):
                        return ir.function




EQ = "=="
NEQ = "!="
GT = ">"
GTE = ">="
LT = "<"
LTE = "<="
AND = "&&"
OR = "||"
NOT = "!"
ADD = "+"
SUB = "-"
MULTIPLY = "*"
DIVIDE = "/"
MOD = "%"
RM = ">>"
LM = "<<"
POWER = "**"


def translate_op_type(opType):
    if opType == EQ:
        return "EQ"
    elif opType == NEQ:
        return "NEQ"
    elif opType == GT:
        return "GT"
    elif opType == GTE:
        return  "GTE"
    elif opType == LT:
        return "LT"
    elif opType == LTE:
        return "LTE"
    elif opType == AND:
        return "AND"
    elif opType == OR:
        return "OR"
    elif opType == NOT:
        return "NOT"
    elif opType == ADD:
        return "ADD"
    elif opType == SUB:
        return "SUB"
    elif opType == MULTIPLY:
        return "MUL"
    elif opType == DIVIDE:
        return "DIV"
    elif opType == MOD:
        return "MOD"
    elif opType == RM:
        return "RM"
    elif opType == LM:
        return "LM"
    elif opType == POWER:
        return "POWER"
    else:
        print(opType)
        assert False  
        
        
def to_tuple(data):
    """Recursively convert nested lists to nested tuples."""
    if isinstance(data, list):
        return tuple(to_tuple(item) for item in data)
    else:
        return data

def remove_duplicates(main_list):
    seen = set()
    unique_list = []
    for sublist in main_list:
        tuple_version = to_tuple(sublist)
        if tuple_version not in seen:
            seen.add(tuple_version)
            unique_list.append(sublist)
    return unique_list
