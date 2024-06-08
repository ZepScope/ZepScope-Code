from collections import defaultdict
from falcon.core.expressions.literal import Literal
from falcon.core.expressions.identifier import Identifier
from falcon.core.expressions.index_access import IndexAccess
from falcon.core.expressions.member_access import MemberAccess
from falcon.core.expressions.binary_operation import BinaryOperation
from falcon.core.expressions.call_expression import CallExpression
from falcon.core.expressions.type_conversion import TypeConversion
from falcon.core.expressions.unary_operation import UnaryOperation
from falcon.core.solidity_types.function_type import FunctionType
from falcon.core.solidity_types.user_defined_type import UserDefinedType
from falcon.core.solidity_types.array_type import ArrayType
from falcon.core.expressions.assignment_operation import AssignmentOperation
from falcon.core.declarations.function_contract import FunctionContract
from falcon.core.variables.local_variable import LocalVariable
from falcon.core.cfg.node import Node
from falcon.ir.variables.temporary import TemporaryVariable
from falcon.core.expressions.tuple_expression import TupleExpression
from falcon.core.variables.state_variable import StateVariable
from falcon.ir.operations.internal_call import InternalCall
from falcon.ir.operations.high_level_call import HighLevelCall
from falcon.ir.operations.low_level_call import LowLevelCall
from falcon.ir.operations.library_call import LibraryCall
from falcon.detectors.zep_checker.variable_utils import *
import re
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

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
    def addEdge(self, u, v):
        if isinstance(u,tuple):
            u=u[1]
        if isinstance(v,tuple):
            v=v[1]
        if not(hasattr(u,'signature_str') and hasattr(v,'signature_str')):
            return
        exist=False
        for source in self.edges:
            if func_equal(source,u):
                for target in self.edges[source]:
                    if func_equal(target,v):
                        exist=True
                        break
                if not exist:
                    self.edges[source].append(v)
                    exist=True
                    break
        if not exist:
            self.edges[u].append(v)
    def addAllEdges(self, edges:list):
        for edge in edges:
            self.addEdge(edge.source_call, edge.target_call)
    def reverse(self):
        rgraph = Graph()
        for node in self.edges:
            if self.edges[node]==[]:
                continue
            for neighbor in self.edges[node]:
                rgraph.addEdge(neighbor, node)
        return rgraph

    def BFS(self, s):
        visited=set()
        queue = []
        queue.append(s)
        visited.add(s)
        nodes_reachable = []

        while queue:
            node = queue.pop(0)
            # if type(node)==tuple:
            #     node=node[1]
            nodes_reachable.append(node)
            nodes=[]
            if not hasattr(node, 'signature_str'):
                continue
            for i in self.edges.keys():
                if hasattr(i, 'signature_str'):
                    if func_equal(i, node):
                        nodes.append(i)
            for n in nodes:
                for i in self.edges[n]:
                    if i not in visited :
                        queue.append(i)
                        visited.add(i)
        final_reachable = []
        for node in nodes_reachable:
            if type(node)==tuple:
                final_reachable.append(node[1])
            else:
                final_reachable.append(node)
        return final_reachable

    def DFS(self, start, path=None):
        if path is None:
            path = [start]
        else:
            path = path + [start]
        unvisited_nodes=[]
        for snode in self.edges:
            if func_equal(snode,start):
                for node in self.edges[snode]:
                    if not judge_in(node,path):
                        unvisited_nodes.append(node)
        # unvisited_nodes = [node for node in self.edges[start] if judge_in(node, path)]
        
        paths = []
        for node in unvisited_nodes:
            paths.extend(self.DFS(node, path))

        # Only add the current path to the list of paths if there are no more nodes to visit.
        # This ensures that we only keep paths that are not sub-paths of any other path.
        if not unvisited_nodes:
            paths.append(path)
        
        return paths
def judge_in(node, path)->bool:
    for n in path:
        if func_equal(n,node):
            return True
    return False
def func_equal(func1, func2)->bool:
    if not(hasattr(func1,'signature_str') and hasattr(func2,'signature_str')):
        return False
    if func1.signature_str == func2.signature_str and func1.canonical_name == func2.canonical_name:
        return True
    else:
        return False



