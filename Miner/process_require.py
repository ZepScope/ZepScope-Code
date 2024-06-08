
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
from slither.core.declarations.function_contract import FunctionContract
from utils import translate_op_type,remove_duplicates
def extract_require_from_call_chain(callchain:list,extractError=False):
    require_list=[]
    for call in callchain:
        req_item=process_require(call,extractError)
        require_list.extend(req_item)
        for modifier in call.modifiers:
            if str(modifier)=='getRoleAdmin':
                continue
            # require_list.append([str(modifier)])
            modifier_req=process_require(modifier,extractError)
            require_list.extend(modifier_req)
    return require_list

def process_require(function,extractError=False,target_func=None, process_revert=True):
    hasRequire = []
    if not hasattr(function, 'nodes'):
        return hasRequire
    for node in function.nodes:
        if not process_revert:
            isRequireOrAssert = node.contains_require_or_assert()
            if isRequireOrAssert:
                if node.expression is not None:
                    requireArguments = node.expression.arguments
                    condition = requireArguments[0]
                    errorMsg = None 
                    if len(requireArguments)>1:
                        errorMsg = requireArguments[1]
                    if hasattr(condition,'type') and hasattr(condition.type,'name') and (condition.type.name=='ANDAND'):
                        result=process_or_and(condition,'ERROR_MSG:'+str(errorMsg))
                    else:
                        result = process_condition_require(condition)
                        if isinstance(condition,CallExpression):
                            result=[result]
                        if extractError:
                            result.append('ERROR_MSG:'+str(errorMsg))
                        result=[result]
                    req_item = []
                    req_item.extend(result)
                    hasRequire.extend(req_item)
        else:
            result=[]
            if hasattr(node,'type') and hasattr(node.type,'name') and node.type.name == 'EXPRESSION' and (' revert(' in str(node) or ' revert ' in str(node)):
                errorMsg=str(node)
                errorMsg=errorMsg.replace('EXPRESSION ','')
                errorMsg=errorMsg.replace('revert(string)','')
                errorMsg=errorMsg.replace('revert ','')
                target_nodes=node.fathers
                for tn in target_nodes:
                    if not hasattr(tn,'expression'):
                        continue
                    condition=tn.expression
                    if 'IF' in str(tn):
                        if hasattr(condition,'type') and hasattr(condition.type,'name') and (condition.type.name=='ANDAND'):
                            result=process_or_and(condition,'ERROR_MSG:'+str(errorMsg))
                            result=revert_list(result)
                        else:
                            result = process_condition_require(condition)
                            if isinstance(condition,CallExpression):
                                result=[result]
                            result=revert_list(result)
                            if extractError:
                                result.append('ERROR_MSG:'+str(errorMsg))
                            result=[result]
                        break
                    elif 'ELSE' in str(tn):
                        if hasattr(condition,'type') and hasattr(condition.type,'name') and (condition.type.name=='ANDAND'):
                            result=process_or_and(condition,'ERROR_MSG:'+str(errorMsg))
                        else:
                            result = process_condition_require(condition)
                            if isinstance(condition,CallExpression):
                                result=[result]
                            if extractError:
                                result.append('ERROR_MSG:'+str(errorMsg))
                            result=[result]
            else:
                continue
            req_item = []
            if result!=[]:
                req_item.extend(result)
                hasRequire.extend(req_item)
    # hasRequire=replaceVar(hasRequire,func_paras)
    # caller_au=msgsenderInRequire(function)
    # if len(caller_au)!=0:
    #     hasRequire.append(['MsgSender',caller_au,'Para Need to be MsgSender'])
    return hasRequire


def revert_list(listA):
    newA=[]
    if len(listA)!=3:
        return ['NOT'] + listA
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
def process_or_and(expression,errormsg='ERROR_MSG'):
    result=[]
    if hasattr(expression,'type') and hasattr(expression.type,'name') and (expression.type.name=='OROR' or expression.type.name=='ANDAND'):
        left=process_or_and(expression.expression_left,errormsg)
        right=process_or_and(expression.expression_right,errormsg)
        if not (isinstance(left[-1], str) and 'ERROR_MSG' in left[-1]):
            result.extend(left)
        else:
            result.append(left)
        if not (isinstance(right[-1], str) and 'ERROR_MSG' in right[-1]):
            result.extend(right)
        else:
            result.append(right)
    else:
        result.extend(process_condition_require(expression))
        result.append(errormsg)
    return result
