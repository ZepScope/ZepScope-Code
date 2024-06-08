
import falcon.detectors.zep_checker.simliarity_compare as simliarity_compare
from falcon.detectors.zep_checker.utils import *
import falcon.detectors.zep_checker.info_match as info_match
def judgeHasRevert(index,all_nodes):
    if index==len(all_nodes):
        return False
    if_count=1
    for node in all_nodes[index:]:
        if if_count==0:
            break
        if 'revert' in str(node) or 'return' in str(node).lower():
            return True
        if node.type.name=='IF':
            if_count+=1
        if node.type.name=='ENDIF':
            if_count-=1
    return False
def processRequire(function,extractError=False,target_func=None):
    hasRequire = []
    if not hasattr(function, 'nodes'):
        return hasRequire
    for index,node in enumerate(function.nodes):
        isRequireOrAssert = node.contains_require_or_assert()
        if isRequireOrAssert:
            if node.expression is not None:
                requireArguments = node.expression.arguments
                condition = requireArguments[0]
                errorMsg = None 
                if len(requireArguments)>1:
                    errorMsg = requireArguments[1]
                if hasattr(condition,'type') and hasattr(condition.type,'name') and (condition.type.name=='ANDAND' or condition.type.name=='OROR'):
                    result=process_or_and(condition,'ERROR_MSG:'+str(errorMsg))
                else:
                    result = process_condition(condition)
                    if extractError:
                        result.append('ERROR_MSG:'+str(errorMsg))
                    result=[result]
                req_item = []
                req_item.extend(result)
                hasRequire.extend(req_item)
        call_expression = contains_call_expression(node, target_func)
        if call_expression:
            pass
        str_node=str(node)
        if node.type.name=='EXPRESSION' and 'allow' in str_node.lower() and (('msgsender' in str_node.lower() or 'msg.sender' in str_node.lower() or 'spender' in str_node.lower()) and '-' in str_node.lower()):
            hasRequire.append(['Allow Check Stastisfied'])
        if '.sub' in str_node or 'safesub' in str_node.lower():
            temp=process_sub_with_process(node)
            if temp!=None:
                hasRequire.append(temp)
        isIFStatement=(node.type.name=='IF') and (judgeHasRevert(index+1,function.nodes))
        if isIFStatement:
            IFArguments=node.expression
            if hasattr(IFArguments,'type') and hasattr(IFArguments.type,'name') and (IFArguments.type.name=='ANDAND' or IFArguments.type.name=='OROR'):
                tempresult=process_or_and(IFArguments,'ERROR_MSG: None')
                temp=[]
                result=[]
                for i in tempresult:
                    temp.append(i)
                    if 'ERROR_MSG' in i:
                        result.append(temp)
                        temp=[]
                    else:
                        if 'ERROR_MSG' in str(i):
                            result.extend(temp)
                            temp=[]
                        
            else:
                result=process_condition(IFArguments)
                if extractError:
                    result.append('ERROR_MSG: None')
                result=[result]
            result=[revert_if_statement(i) for i in result]
            hasRequire.extend(result)

    return hasRequire


    
def extractRequireFromCallChain(callchain:list,extractError=False):
    require_list=[]
    for call in callchain:
        req_item=processRequire(call,extractError)
        require_list.extend(req_item)
        if not hasattr(call, 'modifiers'):
            continue
        for modifier in call.modifiers:
            require_list.append([str(modifier)])
            if str(modifier).startswith('only'):
                continue
            elif 'owner' in str(modifier).lower() or 'admin' in str(modifier).lower() or 'role' in str(modifier).lower() or 'auth' in str(modifier).lower():
                require_list.append(['OnlyRole'])
            require_list.extend(processRequire(modifier,extractError))
    return require_list