def check_target_function(function:FunctionContract,req_dic,contract_name=None,related_name=None,check_sub=False):
    if contract_name==None:
        contract_name=function.canonical_name.split('.')[0]
    if related_name!=None:
        func_sign=contract_name+'.'+function.signature_str
        if func_sign in req_dic.keys():
            return req_dic[func_sign]
        elif check_sub:
            for key in req_dic.keys():
                if match_sub_signature(key,func_sign,match_con_name=True):
                    return req_dic[key]
        for related in related_name:
            func_sign=related+'.'+function.signature_str
            if func_sign in req_dic.keys():
                return req_dic[func_sign]
            elif check_sub:
                for key in req_dic.keys():
                    if match_sub_signature(key,func_sign,match_con_name=True):
                        return req_dic[key]
        return None
    func_sign=contract_name+'.'+function.signature_str
    if func_sign in req_dic.keys():
        return req_dic[func_sign]
    elif check_sub:
        for key in req_dic.keys():
            if match_sub_signature(key,func_sign,match_con_name=True):
                return req_dic[key]
def check_target_function_sign(function_sign,req_dic,contract_name=None,related_name=None,check_sub=False):
    if contract_name==None:
        contract_name=function_sign.split('.')[0]
    if related_name!=None:
        func_sign=contract_name+'.'+function_sign.split('.')[1]
        if func_sign in req_dic.keys():
            return req_dic[func_sign]
        elif check_sub:
            for key in req_dic.keys():
                if match_sub_signature(key,func_sign,match_con_name=True):
                    return req_dic[key]
        for related in related_name:
            func_sign=related+'.'+function_sign.split('.')[1]
            if func_sign in req_dic.keys():
                return req_dic[func_sign]
            elif check_sub:
                for key in req_dic.keys():
                    if match_sub_signature(key,func_sign,match_con_name=True):
                        return req_dic[key]
        return None
    func_sign=contract_name+'.'+function_sign.split('.')[1]
    if func_sign in req_dic.keys():
        return req_dic[func_sign]
    elif check_sub:
        for key in req_dic.keys():
            if match_sub_signature(key,func_sign,match_con_name=True):
                return req_dic[key]



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
    elif opType == "~":
        return "NOT"
    elif opType == "&":
        return "AND"
    elif opType == "|":
        return "OR"
    else:
        print(opType)
        assert False  

def process_call_function(function):
    final_result=[]
    if hasattr(function,'called'):
        called=function.called
    elif hasattr(function,'function'):
        called=function.function
    else:
        called=function
    final_result.append(ssa_name(function))
    result=[]
    arguments=[]
    for argument in function.arguments:
        arguments.append(ssa_name(argument))  
    if isinstance(called,Identifier):
        called=called.value
    if not isinstance(called,FunctionContract):
        return final_result
    arg_replace={}
    cou=0
    flag=True
    return_node=None
    for node in  called.nodes_ordered_dominators:
        strnode=str(node)
        if strnode.startswith('RETURN'):
            return_node=node
            continue
        if strnode.startswith('ENTRY_POINT') or strnode.startswith('RETURN'):
            continue
        else:
            flag=False
            break
    if not flag:
        return final_result
    for parameter in called.parameters:
        # arg_replace[parameter.name]=arguments[cou]
        arg_replace[arguments[cou]]=ssa_name(parameter)
        cou+=1
    re_value=[]
    for ret in called.return_values:
        ret_process=process_returns(ret)
        for p in ret_process:
            if isinstance(p,list):
                for pp in p:
                    for arg in arguments:
                        if arg in pp:
                            pp=pp.replace(arg,arg_replace[arg])
            else:
                for arg in arguments:
                    if arg in p:
                        p=p.replace(arg,arg_replace[arg])
        re_value.extend(ret_process)
    for i in range(len(re_value)):
        if isinstance(re_value[i],str) and re_value[i].endswith('.'):
            re_value.remove(re_value[i])
            i=i-1 if i>0 else 0
    ret_process=process_returns(return_node)
    for p in ret_process:
        if isinstance(p,list):
            for pp in p:
                for arg in arguments:
                    if arg in pp:
                        pp=pp.replace(arg,arg_replace[arg])
        else:
            for arg in arguments:
                if arg in p:
                    p=p.replace(arg,arg_replace[arg])
    re_value.extend(ret_process)
    result.extend(re_value)
    result=remove_duplicates(result)
    if len(result)==1:
        final_result.append(result[0])
    elif len(result)>1 and result[0] in ['EQ','NEQ','GT','LT','GTE','LTE','AND','OR','NOT','ADD','SUB','MUL','DIV','MOD','RM','LM','POWER']:
        final_result.append(result)
    else:
        final_result.extend(result)
    return final_result
        
