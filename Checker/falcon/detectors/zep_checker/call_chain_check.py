from falcon.detectors.zep_checker.utils import *
from falcon.core.declarations.function_contract import FunctionContract
from falcon.core.declarations.solidity_variables import SolidityFunction
class CallChain():
    def __init__(self, callgraph:Graph, callFunction:FunctionContract):
        self.call_chain = callgraph
        self.reverse_call_chain = callgraph.reverse()
        self.call_function = callFunction
        self.call_chains = []
        self.def_call_chains = []
        self.direct_caller=[]
    def get_def_call_chain(self):
        self.def_call_chains = self.call_chain.BFS(self.call_function)
        for call in self.def_call_chains:
            if not hasattr(call, 'name'):
                continue
            if 'require' in call.name:
                self.def_call_chains.remove(call)
        return self.def_call_chains
    def get_call_chain(self):
        self.call_chains = self.reverse_call_chain.DFS(self.call_function)
        for call_chain in self.call_chains:
            for call in call_chain:
                if not hasattr(call, 'name'):
                    continue
                if 'require' in call.name or 'constructor' in call.name:
                    call_chain.remove(call)
                elif func_equal(call, self.call_function):
                    call_chain.remove(call)
            if len(call_chain)==0:
                self.call_chains.remove(call_chain)
        return self.call_chains
    def find_direct_caller(self):
        self.find_direct_caller_nr(self.call_function)

    def find_direct_caller_nr(self, callfunction):
        MAX_DEPTH = 10
        stack = [(callfunction, 1)]  # Each item is a tuple of (function, depth)

        while stack:
            current_function, depth = stack.pop()
            for node in self.reverse_call_chain.edges:
                now_node = node
                if type(now_node) == tuple:
                    now_node = now_node[1]
                if isinstance(now_node, SolidityFunction):
                    continue
                if not hasattr(now_node, 'signature_str'):
                    continue
                if func_equal(current_function, now_node):
                    if now_node.visibility == 'public' or now_node.visibility == 'external':
                        self.direct_caller.extend(self.reverse_call_chain.edges[node])
                    elif depth < MAX_DEPTH:
                        stack.append((now_node, depth + 1))
        return self.direct_caller

    