def compareRequireWithFacts(require_list_del:list, facts_list:list):
    lack_require=[]
    for fact in facts_list:
        error_msg=fact[-1]
        if "ERROR_MSG" in error_msg and "None" not in error_msg:
            error_msg_fact=error_msg.replace("ERROR_MSG:","")
            if ':' in error_msg_fact:
                error_msg_fact=error_msg_fact.split(':')[1:]
                error_msg_fact=':'.join(error_msg_fact)
                error_msg_fact=error_msg_fact.strip()
            fact_str=fact[:-1]
        else:
            error_msg_fact=None
            fact_str=fact
        has_require=False
        for require in require_list_del:
            req_error_msg=require[-1]
            if isinstance(req_error_msg,list):
                for msg in req_error_msg:
                    if "ERROR_MSG" in msg and "None" not in msg:
                        error_msg=msg.replace("ERROR_MSG:","")
                        if ':' in error_msg:
                            error_msg=error_msg.split(':')[1:]
                            error_msg=':'.join(error_msg)
                            error_msg=error_msg.strip()
                    if "ERROR_MSG" in msg:
                        require_str=require[:-1]
                    else:
                        require_str=require
                    if compareStringsAndMsgs(require_str,fact_str,error_msg,error_msg_fact):
                        has_require=True
                        # require_list_del.remove(require)
                        break 
                if has_require:
                    break   
            else:
                if "ERROR_MSG" in req_error_msg and "None" not in req_error_msg:
                    error_msg_require=req_error_msg.replace("ERROR_MSG:","")
                    if ':' in error_msg_require:
                        error_msg_require=error_msg_require.split(':')[1:]
                        error_msg_require=':'.join(error_msg_require)
                        error_msg_require=error_msg_require.strip()
                    require_str=require[:-1]
                else:
                    error_msg_require=None
                    if "ERROR_MSG" in req_error_msg:
                        require_str=require[:-1]
                    else:
                        require_str=require
                if compareStringsAndMsgs(require_str,fact_str,error_msg_require,error_msg_fact):
                    has_require=True
                    # require_list_del.remove(require)
                    break
        facts_str=str(fact)
        if not has_require and (isinstance(fact[0],str) and (fact[0].startswith('only') or 'role' in fact[0].lower() or 'admin' in fact[0].lower())) or ('onlyrole' in facts_str.lower() or 'hasrole' in facts_str.lower()):
            for require in require_list_del:
                req_error_msg=str(require).lower()
                if 'hasrole' in req_error_msg or ('admin' in req_error_msg and 'role' in req_error_msg) or 'onlyrole' in req_error_msg or req_error_msg.startswith("['only"):
                    has_require=True
                    break
        if not has_require:
            lack_require.append(fact)
    # for require in lack_require:
    #     if len(require)<=2:
    #         for require_item in require_list:
    #             if len(require_item)==1:
    #                 if require_item==require[0] or require_item.startswith('only'):
    #                     lack_require.remove(require)
    #                 break     
    return lack_require