def process_returns(expression):
    result = []
    if isinstance(expression, Literal):
        result.append(ssa_name(expression))
        return result
    elif isinstance(expression,Identifier):
        result.append(ssa_name(expression))
        return result 
    elif isinstance(expression, BinaryOperation):
        opType = translate_op_type(str(expression.type)) 
        left = process_condition(expression.expression_left)
        right = process_condition(expression.expression_right)
        result.append(str(opType))
        result.extend(left)
        result.extend(right)
        return result 
    elif isinstance(expression, IndexAccess):
        expression_left=process_expression(expression.expression_left)
        expression_right=process_expression(expression.expression_right)
        for l in expression_left:
            for r in expression_right:
                if isinstance(r,list):
                    for rr in r:
                        if isinstance(l,list):
                            for ll in l:
                                result.append(ll+'@'+rr)
                        else:
                            result.append(l+'@'+rr)
                else:
                    if isinstance(l,list):
                        for ll in l:
                            result.append(ll+'@'+r)
                    else:
                        result.append(l+'@'+r)
        return result
    elif isinstance(expression, MemberAccess):
        member_name=process_expression(expression.member_name)
        exp=process_expression(expression.expression)
        for l in member_name:
            for r in exp:
                if isinstance(r,list):
                    for rr in r:
                        if isinstance(l,list):
                            for ll in l:
                                result.append(ll+'@'+rr)
                        else:
                            result.append(l+'@'+rr)
                else:
                    if isinstance(l,list):
                        for ll in l:
                            result.append(ll+'@'+r)
                    else:
                        result.append(l+'@'+r)
        return result
    elif isinstance(expression,TemporaryVariable):
        node=expression.node
        result.extend(process_returns(node.expression))
    elif isinstance(expression,Node):
        result.extend(process_returns(expression.expression))
    else:
        result.append(ssa_name(expression))
    return result
def process_expression(expression):
    result = []
    if isinstance(expression, Literal):
        result.append(ssa_name(expression))
        return result
    elif isinstance(expression, LocalVariable):
        var_list=find_va_in_func(expression)
        if ssa_name(expression) not in var_list:
            var_list.append(ssa_name(expression))
        result.extend(var_list)
        return result
    elif isinstance(expression,Identifier):
        result.extend(process_expression(expression.value))
        return result 
    elif isinstance(expression, AssignmentOperation):
        expression_left=process_expression(expression.expression_left)
        expression_right=process_expression(expression.expression_right)
        result.extend(expression_left)
        result.extend(expression_right)
        return result
    elif isinstance(expression, CallExpression):
        result.extend(process_call_function(expression))
        return result
    elif isinstance(expression, IndexAccess):
        expression_left=process_expression(expression.expression_left)
        expression_right=process_expression(expression.expression_right)
        for l in expression_left:
            for r in expression_right:
                if isinstance(r,list):
                    for rr in r:
                        if isinstance(l,list):
                            for ll in l:
                                result.append(ll+'@'+rr)
                        else:
                            result.append(l+'@'+rr)
                else:
                    if isinstance(l,list):
                        for ll in l:
                            result.append(ll+'@'+r)
                    else:
                        result.append(l+'@'+r)
        return result
    elif isinstance(expression, MemberAccess):
        member_name=process_expression(expression.member_name)
        exp=process_expression(expression.expression)
        for l in member_name:
            for r in exp:
                if isinstance(r,list):
                    for rr in r:
                        if isinstance(l,list):
                            for ll in l:
                                result.append(ll+'@'+rr)
                        else:
                            result.append(l+'@'+rr)
                else:
                    if isinstance(l,list):
                        for ll in l:
                            result.append(ll+'@'+r)
                    else:
                        result.append(l+'@'+r)
        return result
    elif isinstance(expression, StateVariable):
        if hasattr(expression,'type') and hasattr(expression.type,'name'):
            result.extend([ssa_name(expression),str(expression.type.name)])
        else:
            result.append(ssa_name(expression))
        return result #【result】
    else:
        result.append(ssa_name(expression))
        return result
    
def process_condition(booleanExpression):
    result=process_condition_sub(booleanExpression)
    for ele in result:
        if 'isexcluded' in str(ele).lower():
            result=['NEQ', 'address', 'address(0)']
            break
        if 'exists(tokenId)' in str(ele).lower() or 'exists.tokenId' in str(ele).lower() or 'exists.address1' in str(ele).lower():
            if result[0]=='NOT':
                result=['NOT','_exists(tokenId)']
            else:
                result=['_exists(tokenId)']
            break
    if len(result)>=3 and result[2]=='address(0)' and isinstance(result[1],list) and result[1]!='address':
        result[1].append('address')
    if isinstance(booleanExpression,CallExpression):
        result=[result]
    return result
