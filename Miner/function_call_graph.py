# need to check use function signature or function name
import slither.core.expressions.expression
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.core.expressions.call_expression import CallExpression
from slither.core.declarations import SolidityFunction
from slither.slithir.operations.solidity_call import SolidityCall
from slither.slithir.operations.assignment import Assignment
from slither.slithir.operations.internal_call import InternalCall
from slither.slithir.operations.library_call import HighLevelCall
from slither.slithir.operations.low_level_call import LowLevelCall
from slither.core.cfg.node import Contract
from slither.slithir.operations.binary import Binary
from slither.slithir.operations.unary import Unary
from slither.slithir.operations.index import Index
from slither.slithir.operations.member import Member
from slither.slithir.variables.constant import Constant
from slither.slithir.variables.local_variable import LocalVariable
from slither.slithir.variables.reference import SolidityVariable
from slither.slithir.variables.temporary import TemporaryVariable
from slither.slithir.operations.return_operation import Return
from slither.slithir.variables.state_variable import StateVariable
from slither.slithir.operations.type_conversion import TypeConversion
from slither.slithir.operations.transfer import Transfer
from slither.slithir.operations.send import Send
from slither.core.expressions.member_access import MemberAccess
from slither.core.expressions.identifier import Identifier
from slither.core.solidity_types.user_defined_type import UserDefinedType
from enum import Enum

class FunctionGraphType(Enum):
    Call = 0
    Transfer = 1
    Relation = 2

class ABIFunctionType(Enum):
    EncodeWithSelector = 'abi.encodeWithSelector'
    EncodeWithSignature = 'abi.encodeWithSignature'
    EncodeCall = 'abi.encodeCall'
    Encode = 'abi.encode'
    Error = ""

# class FunctionCall:
#     # def __init__(self):
#     #     self.called_contract = None
#     #     self.called_function_name = ""
#     #     self.arguments = []
#     #     self.call_type = None
#     #     self.destination = None
#     #     self.caller_contract = None
#     #     self.caller_function_name = ""
#     def __int__(self,called_contract,called_function,arguments,call_type, destination, caller_contract,caller_function):
#         self.called_contract = called_contract
#         self.called_function_name = called_function
#         self.arguments = arguments
#         self.call_type = call_type
#         self.destination = destination
#         self.caller_contract = caller_contract
#         self.caller_function_name = caller_function

def ABIFuncType(func_name):
    if func_name == 'abi.encodeWithSelector' or func_name == 'abi.encodeWithSelector()':
        return ABIFunctionType.EncodeWithSelector
    if func_name == 'abi.encodeWithSignature' or func_name == 'abi.encodeWithSignature()':
        return ABIFunctionType.EncodeWithSignature
    if func_name == 'abi.encodeCall' or func_name == 'abi.encodeCall()':
        return ABIFunctionType.EncodeCall
    if func_name == 'abi.encode' or func_name == 'abi.encode()':
        return ABIFunctionType.Encode
    return ABIFunctionType.Error


class LowLevelCallInfo:
    def __init__(self, low_level_call: LowLevelCall, abi_map):
        self.call_name = ""
        self.call_function = None
        self.call_function_type = None
        self.call_name = low_level_call.function_name.name
        self.call_value = low_level_call.call_value
        self.call_gas = low_level_call.call_gas
        self.destination = low_level_call.destination
        self.call_function_arguments = []
        if len(low_level_call.arguments) == 0:
            self.call_function = None
        else:
            fst_arg = low_level_call.arguments[0]
            if isinstance(fst_arg,Constant):
                self.call_function = None
            else:
                if self.call_name == 'call' or self.call_name == 'staticcall' or self.call_name == 'delegatecall':
                    exp = low_level_call.expression
                    if isinstance(exp, CallExpression):
                        args = exp.arguments
                        index = 0
                        for arg in args:
                            if index == 0:
                                arg_call = args[0]
                                if isinstance(arg_call, CallExpression):
                                    called = arg_call.called
                                    if isinstance(called, MemberAccess):
                                        called_exp = called.expression
                                        if isinstance(called_exp, Identifier):
                                            called_value = called_exp.value
                                            if isinstance(called_value,
                                                          SolidityVariable) and called_value.name == 'abi':
                                                called_name = 'abi' + '.' + called.member_name
                                                parser = abiFuncParser(args[0], called_name)
                                                # print(parser)
                                                self.call_function = parser.get('name')
                                                self.call_function_arguments = parser.get('arguments')
                                                self.call_function_type = parser.get('type')
                                if isinstance(arg_call, Identifier):
                                    abi = abi_map.get(arg_call.value)
                                    if abi:
                                        self.call_function = abi.get('name')
                                        self.call_function_arguments = abi.get('arguments')
                                        self.call_function_type = abi.get('type')
                                    else:
                                        self.call_function_arguments.append(arg_call)
                            else:
                                self.call_function_arguments.append(arg)
                            index += 1
                # elif self.call_name == 'delegatecall':
                #     self.call_function_arguments = []
                #     index = 0
                #     for arg in low_level_call.arguments:
                #         if index == 0:
                #             abi = abi_map.get(arg)
                #             if abi:
                #                 self.call_function = abi.get('name')
                #                 self.call_function_arguments = abi.get('arguments')
                #                 self.call_function_type = abi.get('type')
                #         else:
                #             self.call_function_arguments.append(arg)
                #         index += 1
                #     print(self.call_name)