def check_require_in_call_chain(callchain,req_list,caller=None,extractError=False,variables=None,function=None):
    callchain_name=[str(call.name).lower() for call in callchain]
    if 'safetransfer' in function.name.lower():
        if '_transfer' not in callchain_name and 'transfer' not in callchain_name and 'transferfrom' not in callchain_name:
            return []
    require_list=extractRequireFromCallChain(callchain,extractError)
    has_only_check=False
    has_msg_sender_allowed=False
    has_array_check=False
    has_allow_check= True if ['Allow Check Stastisfied'] in require_list else False
    require_list=[x for x in require_list if x != ['Allow Check Stastisfied']]
    for req in require_list:
        req_str=str(req)
        if ('balance' in req_str.lower() or 'allow' in req_str.lower()) and ('msgsender' in req_str.lower() or 'msg.sender' in req_str.lower()):
        # if ('balance' in req_str.lower() or 'allow' in req_str.lower()) and ('msgsender' in req_str.lower() or 'msg.sender' in req_str.lower()):
            has_msg_sender_allowed=True
        if ('balance' in req_str.lower() or 'allow' in req_str.lower() or has_allow_check):
            has_array_check=True
        if len(req)==1 and isinstance(req[0],str)and ((req[0].lower()).startswith('only') or 'admin' in req[0].lower() or 'role' in req[0].lower() or 'auth' in req[0].lower()):
            has_only_check=True
        if len(req)==1 and isinstance(req[0],str)and (req[0].lower()).startswith('only') and 'mint' in function.name:
            require_list.append( [[
                "hasRole(MINTER_ROLE,_msgSender())",
                [
                    "REF_11975",
                    "members@_roles@role@account"
                ]
            ],
            "ERROR_MSG:ERC20: must have minter role to mint"])
        if 'whitelist' in req_str.lower() or 'permission' in req_str.lower():
            has_only_check=True
        if 'approvedorowner' in req_str.lower() or 'isapprovedforall' in req_str.lower() :
            has_only_check=True
        if 'isapprovedorowner' in req_str.lower():
            has_only_check=True
            require_list.append([
            [
                [
                    "EQ",
                    "_msgSender()",
                    "tokenId"
                ],
                "isApprovedForAll(_msgSender(),tokenId)",
                "isApprovedForAll(msgsender,tokenId)",
                "_operatorApprovals@_msgSender()@tokenId",
                "_operatorApprovals@msgsender@tokenId",
                [
                    "EQ",
                    "getApproved(tokenId)",
                    ["_msgSender()", "msgsender"]
                ]
            ],
            "ERROR_MSG:ERC721: caller is not token owner or approved"
        ]
            )
    # add find msgsender
    has_array_check=True and has_array_check
    require_list_extend_var=variable_extend(require_list,variables)
    paras=parasName(function)
    require_list_extend_paras=variable_extend(require_list_extend_var,paras)
    require_list_deleted=deleteCanName(require_list_extend_paras)
    lack_require=compareRequireWithFacts(require_list_deleted,req_list)
    has_msg_value=findMsgValue(callchain)
    has_msg_sender=find_msg_sender(function,caller,variables)
    has_msg_sender_function=msgsenderInfunction(function)
    # has_allow_in_function=allowInfunction(function)
    new_lack_require=[]
    for lack in lack_require:
        lack_str=str(lack)
        if 'address_' in lack_str and 'address(0)' in lack_str and has_msg_sender:
            pass
            # lack_require.remove(lack)
        elif 'incorrect owner' in lack_str.lower() and has_only_check:
            pass
        elif 'address(0)' in lack_str and has_array_check:
            pass
        elif 'allow' in lack_str and has_msg_sender:
            pass
        elif 'allow' in lack_str and has_allow_check:
            new_lack_require.append(['Allowance checked in function but may underflow'])
        # elif 'address(0)' in lack_str and has_allow_in_function and has_msg_sender:
        #     pass
        elif isCheckAccess(lack_str) and has_only_check:
            pass
            # lack_require.remove(lack)
        elif ('address(0)' in lack_str or 'address(this)' in lack_str) and 'msgsender' in lack_str.lower():
            # lack_require.remove(lack)
            pass
        elif (('isapproved' in lack_str.lower()) or ('isoperator' in lack_str.lower()) or ('msgsender' in lack_str.lower() and ('account' in lack_str.lower() or 'owner' in lack_str.lower()) and 'EQ' in lack_str)) and (has_only_check):
            pass
            # lack_require.remove(lack)
        elif has_msg_value and isCheckAccess(lack_str) :
            # lack_require.remove(lack)
            new_lack_require.append(['MsgValue Required'])
        elif (has_msg_sender or has_msg_sender_allowed or has_only_check) and isAddress_0(lack_str):
            # lack_require.remove(lack)
            new_lack_require.append(['Lack Addess(0) Check'])
        elif (has_msg_sender_function) and isAddress_0(lack_str):
            # lack_require.remove(lack)
            new_lack_require.append(['Lack Addess(0) Check: Not Clear'])
            
        elif has_only_check and 'invalid signature' in lack_str.lower():
            pass
        elif has_only_check and 'Para Need to be MsgSender' in lack_str:
            pass
        else:
            new_lack_require.append(lack)
    new_lack_require=remove_duplicates(new_lack_require)
    return new_lack_require