def process_condition_sub(booleanExpression):
    result = []
    if isinstance(booleanExpression, BinaryOperation):
        opType = translate_op_type(str(booleanExpression.type)) 
        left = process_condition_sub(booleanExpression.expression_left)
        right = process_condition_sub(booleanExpression.expression_right)
        result.append(str(opType))
        result.append(left)
        result.append(right)
        # return result 
    elif isinstance(booleanExpression, Literal):
        result.append(ssa_name(booleanExpression))
        # return result 
    elif isinstance(booleanExpression, TypeConversion):
        result.append(ssa_name(booleanExpression))
        # return result
    elif isinstance(booleanExpression, CallExpression):
        result.extend(process_call_function(booleanExpression))
        # return result
    elif isinstance(booleanExpression, UnaryOperation):
        opType = translate_op_type(str(booleanExpression.type)) 
        exp = booleanExpression.expression
        result.append(str(opType))
        result.append(process_condition_sub(exp))
        # return result
    elif isinstance(booleanExpression, Identifier):
        result.extend(process_expression(booleanExpression))
        # return result
    elif isinstance(booleanExpression, IndexAccess):
        expression_left=process_condition_sub(booleanExpression.expression_left)
        expression_right=process_condition_sub(booleanExpression.expression_right)
        for l in expression_left:
            for r in expression_right:
                if isinstance(r,list):
                    for rr in r:
                        if isinstance(l,list):
                            for ll in l:
                                result.append(ll+'@'+rr)
                        else:
                            result.append(l+'@'+rr)
                else:
                    if isinstance(l,list):
                        for ll in l:
                            result.append(ll+'@'+r)
                    else:
                        result.append(l+'@'+r)
        return result
    elif isinstance(booleanExpression, MemberAccess):
        member_name=process_condition_sub(booleanExpression.member_name)
        exp=process_condition_sub(booleanExpression.expression)
        for l in member_name:
            for r in exp:
                if isinstance(r,list):
                    for rr in r:
                        if isinstance(l,list):
                            for ll in l:
                                result.append(ll+'@'+rr)
                        else:
                            result.append(l+'@'+rr)
                else:
                    if isinstance(l,list):
                        for ll in l:
                            result.append(ll+'@'+r)
                    else:
                        result.append(l+'@'+r)
    elif isinstance(booleanExpression, TupleExpression):
        result.append(process_condition_sub(booleanExpression.expressions[0]))
    else:
        #add alais analysis
        # variable=booleanExpression.value
        result.append(ssa_name(booleanExpression).replace(" ", ""))
    return result   

# process in this function 
def find_va_in_func(exp):
    if isinstance(exp,CallExpression):
        return process_call_function(exp)
    if isinstance(exp,Identifier):
        return find_va_in_func(exp.value)
    if isinstance(exp,TypeConversion):
        return find_va_in_func(exp.expression)
    if not hasattr(exp,'signature_str'):
        return []
    exp_sign=exp.signature_str
    if not hasattr(exp,'function'):
        return []
    func=exp.function
    if not hasattr(func,'variables_read_or_written'):
        return []
    vars_list = []
    for var in func.variables_read_or_written:
        if not hasattr(var,'expression'):
            continue
        if var.signature_str!=exp_sign:
            continue
        if var.expression:
            vars=process_expression(var.expression)
            new_vars=[]
            for v in vars:
                if isinstance(v,list) and (len(v)>=1 and v[0] not in ['EQ','NEQ','GT','LT','GTE','LTE','AND','OR','NOT']):
                    new_vars.extend(v)
                else:
                    new_vars.append(v)
            vars=new_vars
            if vars==None:
                continue
            vars=[i for i in vars if i!='0']
            vars.append(ssa_name(var))
            vars_list.extend(vars)
    vars_list=remove_duplicates(vars_list)
    return vars_list


def processParas(function):
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




def convert2str(reqs):
    return [str(req) for req in reqs ]


def find_call_exp(node,func):
    if str(func) not in str(node):
        return None
    if isinstance(node,Node):
        return find_call_exp(node.expression,func)
    elif isinstance(node,AssignmentOperation):
        exp_left=find_call_exp(node.expression_left,func)
        exp_right=find_call_exp(node.expression_right,func)
        if exp_right:
            return exp_right
        else:
            return exp_left
    elif isinstance(node,BinaryOperation ):
        exp_left=find_call_exp(node.expression_left,func)
        exp_right=find_call_exp(node.expression_right,func)
        if exp_right:
            return exp_right
        else:
            return exp_left
    elif isinstance(node,CallExpression):
        return node
    elif isinstance(node,UnaryOperation) or isinstance(node,TypeConversion):
        return find_call_exp(node.expression,func)
    elif isinstance(node,IndexAccess ):
        exp_left=find_call_exp(node.expression_left,func)
        exp_right=find_call_exp(node.expression_right,func)
        if exp_right:
            return exp_right
        else:
            return exp_left
    elif isinstance(node,Identifier):
        return None
    elif node==None:
        return None
    else:
        raise Exception('type error')
        
