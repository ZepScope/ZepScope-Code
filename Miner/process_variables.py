from variables_utils import *
from slither.slithir.operations.internal_call import InternalCall
from slither.slithir.operations.high_level_call import HighLevelCall
from slither.slithir.operations.library_call import LibraryCall
from slither.core.declarations.function_contract import FunctionContract
from slither.core.expressions.binary_operation import BinaryOperation
from slither.core.expressions.call_expression import CallExpression
from slither.core.expressions.type_conversion import TypeConversion
from slither.core.expressions.unary_operation import UnaryOperation
from slither.core.expressions.literal import Literal
from slither.core.expressions.identifier import Identifier
from slither.core.expressions.index_access import IndexAccess
from slither.core.expressions.member_access import MemberAccess
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.variables.local_variable import LocalVariable
from slither.slithir.variables.temporary import TemporaryVariable
from slither.core.expressions.tuple_expression import TupleExpression
from slither.core.variables.state_variable import StateVariable
from slither.core.cfg.node import Node
from utils import translate_op_type,remove_duplicates
variable_map={}
def variable_in_call_chain(function:FunctionContract,deep=0):
    global variable_map
    if function in variable_map.keys():
        return variable_map[function]
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
                if v.startswith('TMP_') or v.startswith('REF_'):
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
            if ssa_name(var).startswith('TMP_') or ssa_name(var).startswith('REF_'):
                continue
            vars_list.append([ssa_name(var)])
    for par in function.parameters:
        if ssa_name(par).startswith('TMP_') or ssa_name(par).startswith('REF_'):
            continue
        vars_list.append([ssa_name(par)])
    unique_tuples = set(tuple(inner_list) for inner_list in vars_list)
    # Convert tuples back to lists
    vars_list = [list(t) for t in unique_tuples]
    cou={}
    for node in function.nodes:
        if node.high_level_calls+node.internal_calls+node.library_calls==[]:
            continue
        for ir in node.irs:
            if isinstance(ir,(InternalCall,HighLevelCall,LibraryCall)):
                if ir.function.name=='sub' or ir.function.name=='safesub' or ir.function.name=='add' or ir.function.name=='safeadd' or ir.function.name=='mul' or ir.function.name=='safemul' or ir.function.name=='div' or ir.function.name=='safediv':
                    continue
                vars_in_call=variable_in_call_chain(ir.function,deep+1)
                if ir.function in cou:
                    cou[ir.function]+=1
                else:
                    cou[ir.function]=1
                vars_in_call=add_ssa(vars_in_call,'#'+str(cou[ir.function]))

                for i in range(len(ir.arguments)):
                    if ssa_name(ir.arguments[i]).startswith('TMP_') or ssa_name(ir.arguments[i]).startswith('REF_'):
                        continue
                    # vars_in_call.append([ssaName(ir.function.parameters[i]),ssaName(ir.arguments[i])])
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
    else:
        return str(expression)
    
def process_expression(expression):
    result = []
    if isinstance(expression, Literal):
        result.append(ssa_name(expression))
        return result
    elif isinstance(expression, LocalVariable):
        var_list=find_var_in_func(expression)
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
def process_call_function(function):
    result=[]
    if hasattr(function,'called'):
        called=function.called
    elif hasattr(function,'function'):
        called=function.function
    else:
        called=function
    result.append(ssa_name(function))
    arguments=[]
    for argument in function.arguments:
        arguments.append(ssa_name(argument))  
    if isinstance(called,Identifier):
        called=called.value
    if not isinstance(called,FunctionContract):
        return result
    arg_replace={}
    cou=0
    flag=True
    return_node=None
    for node in  called.nodes_ordered_dominators:
        strnode=str(node)
        if strnode.startswith('RETURN'):
            return_node=node
        if strnode.startswith('ENTRY_POINT') or strnode.startswith('RETURN'):
            continue
        else:
            flag=False
            break
    if not flag:
        return result
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
    for rv in re_value:
        if isinstance(rv,str) and rv.endswith('.'):
            re_value.remove(rv)
    if return_node!=None:
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
    return result
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
        for l in left:
            for r in right:
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
        # result.append(str(opType))
        # result.append(left)
        # result.append(right)
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

def process_condition(boolean_expression):
    result = []
    if isinstance(boolean_expression, BinaryOperation):
        opType = translate_op_type(str(boolean_expression.type)) 
        left = process_condition(boolean_expression.expression_left)
        right = process_condition(boolean_expression.expression_right)
        result.append(str(opType))
        result.append(left)
        result.append(right)
        # return result 
    elif isinstance(boolean_expression, Literal):
        result.append(ssa_name(boolean_expression))
        # return result 
    elif isinstance(boolean_expression, TypeConversion):
        result.append(ssa_name(boolean_expression))
        # return result
    elif isinstance(boolean_expression, CallExpression):
        result.extend(process_call_function(boolean_expression))
        # return result
    elif isinstance(boolean_expression, UnaryOperation):
        opType = translate_op_type(str(boolean_expression.type)) 
        exp = boolean_expression.expression
        result.append(str(opType))
        result.append(process_condition(exp))
        # return result
    elif isinstance(boolean_expression, Identifier):
        result.extend(process_expression(boolean_expression))
        # return result
    elif isinstance(boolean_expression, IndexAccess):
        expression_left=process_condition(boolean_expression.expression_left)
        expression_right=process_condition(boolean_expression.expression_right)
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
    elif isinstance(boolean_expression, MemberAccess):
        member_name=process_condition(boolean_expression.member_name)
        exp=process_condition(boolean_expression.expression)
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
    elif isinstance(boolean_expression, TupleExpression):
        result.append(process_condition(boolean_expression.expressions[0]))
    else:
        #add alais analysis
        # variable=booleanExpression.value
        result.append(ssa_name(boolean_expression).replace(" ", ""))
    return result

def find_var_in_func(exp):
    if isinstance(exp,CallExpression):
        return process_call_function(exp)
    if isinstance(exp,Identifier):
        return find_var_in_func(exp.value)
    if isinstance(exp,TypeConversion):
        return find_var_in_func(exp.expression)
    exp_sign=exp.signature_str
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
            if vars==None:
                continue
            vars=[i for i in vars if i!='0']
            vars.append(ssa_name(var))
            vars_list.extend(vars)
    vars_list=remove_duplicates(vars_list)
    return vars_list
def process_or_and(expression,errormsg='ERROR_MSG'):
    result=[]
    if hasattr(expression,'type') and hasattr(expression.type,'name') and (expression.type.name=='OROR' or expression.type.name=='ANDAND'):
        left=process_or_and(expression.expression_left,errormsg)
        right=process_or_and(expression.expression_right,errormsg)
        result.append(left)
        result.append(right)
    else:
        result.extend(process_condition(expression))
        result.append(errormsg)
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