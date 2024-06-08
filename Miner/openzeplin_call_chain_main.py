
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from function_call_graph import FunctionCallGraph
from slither import Slither
import json
from utils import variable_extend,paras_name,delete_can_name,remove_duplicates,get_func_direct_caller
from call_chain import *
from process_variables import variable_in_call_chain,variable_map,delete_ssa
from process_require import extract_require_from_call_chain
from process_before_caller import extract_before_caller
from tqdm import tqdm
from slither.core.declarations import SolidityFunction,Modifier
import subprocess
subprocess.run(f"solc-select use 0.8.9",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
opz_slither = Slither('./opz_code.sol')
opz_contracts = opz_slither.contracts
opz_callgraph=FunctionCallGraph(opz_contracts)
funcs=[]
for contract in opz_contracts:
    if contract.is_interface:
        continue
    if contract.name.startswith('$'):
        continue
    funcs.extend(contract.functions_and_modifiers)

call_graph=Graph()
call_graph.addAllEdges(opz_callgraph.edges)

for func in funcs:
    if func.is_shadowed or (func.contract.name not in func.canonical_name):
        funcs.remove(func)
cou=0
funcs=list(set(funcs))
for func in tqdm(funcs):
    if func.contract not in variable_map.keys():
        variable_map[func.contract]={}
    vars=variable_in_call_chain(func,0)
    vars=delete_ssa(vars)
    variable_map[func.contract][func]=vars
    
if True:
    func_def_req={}
    for func in tqdm(funcs):
        func_sign=func.canonical_name.split('.')[0]+'.'+func.signature_str
        if func_sign.startswith('IERC'):
            continue
        func_def=CallChain(call_graph,func)
        func_def.get_def_call_chain()
        try:
            require_list=extract_require_from_call_chain(func_def.defCallChains,True)
            require_list=variable_extend(require_list,variable_map[func.contract][func])
            paras=paras_name(func)
            require_list=variable_extend(require_list,paras)
            require_list=delete_can_name(require_list)
        except Exception as e:
            print(func_sign)
            print(e)
            continue
        require_list =remove_duplicates(require_list)
        func_def_req[func_sign] = require_list
    with open('./requirement.json','w') as f:
        json.dump(func_def_req,f,indent=4)  
    
    
    
    
# extract internal function call requirement
if True:
    calls_reqs={}
    for func in tqdm(funcs):

        falg=False
        if func.visibility != 'internal':
            continue
        func_sign=func.canonical_name.split('.')[0]+'.'+func.signature_str
        func_direct_callers = get_func_direct_caller(func_sign, opz_callgraph)
        call_req_dic={}
        for caller in func_direct_callers:
            if isinstance(caller, SolidityFunction):
                continue
            caller_sign=caller.canonical_name.split('.')[0]+'.'+caller.signature_str
            if caller_sign.startswith('$'):
                continue
            if caller.visibility == 'internal':
                continue
            if caller.visibility == 'private':
                continue
            call_req,need_to_extract=extract_before_caller(func,caller,variable_map[func.contract][func])
            for cfunc in need_to_extract:
                if isinstance(cfunc, Modifier):
                    crequire_list=extract_require_from_call_chain([cfunc],True)
                    crequire_list=delete_can_name(crequire_list)
                    if len(crequire_list)>0:
                        call_req.extend([crequire_list,str(cfunc)])
                elif isinstance(cfunc, SolidityFunction):
                    continue
                else:
                    cfunc_def=CallChain(call_graph,cfunc)
                    cfunc_def.get_def_call_chain()
                    crequire_list=extract_require_from_call_chain(cfunc_def.defCallChains,True)
                    if caller.contract in variable_map.keys() and caller in variable_map[caller.contract].keys():
                        crequire_list=variable_extend(crequire_list,variable_map[caller.contract][caller])
                    paras=paras_name(func)
                    crequire_list=variable_extend(crequire_list,paras)
                    crequire_list=delete_can_name(crequire_list)
                    call_req.extend(crequire_list)
            call_req=remove_duplicates(call_req)
            call_req_dic[caller_sign]=call_req
        if len(call_req_dic)>0:
            calls_reqs[func_sign]=call_req_dic
    with open('./calls_requirement.json','w') as f:
        json.dump(calls_reqs,f,indent=4)

            
        
    