def find_msg_sender(exp):
    if exp==None:
        return []
    source="msgsender"
    func=exp.called
    while not hasattr(func,'value'):
        func=func.expression
    if isinstance(func,LocalVariable):
        func=func.function
    vars_list = []
    if hasattr(func,'variables_read_or_written'):
        for var in func.variables_read_or_written:
            if not hasattr(var,'expression'):
                continue
            sign=var.signature_str
            sign=sign.replace('.','').lower()
            sign2=str(var.expression)
            sign2=sign2.replace('.','').lower()
            if (source not in sign) and (source not in sign2):
                continue
            if var.expression:
                vars=process_expression(var.expression)
                if vars==None:
                    continue
                vars.append(str(var))
                vars_list.extend(vars)
    for argu in exp.arguments:
        if str(argu)=='msg.sender':
            vars_list.append('msg.sender')
        elif isinstance(argu,CallExpression):
            vars=process_call_function(argu)
            for var in vars:
                if 'msg.sender' in var.lower() or 'msgsender' in var.lower():
                    vars_list.extend(vars)
                    vars_list.append('msg.sender')
        elif isinstance(argu,Identifier):
            var=argu.value
            if hasattr(var,'expression'):
                if 'msg.sender' in str(var.expression).lower() or 'msgsender' in str(var.expression).lower():
                    vars_list.append('msg.sender')          
        
    vars_list=list(set(vars_list))
    return vars_list


# rewrite findMsgSender Function
# find msg.sender in caller function 
def find_msg_sender_in_caller(caller, cfunction):
    source="msgsender"
    vars_list=[]
    if hasattr(caller,'variables_read_or_written'):
        for var in caller.variables_read_or_written:
            if not hasattr(var,'expression'):
                continue
            sign=var.signature_str
            sign=sign.replace('.','').lower()
            sign2=str(var.expression)
            sign2=sign2.replace('.','').lower()
            if (source not in sign) and (source not in sign2):
                continue
            if var.expression:
                vars=process_expression(var.expression)
                if vars==None:
                    continue
                vars.append(str(var))
                vars_list.extend(vars)
    caller_statement=None
    for node in caller.nodes_ordered_dominators:
        flag=False
        calls=node.low_level_calls+node.high_level_calls+node.internal_calls+node.library_calls
        for call_func in calls:
            if isinstance(call_func,tuple):
                call=call_func[1]
            else:
                call=call_func
            if not hasattr(call,'signature_str'):
                continue
            if call.signature_str == cfunction.signature_str and call.canonical_name == cfunction.canonical_name:
                flag=True
                break
        if flag:
            caller_statement=node
            break
    caller_expression=find_call_exp(caller_statement,cfunction)
    has_msgsender=False
    if caller_expression==None:
        return has_msgsender
    for argu in caller_expression.arguments:
        if str(argu)=='msg.sender':
            has_msgsender=True
        elif isinstance(argu,CallExpression):
            vars=process_call_function(argu)
            for var in vars:
                if 'msg.sender' in var.lower() or 'msgsender' in var.lower():
                    has_msgsender=True
        elif isinstance(argu,Identifier):
            var=argu.value
            if hasattr(var,'expression'):
                if 'msg.sender' in str(var.expression).lower() or 'msgsender' in str(var.expression).lower():
                    has_msgsender=True
        argu_str=str(argu)
        if 'msg.sender' in argu_str.lower() or 'msgsender' in argu_str.lower():
            has_msgsender=True
        for var in vars_list:
            if var in argu_str:
                has_msgsender=True
                break
    return has_msgsender

def msg_sender_in_require(func):
    if not isinstance(func,FunctionContract):
        return []
    flag_owner=False
    for node in func.nodes_ordered_dominators:
        
        if ('owner' in str(node))and ('msg.sender' in str(node).lower() or 'msgsender' in str(node).lower()) and '=' in str(node):
            flag_owner=True
        #msg.sender in caller function
        if node.calls_as_expression!=None and len(node.calls_as_expression)>0:
            if 'msg.sender' in str(node.calls_as_expression[0]).lower() or 'msgsender' in str(node.calls_as_expression[0]).lower():
                return ['msg.sender']
        if (('allowed' in str(node)) or ('allowance' in str(node)) or ('balance' in str(node)))and ('msg.sender' in str(node).lower() or 'msgsender' in str(node).lower()):
            return ['msg.sender']
        is_require_or_assert = node.contains_require_or_assert()
        if is_require_or_assert:
            nodestr=str(node)
            if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower() or ('owner' in nodestr.lower() and flag_owner):
                return ['msg.sender']
        is_if_statement=(node.type.name=='IF')
        if is_if_statement:
            nodestr=str(node)
            if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower() or ('owner' in nodestr.lower() and flag_owner):
                return ['msg.sender']
    for modifier in func.modifiers:
        for node in modifier.nodes_ordered_dominators:
            is_require_or_assert = node.contains_require_or_assert()
            if is_require_or_assert:
                nodestr=str(node)
                if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower():
                    return ['msg.sender']
            is_if_statement=(node.type.name=='IF')
            if is_if_statement:
                nodestr=str(node)
                if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower():
                    return ['msg.sender'] 
    return []           



