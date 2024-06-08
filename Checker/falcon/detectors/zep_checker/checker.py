from falcon.detectors.abstract_detector import AbstractDetector, DetectorClassification
from falcon.detectors.zep_checker.function_call_graph import FunctionCallGraph
from falcon.detectors.zep_checker.call_chain_check import CallChain
from falcon.detectors.zep_checker.configs import *
from falcon.detectors.zep_checker.utils import *
from falcon.utils.output import Output
from typing import List
import copy
import falcon.detectors.zep_checker.check_require as check_require
class ZepChecker(AbstractDetector):
    ARGUMENT = 'zep-checker'

    IMPACT = DetectorClassification.MEDIUM
    CONFIDENCE = DetectorClassification.MEDIUM

    HELP = 'Check API usage of OpenZeppelin'
    WIKI = HELP
    WIKI_TITLE = 'MWE-999: zep-checker'
    WIKI_DESCRIPTION = HELP
    WIKI_RECOMMENDATION = HELP
    WIKI_EXPLOIT_SCENARIO = ''' '''
    
    def get_caller(self,call_graph,function):
        call_chain=CallChain(call_graph,function)
        call_chain.get_def_call_chain()
        call_chain.get_call_chain()
        caller_def_call_chain={}#{directed caller: def call chain的字典}
        flag_add={}#{function:has add private}
        if function.contract_declarer.contract_kind=='interface':
            return {}
        if (function.visibility=='public' or function.visibility=='external') and function.contract_declarer.contract_kind!='interface':
            caller_def_call_chain[function]=call_chain.def_call_chains
            flag_add[function]=False
        else:
            for callers in call_chain.call_chains:
                func_def_call_chian=[]+call_chain.def_call_chains
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
    def check(self,function,call_graph,requre_facts,sec=None,is_over8=False,caller_def_call_chain=None,variable_map=None):
        final_lack={}
        for caller in caller_def_call_chain.keys():
            if len(requre_facts)==0 and sec!=None:    
                sec_sign=sec.split('(')[0]
                sec_contract=sec_sign.split('.')[0]
                sec_func=sec_sign.split('.')[1]
                sec_contract_key=split_name(sec_contract)
                sec_func_key=split_name(sec_func)
                flag1=False
                flag2=False
                for word in sec_contract_key:
                    if 'ERC' in word and len(sec_contract_key)!=1:
                        continue
                    if word.lower() in caller.canonical_name.lower():
                        flag1=True
                        break
                for word in sec_func_key:
                    if word.lower() in caller.canonical_name.lower():
                        flag2=True
                        break
                if len(sec_contract_key)==1:
                    if sec_contract_key[0].lower() in caller.canonical_name.lower():
                        flag1=True
                if flag1 and flag2:
                # process sec match
                    final_lack[caller]=[]
                    continue
                else:
                    continue
            caller_def=CallChain(call_graph,caller)
            caller_def.get_def_call_chain()
            def_lack_req=check_require.check_require_in_call_chain(caller_def.def_call_chains,requre_facts,caller,EXTRACT_ERROR_MSG,variable_map[caller.contract][caller],function)
            if len(def_lack_req)!=0:
                direct_caller=caller
                for call in caller_def_call_chain[caller]:
                    if judge_direct_caller(function,call):
                        direct_caller=call
                        break
                def_lack_req=check_require.check_argument(function,direct_caller,def_lack_req,variable_map[caller.contract][caller],EXTRACT_ERROR_MSG)
            if is_over8:
                def_call_lack_req=check_req(def_lack_req)
            else:
                def_call_lack_req=def_lack_req
            final_lack[caller]=def_call_lack_req
        return final_lack
    def _detect(self) -> List[Output]:
        # cou=0
        # cou_all=0
        # for contract in self.contracts:
        #     for function in contract.functions:
        #         cou_all+=1
        #         if function.is_shadowed:
        #             continue
        #         if function.contract.name not in function.canonical_name:
        #             continue
        #         cou+=1
        # results = []
        # info=['total function: '+str(cou_all)+'\n','total function definition: '+str(cou)+'\n\n']
        # res=self.generate_result(info)
        # results.append(res)
        # return results
        results = []
        
        s_version=self.compilation_unit.solc_version
        split_s=s_version.split('.')
        is_over8=False
        if len(split_s)>1:
            int_version=int(split_s[1])
            is_over8=int_version > 7
        function_call_graph=FunctionCallGraph(self.contracts)
        call_graph=Graph()
        call_graph.addAllEdges(function_call_graph.edges)
        #{file:{func_sign:[req]}}
        def_req_file={}
        #{function_sign:[file_name]}
        file_name_set=set()
        func_signature_to_file={}
        for func in def_req.keys():
            file=func.split('.')[0]
            file_name_set.add(file)
            func_s=func.split('.')[1:]
            func_s='.'.join(func_s)
            if func_s not in func_signature_to_file:
                func_signature_to_file[func_s]=set()
            func_signature_to_file[func_s].add(file)
            if file in def_req_file.keys():
                def_req_file[file][func_s]=def_req[func]
            else:
                def_req_file[file]={}
                def_req_file[file][func_s]=def_req[func]
        call_req_file={}
        for func in call_req.keys():
            file=func.split('.')[0]
            file_name_set.add(file)
            func_s=func.split('.')[1:]
            func_s='.'.join(func_s)
            if func_s not in func_signature_to_file:
                func_signature_to_file[func_s]=set()
            func_signature_to_file[func_s].add(file)
            if file in call_req_file.keys():
                call_req_file[file][func_s]=call_req[func]
            else:
                call_req_file[file]={}
                call_req_file[file][func_s]=call_req[func]
        need_to_check_funcs={}
        func_flag={}
        for file in def_req_file.keys():
            if file not in func_flag.keys():
                func_flag[file]={}
                for func in def_req_file[file].keys():
                    if func not in func_flag[file].keys():
                        func_flag[file][func]=[]
        for file in call_req_file.keys():
            if file not in func_flag.keys():
                func_flag[file]={}
                for func in call_req_file[file].keys():
                    if func not in func_flag[file].keys():
                        func_flag[file][func]=[]
        func_flag_copy=copy.deepcopy(func_flag)
        all_related_contract={}
        for contract in self.contracts:
            for derived_contract in contract.derived_contracts:
                if derived_contract.name in all_related_contract.keys():
                    all_related_contract[derived_contract.name].append(contract.name)
                else:
                    all_related_contract[derived_contract.name]=[contract.name]
        for contract in self.contracts:
            if contract.contract_kind=='interface':
                continue
            func_flag=copy.deepcopy(func_flag_copy)
            for function in contract.functions:
                if function.is_shadowed:
                    continue
                if function.contract.name not in function.canonical_name:
                    continue
                if not isinstance(function,FunctionContract):
                    continue
                if contract.name in all_related_contract.keys():
                    related_name=all_related_contract[contract.name]
                else:
                    related_name=None
                func_def_req=check_target_function(function,def_req,contract_name=None,related_name=related_name,check_sub=True)
                func_call_req=check_target_function(function,call_req,contract_name=None,related_name=related_name,check_sub=True)
                # if len(func_def_req)+len(func_call_req)!=0 :
                if not (func_def_req==None and func_call_req==None):
                    if func_def_req==None:
                        func_def_req={}
                    if func_call_req==None:
                        func_call_req={}
                    need_to_check_funcs[function]=[func_def_req,func_call_req]
                    # continue
                func_signature=function.signature_str
                if not func_signature in func_signature_to_file.keys():
                    continue
                for file in func_signature_to_file[func_signature]:
                    if func_signature in func_flag.keys():
                        func_flag[file][func_signature].append(function)
                    else:
                        func_flag[file][func_signature]=[function]

            num_func_file={}
            for file in func_flag.keys():
                cou=0
                for func in func_flag[file].keys():
                    if len(func_flag[file][func])!=0:
                        cou+=1
                if 'ERC20Burnable' in file:
                    cou+=1
                num_func_file[file]=cou
            sorted_files_list=sorted(num_func_file.keys(), key=lambda x: (num_func_file[x],-len(x)),reverse=True)
            for file in sorted_files_list:
                if num_func_file[file] >= MATCH_NUM:
                    for func in func_flag[file].keys():
                        for t_func in func_flag[file][func]:
                            if t_func in need_to_check_funcs.keys():
                                continue
                            if t_func.contract_declarer.contract_kind=='interface':
                                continue
                            file_name=t_func.canonical_name.split('.')[0]
                            if file_name in file_name_set:
                                continue
                            tempfile=file
                            if file_name not in all_related_contract.keys():
                                related_names=[]
                            else:
                                related_names=all_related_contract[file_name]
                            if ('ERC20' in file_name and 'ERC20' not in file) or ('ERC20'==file_name and tempfile!='ERC20'):
                                tempfile = 'ERC20'
                            if ('BEP20' in file_name and 'ERC20' not in file and ('ERC721' in file or 'ERC1155' in file or 'ERC777' in file)) or ('BEP20'==file_name and tempfile!='ERC20'):
                                tempfile = 'ERC20'
                            if ('ERC721' in file_name and 'ERC721' not in file) or ('ERC721'==file_name and tempfile!='ERC721'):
                                tempfile = 'ERC721'
                            if ('ERC777' in file_name and 'ERC777' not in file) or ('ERC777'==file_name and tempfile!='ERC777'):
                                tempfile = 'ERC777'
                            if ('ERC1155' in file_name and 'ERC1155' not in file) or ('ERC1155'==file_name and tempfile!='ERC1155'):
                                tempfile = 'ERC1155'
                            for related in related_names:
                                if ('ERC20' in related and 'ERC20' not in file)  or ('ERC20'==file_name and tempfile!='ERC20'):
                                    tempfile = 'ERC20'
                                if ('BEP20' in related and 'ERC20' not in file and ('ERC721' in file or 'ERC1155' in file or 'ERC777' in file)) or ('BEP20'==file_name and tempfile!='ERC20'):
                                    tempfile = 'ERC20'
                                if ('ERC721' in related and 'ERC721' not in file) or ('ERC721'==file_name and tempfile!='ERC721'):
                                    tempfile = 'ERC721'
                                if ('ERC777' in related and 'ERC777' not in file) or ('ERC777'==file_name and tempfile!='ERC777'):
                                    tempfile = 'ERC777'
                                if ('ERC1155' in related and 'ERC1155' not in file) or ('ERC1155'==file_name and tempfile!='ERC1155'):
                                    tempfile = 'ERC1155'
                            func_def_req=check_target_function(t_func,def_req,contract_name=tempfile)
                            func_call_req=check_target_function(t_func,call_req,contract_name=tempfile)
                            # if len(func_def_req)+len(func_call_req)!=0 :
                            if func_def_req==None and func_call_req==None:
                                continue
                            if func_def_req==None:
                                func_def_req={}
                            if func_call_req==None:
                                func_call_req={}
                            if t_func not in need_to_check_funcs.keys():
                                need_to_check_funcs[t_func]=[func_def_req,func_call_req] 

            func_flag=copy.deepcopy(func_flag_copy)
            for function in contract.functions:
                if function.is_shadowed:
                    continue
                if function.contract.name not in function.canonical_name:
                    continue
                if not isinstance(function,FunctionContract):
                    continue
                if contract.name in all_related_contract.keys():
                    related_name=all_related_contract[contract.name]
                else:
                    related_name=None
                func_signature=function.signature_str
                func_signature_with_cname=function.contract.name+'.'+func_signature
                for t_func_sign in func_signature_to_file.keys():
                    t_func_sign_with_c_name='None.'+t_func_sign
                    if match_sub_signature(t_func_sign_with_c_name,func_signature_with_cname,match_con_name=False):
                        for file in func_signature_to_file[t_func_sign]:
                            if t_func_sign in func_flag.keys():
                                func_flag[file][t_func_sign].append(function)
                            else:
                                func_flag[file][t_func_sign]=[function]
            num_func_file={}
            for file in func_flag.keys():
                cou=0
                for func in func_flag[file].keys():
                    if len(func_flag[file][func])!=0:
                        cou+=1
                num_func_file[file]=cou
            sorted_files_list=sorted(num_func_file.keys(), key=lambda x: (num_func_file[x],-len(x)),reverse=True)
            for file in sorted_files_list:
                if num_func_file[file] >= MATCH_NUM:
                    for func in func_flag[file].keys():
                        for t_func in func_flag[file][func]:
                            if t_func in need_to_check_funcs.keys():
                                continue
                            if t_func.contract_declarer.contract_kind=='interface':
                                continue
                            file_name=t_func.canonical_name.split('.')[0]
                            if file_name in file_name_set:
                                continue
                            tempfile=file
                            if file_name not in all_related_contract.keys():
                                related_names=[]
                            else:
                                related_names=all_related_contract[file_name]
                            if ('ERC20' in file_name and 'ERC20' not in file) or ('ERC20'==file_name and tempfile!='ERC20'):
                                tempfile = 'ERC20'
                            if ('BEP20' in file_name and 'ERC20' not in file and ('ERC721' in file or 'ERC1155' in file or 'ERC777' in file)) or ('BEP20'==file_name and tempfile!='ERC20'):
                                tempfile = 'ERC20'
                            if ('ERC721' in file_name and 'ERC721' not in file) or ('ERC721'==file_name and tempfile!='ERC721'):
                                tempfile = 'ERC721'
                            if ('ERC777' in file_name and 'ERC777' not in file) or ('ERC777'==file_name and tempfile!='ERC777'):
                                tempfile = 'ERC777'
                            if ('ERC1155' in file_name and 'ERC1155' not in file) or ('ERC1155'==file_name and tempfile!='ERC1155'):
                                tempfile = 'ERC1155'
                            for related in related_names:
                                if ('ERC20' in related and 'ERC20' not in file)  or ('ERC20'==file_name and tempfile!='ERC20'):
                                    tempfile = 'ERC20'
                                if ('BEP20' in related and 'ERC20' not in file and ('ERC721' in file or 'ERC1155' in file or 'ERC777' in file)) or ('BEP20'==file_name and tempfile!='ERC20'):
                                    tempfile = 'ERC20'
                                if ('ERC721' in related and 'ERC721' not in file) or ('ERC721'==file_name and tempfile!='ERC721'):
                                    tempfile = 'ERC721'
                                if ('ERC777' in related and 'ERC777' not in file) or ('ERC777'==file_name and tempfile!='ERC777'):
                                    tempfile = 'ERC777'
                                if ('ERC1155' in related and 'ERC1155' not in file) or ('ERC1155'==file_name and tempfile!='ERC1155'):
                                    tempfile = 'ERC1155'
                            t_func_sign=t_func.contract.name+'.'+func
                            func_def_req=check_target_function_sign(t_func_sign,def_req,contract_name=tempfile)
                            func_call_req=check_target_function_sign(t_func_sign,call_req,contract_name=tempfile)
                            # if len(func_def_req)+len(func_call_req)!=0 :
                            if func_def_req==None and func_call_req==None:
                                continue
                            if func_def_req==None:
                                func_def_req={}
                            if func_call_req==None:
                                func_call_req={}
                            if t_func not in need_to_check_funcs.keys():
                                need_to_check_funcs[t_func]=[func_def_req,func_call_req]          
        final_check={}
        for func in need_to_check_funcs.keys():
            lenth=len(need_to_check_funcs[func][0])+len(need_to_check_funcs[func][1])
            if lenth!=0:
                final_check[func]=need_to_check_funcs[func]
        need_to_check_funcs=final_check
        caller_map={}
        all_caller=set()
        for function in need_to_check_funcs:
            caller_map[function]=self.get_caller(call_graph,function)
            for caller in caller_map[function].keys():
                all_caller.add(caller)
        # print('get caller time:',time.time()-stime)
        variable_map={}
        for caller in all_caller:
            if caller.is_shadowed:
                continue
            if caller.contract not in variable_map.keys():
                variable_map[caller.contract]={}
            cvars=variable_in_call_chain(caller,0,caller_map)
            cvars=delete_ssa(cvars)
            variable_map[caller.contract][caller]=cvars
        for func in need_to_check_funcs:
            if func.is_shadowed:
                continue
            if func.contract not in variable_map.keys():
                variable_map[func.contract]={}
            if func not in variable_map[func.contract].keys():
                fcvars=variable_in_call_chain(func,0,caller_map)
                fcvars=delete_ssa(fcvars)
                variable_map[func.contract][func]=fcvars
        # print('get variabile time:',time.time()-stime)
        # function_Set=set()
        # info_set=set()
        for function in need_to_check_funcs:
            # function_signature=function.signature_str
            # function_canonical_name=function.canonical_name
            # function_contract_name=function.contract.name
            # if function_signature+' '+function_canonical_name+' '+function_contract_name in function_Set:
            #     continue
            # function_Set.add(function_signature+' '+function_canonical_name+' '+function_contract_name)
            if function.is_shadowed:
                continue
            if len(function.nodes)==0:
                continue
            if '@openzeppelin' in function.source_mapping.filename.relative:
                continue
            func_def_req=need_to_check_funcs[function][0]
            func_call_req=need_to_check_funcs[function][1]
            final_lacks_def_req=self.check(function,call_graph,func_def_req,sec=None,is_over8=is_over8,caller_def_call_chain=caller_map[function],variable_map=variable_map)
            sec_lack={}#{caller:{sec:lack}}
            for sec in func_call_req.keys():
                caller_req=func_call_req[sec]
                final_lacks_call_req=self.check(function,call_graph,caller_req,sec=sec,is_over8=is_over8,caller_def_call_chain=caller_map[function],variable_map=variable_map)
                for caller in final_lacks_call_req.keys():
                    if caller in sec_lack:
                        sec_lack[caller][sec]=final_lacks_call_req[caller]
                    else:
                        sec_lack[caller]={sec:final_lacks_call_req[caller]}
            info=[function]
            for caller in sec_lack.keys():
                lack=min(sec_lack[caller].values(),key=len)
                if len(lack)!=0:
                    if len(caller.source_mapping.lines)==0:
                        continue
                    lack_list=[' '.join(convert2str(ll)) for ll in sec_lack[caller].values()]
                    lack_str=' '.join(lack_list)
                    info.append('\nlack caller check: \n'+lack_str+' in caller: '+ caller.canonical_name+ "\n")
                    # start=str(caller.source_mapping.lines[0])
                    # end=str(caller.source_mapping.lines[-1]) 
                    # if start==end:
                    #     continue
                    # info_str='\nlack caller check: \n'+lack_str+' in caller: '+ caller.canonical_name+ "("+ start +'-'+end+')'+ '\n'
                    # if info_str in info_set:
                    #     continue
                    # info_set.add(info_str)
                    # info.append(info_str)
                    # info=['lack check : '+' '.join(convert2str(lack))+' in caller: ',caller, 'of API function: '+function.canonical_name.split('.')[0]+'.'+function.signature_str+' \n']
                    # res=self.generate_result(info)
                    # results.append(res)
            # print('check time:',time.time()-stime)
            for caller in final_lacks_def_req.keys():
                def_call_lack_req=final_lacks_def_req[caller]
                if len(def_call_lack_req)!=0:
                    if len(caller.source_mapping.lines)==0:
                        continue
                    info.append('\nlack def check: \n'+' '.join(convert2str(def_call_lack_req))+' in caller: '+ caller.canonical_name+ "\n")

                    # start=str(caller.source_mapping.lines[0])
                    # end=str(caller.source_mapping.lines[-1]) 
                    # if start==end:
                    #     continue
                    # info_str='\nlack def check: \n'+' '.join(convert2str(def_call_lack_req))+' in caller: '+ caller.canonical_name+ "("+ start +'-'+end+')'+ "\n"
                    # if info_str in info_set:
                    #     continue
                    # info_set.add(info_str)
                    # info.append(info_str)
                    # info=['lack def check : '+' '.join(convert2str(def_call_lack_req))+' in caller: ',caller, 'of API function: '+function.canonical_name.split('.')[0]+'.'+function.signature_str+' \n']
                    # res=self.generate_result(info)
                    # results.append(res)
            
            if len(info)>1:
                info.append('\n\n')
                res=self.generate_result(info)
                results.append(res)
        return results