def compareStringsAndMsgs(require,fact,error_msg_require,error_msg_fact):
    if error_msg_require is None or error_msg_fact is None:
        return False
        if simliarity_compare.similarity_check_list(require,fact):
            return True
        else:
            return False
    if info_match.similarity(error_msg_require,error_msg_fact):
        return True
    else:
        #add
        return False
        if simliarity_compare.similarity_check_list(require,fact):
            return True
        else:
            return False
    
def check_argument(function,caller,def_lack_req,variables,EXTRACT_ERROR_MSG=False):
    hasmsgsender=find_msg_sender(function,caller,variables)
    final_lack=[]
    for fact in def_lack_req:
        if fact[0]=='MsgSender' and hasmsgsender:
            continue
        else:
            final_lack.append(fact)
    return final_lack


def find_msg_sender(function,caller,variables):
    caller_statement=None
    flag=False
    for call in caller.calls_as_expressions:
        if hasattr(call,'called') and hasattr(call.called,'value') and hasattr(call.called.value,'canonical_name'):
            if call.called.value.canonical_name==function.canonical_name and call.called.value.signature_str==function.signature_str:
                caller_statement=call
                break
        if hasattr(call,'called') and hasattr(call.called,'member_name'):
            if call.called.member_name==function.name:
                caller_statement=call
                break
    if caller_statement==None:
        for node in caller.nodes_ordered_dominators:
            for ir in node.irs:
                if isinstance(ir,(InternalCall,LibraryCall,HighLevelCall)):
                    if ir.function.canonical_name==function.canonical_name and ir.function.signature_str==function.signature_str:
                        caller_statement=ir
                        flag=True
                        break
            if flag:
                break
    hasmsgsender=False
    if caller_statement==None:
        return hasmsgsender
    argus=[]
    for argu in caller_statement.arguments:
        if hasattr(argu,'value'):
            argus.append(ssa_name(argu.value))
        else:
            argus.append(ssa_name(argu))
    # variables=deleteCanName(variables)
    new_argus=[]
    new_argus.extend(argus)
    for var in variables:
        for var_item in var:
            if var_item in argus:
                new_argus.extend(var)
                break
    # new_argus=deleteCanName(new_argus)
    for argu in new_argus:
        if 'msgsender' in argu.lower() or 'msg.sender' in argu.lower() or 'address(this)' in argu.lower():
            hasmsgsender=True
    return hasmsgsender

def msgsenderInfunction(function):
    for node in function.nodes:
        if 'msgsender' in str(node).lower() or 'msg.sender' in str(node).lower():
            return True
    return False
def allowInfunction(function):
    for node in function.nodes:
        if 'allowed' in str(node).lower() or 'allowance' in str(node).lower():
            return True
    return False

def findMsgValue(callchain):
    hasMsgValue=False
    for func in callchain:
        if not hasattr(func, 'nodes'):
            continue
        for node in func.nodes:
            node_str=str(node)
            if 'msg.value' in node_str.lower() or 'msgvalue' in node_str.lower():
                return True

    return hasMsgValue


def isCheckAccess(check_str):
    if 'onlyrole' in check_str.lower() or 'onlyRoleOrOpenRole' in check_str.lower() or 'onlyowner' in check_str.lower() or 'onlyGovernance' in check_str.lower() or 'hasrole' in check_str.lower() or 'admin' in check_str.lower() or 'role' in check_str.lower() or 'onlyproxy' in check_str.lower() or ('address(underlying())' in check_str.lower() and 'msgsender' in check_str.lower()):
        return True
    return False
    
def isAddress_0(check_str):
    if 'address(0)' in check_str.lower() and 'NEQ' in check_str:
        return True
    return False