def abiFuncParser(call, called_name):
    encode_func_name = ''
    encode_func_type = None
    encode_args = []
    if isinstance(call, CallExpression):
        func_arg = None
        call_type = ABIFuncType(called_name)
        if call_type == ABIFunctionType.EncodeWithSelector:
            tag = 0
            for arg in call.arguments:
                if tag == 0:
                    func_arg = arg
                else:
                    encode_args.append(arg)
                tag += 1
            if func_arg:
                if isinstance(func_arg, MemberAccess):
                    func_arg = func_arg.expression
                    if isinstance(func_arg, MemberAccess):
                        encode_func_name = func_arg.member_name
                        arg_exp = func_arg.expression
                        encode_func_type = arg_exp.type
            # print(call)
        elif call_type == ABIFunctionType.EncodeWithSignature:
            # print(call)
            pass
        elif call_type == ABIFunctionType.EncodeCall:
            # print(call)
            pass
        elif call_type == ABIFunctionType.Encode:
            pass
            # print(call)
    if isinstance(call, SolidityCall):
        call_type = ABIFuncType(called_name)
        if call_type == ABIFunctionType.EncodeWithSelector:
            tag = 0
            for arg in call.arguments:
                if tag == 0:
                    func_arg = arg
                    if isinstance(func_arg, MemberAccess):
                        func_arg = func_arg.expression
                        if isinstance(func_arg, MemberAccess):
                            encode_func_name = func_arg.member_name
                            arg_exp = func_arg.expression
                            encode_func_type = arg_exp.type
                else:
                    encode_args.append(arg)
                tag += 1
        elif call_type == ABIFunctionType.EncodeWithSignature:
            index = 0
            encode_func_name = ""
            for arg in call.arguments:
                if index == 0:
                    encode_func_name = arg.name
                else:
                    encode_args.append(arg)
                index += 1
            # print(call)
        elif call_type == ABIFunctionType.EncodeCall:
            pass
            # print(call)
        elif call_type == ABIFunctionType.Encode:
            pass
            # print(call)
    return {'name': encode_func_name, 'type': encode_func_type, 'arguments': encode_args}

class FunctionCallType(Enum):
    InternalCall = 0
    HighLevelCall = 1
    LowLevelCall = 2

class FunctionCallNode:
    def __init__(self, contract, function_list):
        self.contract = contract
        self.functions = function_list
        self.calls = []

class FunctionCallEdge:
    def __init__(self,source, source_call, target, target_call, type: FunctionCallType):
        self.source = source
        self.target = target
        self.source_call = source_call
        self.target_call = target_call
        self.type = type

class FunctionGraph:
    def __init__(self, type, contracts) -> None:
        self.contract = contracts
        self.nodes = []
        self.edges = []
        self.type = type
        self.abstract_graph = None