def process_condition_require(booleanExpression):
    result = []
    if isinstance(booleanExpression, BinaryOperation):
        opType = translate_op_type(str(booleanExpression.type)) 
        left = process_condition_require(booleanExpression.expression_left)
        right = process_condition_require(booleanExpression.expression_right)
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
        result.extend(process_caller(booleanExpression))
        # return result
    elif isinstance(booleanExpression, UnaryOperation):
        opType = translate_op_type(str(booleanExpression.type)) 
        exp = booleanExpression.expression
        result.append(str(opType))
        result.append(process_condition_require(exp))
        # return result
    elif isinstance(booleanExpression, Identifier):
        result.extend(process_expression(booleanExpression))
        # return result
    elif isinstance(booleanExpression, IndexAccess):
        expression_left=process_condition_require(booleanExpression.expression_left)
        expression_right=process_condition_require(booleanExpression.expression_right)
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
        member_name=process_condition_require(booleanExpression.member_name)
        exp=process_condition_require(booleanExpression.expression)
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
        result.append(process_condition_require(booleanExpression.expressions[0]))
    else:
        #add alais analysis
        # variable=booleanExpression.value
        result.append(ssa_name(booleanExpression).replace(" ", ""))
    return result  

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
        isRequireOrAssert = node.contains_require_or_assert()
        if isRequireOrAssert:
            nodestr=str(node)
            if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower() or ('owner' in nodestr.lower() and flag_owner):
                return ['msg.sender']
        isIFStatement=(node.type.name=='IF')
        if isIFStatement:
            nodestr=str(node)
            if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower() or ('owner' in nodestr.lower() and flag_owner):
                return ['msg.sender']
    for modifier in func.modifiers:
        for node in modifier.nodes_ordered_dominators:
            isRequireOrAssert = node.contains_require_or_assert()
            if isRequireOrAssert:
                nodestr=str(node)
                if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower():
                    return ['msg.sender']
            isIFStatement=(node.type.name=='IF')
            if isIFStatement:
                nodestr=str(node)
                if 'msg.sender' in nodestr.lower() or 'msgsender' in nodestr.lower():
                    return ['msg.sender'] 
    return []           

def ssa_name(expression):
    if hasattr(expression,'canonical_name'):
        # if hasattr(expression,'ssa_name'):
        #     return expression.canonical_name.split('.')[0]+'.'+expression.canonical_name.split('.')[1]+'.'+expression.ssa_name
        # else:
        return expression.canonical_name
    else:
        return str(expression)
    
    
def process_caller(function):
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
    for rv in re_value:
        if isinstance(rv,str) and rv.endswith('.'):
            re_value.remove(rv)
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
    for i in ret_process:
        try:
            if i not in re_value:
                re_value.append(i)
        except:
            pass
    # re_value.extend(ret_process)
    result.extend(re_value)
    if len(result)==1:
        final_result.append(result[0])
    else:
        final_result.append(result)
    flag=False
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
        left = process_condition_require(expression.expression_left)
        right = process_condition_require(expression.expression_right)
        result.append(str(opType))
        result.append(left)
        result.append(right)
        return result 
    elif isinstance(expression, Node):
        result.extend(process_returns(expression.expression))
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
    else:
        result.append(ssa_name(expression))
    return result

def process_expression(expression):
    result = []
    if isinstance(expression, Literal):
        result.append(ssa_name(expression))
        return result
    elif isinstance(expression, LocalVariable):
        var_list=find_var_in_func(expression)
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
        result.extend(process_caller(expression))
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
    
def find_var_in_func(exp):
    if isinstance(exp,CallExpression):
        return process_caller(exp)
    if isinstance(exp,Identifier):
        return find_var_in_func(exp.value)
    if isinstance(exp,TypeConversion):
        return find_var_in_func(exp.expression)
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