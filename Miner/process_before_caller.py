from slither.slithir.operations.internal_call import InternalCall
from slither.slithir.operations.high_level_call import HighLevelCall
from slither.slithir.operations.library_call import LibraryCall
from slither.core.expressions.binary_operation import BinaryOperation
from slither.core.expressions.call_expression import CallExpression
from slither.core.expressions.type_conversion import TypeConversion
from slither.core.expressions.unary_operation import UnaryOperation
from slither.core.expressions.index_access import IndexAccess
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.cfg.node import Node
from slither.core.expressions.identifier import Identifier
from slither.core.expressions.literal import Literal
from slither.core.expressions.member_access import MemberAccess
from slither.core.expressions.tuple_expression import TupleExpression
from slither.core.variables.local_variable import LocalVariable
from process_require import process_or_and,process_condition_require,process_expression,process_caller,find_var_in_func,revert_list
from utils import variable_extend,paras_name,delete_can_name
import re
def extract_before_caller(func,caller,variables, extractError=True):
    hasRequire = []
    if not hasattr(caller, 'nodes'):
        return hasRequire
    need_to_extact_func=[]
    last_caller=None
    caller_exp=None
    flag=False
    for node in caller.nodes_ordered_dominators:
        # calls=node.high_level_calls+node.internal_calls+node.library_calls
        for ir in node.irs:
            if isinstance(ir,(InternalCall,LibraryCall,HighLevelCall)):
                if ir.function.canonical_name==func.canonical_name and ir.function.signature_str==func.signature_str:
                    caller_exp=ir.expression
                    flag=True
                    break
                else:
                    if ir.function.visibility=='internal' or ir.function.visibility=='private':
                        last_caller=ir.function
        if flag:
            break
    caller_statement=find_call_exp(caller_exp,func)
    caller_exp=None
    between_flag=(last_caller==None)
    for node in caller.nodes_ordered_dominators:
        for ir in node.irs:
            if isinstance(ir,(InternalCall,LibraryCall,HighLevelCall)):
                if last_caller!=None and ir.function.canonical_name==last_caller.canonical_name and ir.function.signature_str==last_caller.signature_str:
                    between_flag=True
                if ir.function.canonical_name==func.canonical_name and ir.function.signature_str==func.signature_str:
                    caller_exp=ir.expression
                    break
                else:
                    if judge_related(caller_statement,node.variables_read+node.variables_written) or between_flag:
                        need_to_extact_func.append(ir.function)
        if caller_exp!=None:
            break
        isRequireOrAssert = node.contains_require_or_assert()
        is_related=True
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
                    if extractError:
                        result.append('ERROR_MSG:'+str(errorMsg))
                    result=[result]
                paras=extract_paras_in_require(condition)
                is_related=judge_related(caller_statement,paras)
                req_item = []
                req_item.extend(result)
                if is_related or between_flag:
                    hasRequire.extend(req_item)
        else:
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
                        
                        paras=extract_paras_in_require(condition)
                        is_related=judge_related(caller_statement,paras)
                        req_item = []
                        req_item.extend(result)
                        if is_related or between_flag:
                            hasRequire.extend(req_item)
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
                        paras=extract_paras_in_require(condition)
                        is_related=judge_related(caller_statement,paras)
                        req_item = []
                        req_item.extend(result)
                        if is_related or between_flag:
                            hasRequire.extend(req_item)
            else:
                continue
    require_list=hasRequire
    #### comments
    # caller_au=findMsgSender(caller_exp)
    # if len(caller_au)!=0:
    #     hasRequire.append(['MsgSender',caller_au,'Para Need to be MsgSender'])
    require_list=variable_extend(require_list,variables)
    paras=paras_name(func)
    require_list=variable_extend(require_list,paras)
    require_list=delete_can_name(require_list)
    return hasRequire,need_to_extact_func
def find_call_exp(node,func):
    if str(func) not in str(node):
        return None
    if isinstance(node,(InternalCall,LibraryCall,HighLevelCall)):
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
    
def extract_paras_in_require(booleanExpression):
    result = []
    if isinstance(booleanExpression, BinaryOperation):
        left = extract_paras_in_require(booleanExpression.expression_left)
        right = extract_paras_in_require(booleanExpression.expression_right)
        result.extend(left)
        result.extend(right)
        # return result 
        # return result 
    elif isinstance(booleanExpression, TypeConversion):
        result.append(booleanExpression)
        # return result
    elif isinstance(booleanExpression, CallExpression):
        result.append(booleanExpression)
        result.extend(booleanExpression.arguments)
        # return result
    elif isinstance(booleanExpression, UnaryOperation):
        exp = booleanExpression.expression
        result.append(extract_paras_in_require(exp))
        # return result
    elif isinstance(booleanExpression, Identifier):
        result.append(booleanExpression)
        # return result
    elif isinstance(booleanExpression, IndexAccess):
        expression_left=extract_paras_in_require(booleanExpression.expression_left)
        expression_right=extract_paras_in_require(booleanExpression.expression_right)
        result.extend(expression_left)
        result.extend(expression_right)
    elif isinstance(booleanExpression, MemberAccess):
        member_name=extract_paras_in_require(booleanExpression.member_name)
        exp=extract_paras_in_require(booleanExpression.expression)
        result.extend(member_name)
        result.extend(exp)
    elif isinstance(booleanExpression, TupleExpression):
        result.append(extract_paras_in_require(booleanExpression.expressions[0]))
    elif isinstance(booleanExpression,LocalVariable):
        result.append(booleanExpression)
    return result   

def find_msg_sender(exp):
    if exp==None:
        return []
    source="msgsender"
    func=exp.called
    while not hasattr(func,'value'):
        if hasattr(func,'expression'):
            func=func.expression
        else:
            break
    if isinstance(func,CallExpression):
        func=func.called
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
            vars=process_caller(argu)
            vars=flatten(vars)
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

def judge_related(call:CallExpression,paras):
    call_argus=[]
    for argu in call.arguments:
        argu=str(argu)
        call_argus.extend(split_argu(argu))
    for para in paras:
        para=find_var_in_func(para)
        para=flatten(para)
        if isinstance(para,list):
            temp=[]
            for p in para:
                temp.extend(split_argu(p))
            para=temp
        else:
            para=split_argu(para)
        for argu in call_argus:
            if argu in para:
                return True
        return False
def split_argu(argu):
    pattern=r'[.,()\[\]_=\+\-\*/]'
    if argu=='msg.sender':
        return ['msg.sender']
    argu=re.split(pattern, argu)
    argu=[a.strip() for a in argu if a.strip()!='']
    return argu
def flatten(mixed_list):
    flat_list = []
    for item in mixed_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list