class FunctionCallGraph(FunctionGraph):
    def __init__(self,contracts) -> None:
        FunctionGraph.__init__(self, FunctionGraphType.Call, contracts)
        nodes = []  # ["contract_name.func_name"]
        edges = []  # [<"contract_name.func_name","contract_name.call_func_name">]
        self.nodes = []  # [<Contract,[<func,call_func>]>]
        self.calls = []
        self.low_level_calls = []
        for contract in contracts:
            if contract.name.startswith("$"):
                continue
            node = FunctionCallNode(contract,contract.functions)
            call_list = []
            for function in contract.functions:
                # if isinstance(function,Modifier):
                #     continue
                if hasattr(function, 'name'):
                    if 'constructor' == function.name or 'ininialize' == function.name:
                        continue 
                if function.canonical_name.split('.')[0]!=contract.name:
                    continue
                nodes.append(contract.name + "." + function.name)
                for call in function.internal_calls:
                    # if isinstance(call,Modifier):
                    #     continue
                    if isinstance(call, SolidityFunction):
                        edge = FunctionCallEdge(contract.name + "." + function.name, function, "Solidity." + call.name, call, FunctionCallType.InternalCall)
                        edges.append((contract.name + "." + function.name, "Solidity." + call.name))
                        call_list.append(edge)

                    else:
                        edges.append((contract.name + "." + function.name, call.contract.name + "." + call.name))
                        edge = FunctionCallEdge(contract.name + "." + function.name, function, call.contract.name + "." + call.name,
                                                call, FunctionCallType.InternalCall)
                        call_list.append(edge)
                for call in function.high_level_calls:
                    # if isinstance(call,Modifier):
                    #     continue
                    if call[1]:
                        edges.append((contract.name + "." + function.name, call[0].name + "." + call[1].name))
                        edge = FunctionCallEdge(contract.name + "." + function.name, function,
                                                call[0].name + "." + call[1].name,
                                                call, FunctionCallType.HighLevelCall)
                    else:
                        call_val = call[0]
                        if isinstance(call_val, UserDefinedType):
                            edges.append((contract.name + "." + function.name, call_val.type.canonical_name))
                            edge = FunctionCallEdge(contract.name + "." + function.name, function,
                                                    call_val.type.canonical_name,
                                                    call, FunctionCallType.HighLevelCall)
                        else:
                            edges.append((contract.name + "." + function.name, call_val.name))
                            edge = FunctionCallEdge(contract.name + "." + function.name, function,
                                                    call_val.name,
                                                    call, FunctionCallType.HighLevelCall)
                    call_list.append(edge)
                # for call in function.low_level_calls:
                #     print(call)
                #     edges.append((contract.name+"."+function.name,call.contract.name + "." +call.name))
                #     call_list.append((function, call))
                low_level_calls = []
                abi_list= {}
                for ir in function.slithir_operations:
                    if isinstance(ir, SolidityCall):
                        func_name = ir.function.name
                        if ABIFuncType(func_name) != ABIFunctionType.Error:
                            abi = abiFuncParser(ir, func_name)
                            abi_list.setdefault(ir.lvalue,abi)
                            # print(ir)
                    if isinstance(ir, Assignment):
                        rv = ir.rvalue
                        for key in abi_list.keys():
                            if key == rv:
                                abi_list.setdefault(ir.lvalue,abi_list.get(key))
                                break
                    if isinstance(ir,LowLevelCall):
                        low_level_call = LowLevelCallInfo(ir, abi_list)
                        # print(low_level_call)
                        low_level_calls.append(low_level_call)
                        if low_level_call.call_function:
                            if low_level_call.call_function_type:
                                if isinstance(low_level_call.call_function_type, UserDefinedType):
                                    edges.append((contract.name + "." + function.name,
                                                  low_level_call.call_function_type.type.name + "." + low_level_call.call_function))
                                    edge = FunctionCallEdge(contract.name + "." + function.name, function,
                                                            low_level_call.call_function_type.type.name + "." + low_level_call.call_function,
                                                            low_level_call, low_level_call.call_name)
                                else:
                                    edges.append((contract.name + "." + function.name,
                                                  str(low_level_call.call_function_type) + "." + low_level_call.call_function))
                                    edge = FunctionCallEdge(contract.name + "." + function.name, function,
                                                            str(low_level_call.call_function_type) + "." + low_level_call.call_function,
                                                            low_level_call, low_level_call.call_name)
                                call_list.append(edge)
                            elif low_level_call.call_function:
                                edges.append((contract.name + "." + function.name,
                                              low_level_call.destination.name + "." + low_level_call.call_function))
                                edge = FunctionCallEdge(contract.name + "." + function.name, function,
                                                        low_level_call.destination.name + "." + low_level_call.call_function,
                                                        low_level_call,low_level_call.call_name)
                                call_list.append(edge)
                # print(low_level_calls)
                self.low_level_calls += low_level_calls
            # self.nodes.append((contract, call_list))
            node.calls = call_list
            self.nodes.append(node)
            self.edges += call_list
        self.abstract_graph = {"nodes": nodes, "edges": edges}
    def __str__(self):
        str = ""
        for key in self.abstract_graph.keys():
            edges = self.abstract_graph.get(key)
            for edge in edges:
                str += edge[0] + " --call--> " + edge[1] + "\n"
        return str

    def getCallFunctionName(self, function_key): # function_key = contract_name + . + function_name -> contract1.func1
        edges = self.abstract_graph.get(function_key)
        func_list = []
        for edge in edges:
            func_list.append(edge[1])
        return func_list

class FunctionRelationNode:
    def __init__(self, contract):
        self.contract = contract
        self.read_contracts = []
        self.write_contracts = []
        self.read_functions = []
        self.write_functions = []

class FunctionRelationGraph(FunctionGraph):
    def __init__(self,contracts):
        FunctionGraph.__init__(self, FunctionGraphType.Relation, contracts)
        for contract in contracts:
            self.nodes.append(FunctionRelationNode(contract))
    def addRelation(self, source_contract, target_contract, function_name, relation):
        for node in self.nodes:
            if node.contract.name == source_contract:
                if relation == 0:
                    node.read_contracts.append(target_contract)
                    node.read_contracts = list(set(node.read_contracts))
                    node.read_functions.append(function_name)
                elif relation == 1:
                    node.write_contracts.append(target_contract)
                    node.write_contracts = list(set(node.write_contracts))
                    node.write_functions.append(function_name)

class FunctionTransferGraph(FunctionGraph):
    def __init__(self,contracts) -> None:
        FunctionGraph.__init__(self, FunctionGraphType.Transfer, contracts)

        for contract in contracts:
            for function in contract.functions:
                for node in function.nodes:
                    for ir in node.irs:
                        if isinstance(ir,Transfer):
                            print(ir)
                        elif isinstance(ir,Send):
                            print(ir)
                print(function)

class TransferNode:
    def __init__(self):
        self.source = ""
        self.target = ""
        self.contract = None
        self.function = None