def process_sub_with_process(exp):
    result=process_sub(exp)
    if result==None:
        return None
    else:
        is_allow='allow' in str(result[1])
        is_balance='balance' in str(result[1])
        if is_allow:
            result[1]=['_allowances@owner@spender','_allowances@from@spender','_allowances@from@msgsender','_allowances@owner@msgsender','allowance(owner,spender)','_allowances@address_1@address_2','_allowances@msgsender@spender']
        if is_balance:
            result[1]=['_balances@address_1','_balances@spender',
                 '_balances@owner','_balances@owner','_balances@from','_balances@account']
        return result

def process_sub(exp):
    for ir in exp.irs:
        if isinstance(ir,(InternalCall,HighLevelCall,LibraryCall)):
            if hasattr(ir,'function_name') and (hasattr(ir.function_name,'name')):
                if ir.function_name.name.lower()=="sub" or ir.function_name.name.lower()=="safesub":
                    return ['GTE', [ssa_name(ir.arguments[0])], [ssa_name(ir.arguments[1])], ["ERROR_MSG: sub error"]]
            elif hasattr(ir,'function_name') and (isinstance(ir.function_name,str) and (ir.function_name.lower()=='sub' or ir.function_name.lower()=='safesub')):
                return ['GTE', [ssa_name(ir.arguments[0])], [ssa_name(ir.arguments[1])], ["ERROR_MSG: sub error"]]

def check_req(reqs):
    res=[]
    for req in reqs:
        req_str=convert2str(req)
        errormsg=req[-1]
        flag=True
        if req==['Allowance checked in function but may underflow']:
            continue
        if 'allow' in str(req_str):
            flag=False
        if 'ERROR_MSG' in errormsg:
            if ('insufficient' in errormsg or 'below zero' in errormsg or 'exceeds balance' in errormsg or 'amount exceed' in errormsg or 'SafeCast' in errormsg or 'overflow' in errormsg) and flag:
                continue
            else:
                res.append(req)
        else:
            res.append(req)
    return res

def revert_if_statement(req):
    result=[]
    if isinstance(req[0],str) and (req[0]!='AND' and req[0]!='OR'):
        if req[0]=='EQ':
            result.append('NEQ')
        elif req[0]=='NEQ':
            result.append('EQ')
        elif req[0]=='GT':
            result.append('LTE')
        elif req[0]=='LT':
            result.append('GTE')
        elif req[0]=='GTE':
            result.append('LT')
        elif req[0]=='LTE':
            result.append('GT')
        elif req[0]=='NOT':
            pass
        else:
            result.append('NOT')
            result.append(req[0])
        result.extend(req[1:])
    elif isinstance(req[0],str) and (req[0]=='AND' or req[0]=='OR'):
        for r in req:
            if r=='AND':
                result.append('OR')
            elif r=='OR':
                result.append('AND')
            elif r=='NEQ':
                result.append('EQ')
            elif r=='GT':
                result.append('LTE')
            elif r=='LT':
                result.append('GTE')
            elif r=='GTE':
                result.append('LT')
            elif r=='LTE':
                result.append('GT')
            elif r=='NOT':
                pass
            else:
                result.append(r)
    else:
        result.append('NOT')
        result.extend(req)    
    return result

def process_or_and(expression,errormsg='ERROR_MSG'):
    result=[]
    if hasattr(expression,'type') and hasattr(expression.type,'name') and (expression.type.name=='OROR' or expression.type.name=='ANDAND'):
        left=process_or_and(expression.expression_left,errormsg)
        right=process_or_and(expression.expression_right,errormsg)
        result.append(left)
        result.append(right)
    elif isinstance(expression,TupleExpression):
        for exp in expression.expressions:
            result.extend(process_or_and(exp,errormsg))
    else:
        cond=process_condition(expression)
        if len(cond)<=1:
            result.extend(cond)
        else:
            if isinstance(cond[0],str) and cond[0] in ['EQ','NEQ','GT','LT','GTE','LTE','AND','OR','NOT','ADD','SUB','MUL','DIV','MOD','RM','LM','POWER','MsgSender']:
                result.extend(cond)
            else:
                result.append(cond)
        result.append(errormsg)
    return result

def contains_call_expression(node:Node,function:FunctionContract):
    if function==None:
        return None
    for ir in node.irs:
        if isinstance(ir,(InternalCall,LowLevelCall,HighLevelCall)):
            if ir.function.canonical_name==function.canonical_name and ir.function.signature_str==function.signature_str:
                return ir.expression
    return None


# variable_map={}
def variable_in_call_chain(function:FunctionContract,deep=0,variable_map={}):
    if not isinstance(function,FunctionContract):
        return []
    if function.contract in variable_map.keys() and function in variable_map[function.contract].keys():
        return variable_map[function.contract][function]
    if deep>10:
        return []
    vars_list = []
    if function.nodes==None or len(function.nodes)==0:
        return []
    for var in function.variables_read_or_written:
        if not hasattr(var,'expression'):
            continue
        if var.expression:
            #reprocess expression
            vars=process_expression(var.expression)
            new_vars=[]
            for v in vars:
                if isinstance(v,list):
                    continue
                if v.startswith('TMP_'):
                    continue
                else:
                    pass
                if '0' == v:
                    continue
                else:
                    pass
                if hasattr(var,'canonical_name'):
                    if '.' in v:
                        new_vars.append(v)
                    else:
                        new_vars.append(var.canonical_name.split('.')[0]+'.'+var.canonical_name.split('.')[1]+'.'+v)
                else: # if v.startswith('TMP_'):pass
                    new_vars.append(v)
            new_vars.append(ssa_name(var))
            # else:
            #     new_vars.append(ssaName(var))
            new_vars=list(set(new_vars))
            vars_list.append(new_vars)
        else:
            if ssa_name(var).startswith('TMP_'):
                continue
            vars_list.append([ssa_name(var)])
    for par in function.parameters:
        if ssa_name(par).startswith('TMP_'):
            continue
        vars_list.append([ssa_name(par)])
    unique_tuples = set(tuple(inner_list) for inner_list in vars_list)
    # Convert tuples back to lists
    vars_list = [list(t) for t in unique_tuples]
    cou={}
    for node in function.nodes:
        if node.high_level_calls+node.internal_calls+node.library_calls==[]:
            continue
        has_msgsender=False
        for ir in node.irs:
            if 'msgsender' in str(ir).lower() or 'msg.sender' in str(ir).lower():
                has_msgsender=True
            if isinstance(ir,(InternalCall,HighLevelCall,LibraryCall)):
                if ir.function.name=='sub' or ir.function.name=='safesub' or ir.function.name=='add' or ir.function.name=='safeadd' or ir.function.name=='mul' or ir.function.name=='safemul' or ir.function.name=='div' or ir.function.name=='safediv':
                    continue
                if isinstance(ir.function,StateVariable):
                    continue
                vars_in_call=variable_in_call_chain(ir.function,deep+1,variable_map)
                # if ir.function.contract not in variable_map.keys():
                #     variable_map[ir.function.contract]={}
                # variable_map[ir.function.contract][ir.function]=vars_in_call
                if ir.function in cou:
                    cou[ir.function]+=1
                else:
                    cou[ir.function]=1
                vars_in_call=add_ssa(vars_in_call,'#'+str(cou[ir.function]))

                for i in range(len(ir.arguments)):
                    if ssa_name(ir.arguments[i]).startswith('TMP_'):
                        if has_msgsender:
                            vars_in_call.append([ssa_name(ir.function.parameters[i])+'#'+str(cou[ir.function]),'msg.sender'])
                        continue
                    vars_in_call.append([ssa_name(ir.function.parameters[i])+'#'+str(cou[ir.function]),ssa_name(ir.arguments[i])])

                vars_list.extend(vars_in_call)
    vars_list=remove_duplicates(vars_list)
    union=UnionFind(vars_list)
    vars_list=union.to_lists()
    last=-1
    vars_list=remove_duplicates(vars_list)
    for i in range(5):
        num_of_strings = sum(len(inner_list) for inner_list in vars_list)
        if last==num_of_strings:
            break
        else:
            last=num_of_strings
            vars_list=combine_lists_optimization(vars_list)
    # vars_list=delete_ssa(vars_list)
    return vars_list
            
                    
def ssa_name(expression):
    if hasattr(expression,'canonical_name'):
        # if hasattr(expression,'ssa_name'):
        #     return expression.canonical_name.split('.')[0]+'.'+expression.canonical_name.split('.')[1]+'.'+expression.ssa_name
        # else:
        return expression.canonical_name
    elif hasattr(expression,'points_to'):
        return ssa_name(expression.points_to)
    else:
        return str(expression)
    
    
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
def deleteCanName(req_lists):
    new_req_lists=[]
    for req_list in req_lists:
        new_req_lists.append(deleteCanNameList(req_list))
    return new_req_lists
def deleteCanNameList(req_list):
    new_req_list=[]
    for req in req_list:
        if isinstance(req,list):
            new_req_list.append(deleteCanNameList(req))
        else:
            if 'ERROR_MSG' in req:
                new_req_list.append(req)
            if 'msg.sender' in req:
                req=req.replace('msg.sender','msgsender')
            deleted=deleteCanNameStr(req)
            if deleted not in new_req_list:
                new_req_list.append(deleted)
    return new_req_list
def deleteCanNameStr(req_str):
    if 'ERROR_MSG' in req_str:
        return req_str
    if req_str=='Strings.toHexString(uint256,uint256).value':
        return req_str
    if '@' in req_str:
        eles=req_str.split('@')
        new_req_str=''
        for ele in eles:
            new_ele=deleteCanNameStr(ele)
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


def parasName(function:FunctionContract):
    func_pars=processParas(function)
    para_list=[]
    for key in func_pars:
        para_list.append([func_pars[key],key])
    return para_list


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

def split_name(x):
    if x is None:
        return []
    x_withoutspace=x.split(',')
    x_without_=[]
    for item in x_withoutspace:
        if item=='':
            continue
        else:
            x_without_.extend(item.split('_'))
    x_without__=[]
    for item in x_without_:
        if item=='':
            continue
        else:
            x_without__.extend(item.split('-'))
    result=[]
    for item in x_without__:
        if item=='':
            continue
        else:
            result.extend(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', item)).split())
    return result


def add_ssa(lists,add_str):
    if isinstance(lists,list):
        new_list=[]
        for item in lists:
            new_list.append(add_ssa(item,add_str))
        return new_list
    else:
        # if function_name in lists:
        if '#' in lists:
            return lists
        else:
            return lists+add_str
        # else:
        #     return lists

def delete_ssa(lists):
    if isinstance(lists,list):
        new_list=[]
        for item in lists:
            new_list.append(delete_ssa(item))
        return new_list
    else:
        if '#' in lists:
            return lists.split('#')[0]
        else:
            return lists
        
def judge_direct_caller(function,caller):
    calls=caller.high_level_calls+caller.internal_calls+caller.library_calls
    for call in calls:
        if isinstance(call,tuple):
            call=call[1]
        if not hasattr(call,'canonical_name'):
            continue
        if call.canonical_name==function.canonical_name and call.signature_str==function.signature_str:
            return True
    return False
def split_signature(signature):
    # Extract the contact name
    contactname, rest = signature.split('.', 1)
    
    # Extract the function name
    functionname, rest = rest.split('(', 1)
    
    # Extract the parameters and the rest
    params, rest = rest.split(') returns(', 1)
    params = params.split(',')
    
    # Extract the return types
    returntypes = rest.rstrip(')').split(',')
    
    return [contactname, functionname, params, returntypes]
def match_sub_signature(t_sign,func,match_con_name=False):
    # splict t_sign
    t_con_name,t_func_name,t_params,t_return_types=split_signature(t_sign)
    t_func_name=t_func_name.replace('_','').lower()
    # con_name=func.contract.name
    # func_name=func.name
    
    # params=func.signature[1]
    # returns=func.signature[2]
    con_name,func_name,params,returns=split_signature(func)
    func_name=func_name.replace('_','').lower()
    if match_con_name:
        if not(con_name in t_con_name or t_con_name in con_name):
            return False
    if not(func_name in t_func_name and t_func_name in func_name):
        return False
    new_t_paras=[]
    if len(t_params)!=len(params):
        return False
    for i in range(len(t_params)):
        if t_params[i] in params:
            params.remove(t_params[i])
            i=i-1 if i>0 else 0
        else:
            new_t_paras.append(t_params[i])
    if len(new_t_paras):
        for t_para in new_t_paras:
            flag=False
            for para in params:
                if t_para in para or para in t_para or ('uint' in t_para and 'uint' in para):
                    params.remove(para)
                    flag=True
                    break
            if flag==False:
                return False
    new_t_ret=[]
    for i in range(len(t_return_types)):
        if t_return_types[i] in returns:
            returns.remove(t_return_types[i])
            i=i-1 if i>0 else 0
        else:
            new_t_ret.append(t_return_types[i])
    if len(new_t_ret):
        for t_ret in new_t_ret:
            flag=False
            for ret in returns:
                if t_ret in ret or ret in t_ret or ('unint' in t_ret and 'unint' in ret):
                    returns.remove(ret)
                    flag=True
                    break
            if flag==False:
                return False
    return True
            