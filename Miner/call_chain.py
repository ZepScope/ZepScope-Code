
from slither.core.declarations.function_contract import FunctionContract
from slither.core.declarations.solidity_variables import SolidityFunction
from collections import defaultdict
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
def func_equal(func1, func2)->bool:
    if not(hasattr(func1,'signature_str') and hasattr(func2,'signature_str')):
        return False
    if func1.signature_str == func2.signature_str and func1.canonical_name == func2.canonical_name:
        return True
    else:
        return False
    
def judge_in(node, path)->bool:
    for n in path:
        if func_equal(n,node):
            return True
    return False

class CallChain():
    def __init__(self, callgraph:Graph, callFunction:FunctionContract):
        self.callChain = callgraph
        self.reverseCallChain = None
        self.callFunction = callFunction
        self.callChains = []
        self.defCallChains = []
        self.directCaller=[]
    def get_def_call_chain(self):
        self.defCallChains = self.callChain.BFS(self.callFunction)
        for call in self.defCallChains:
            if not hasattr(call, 'name'):
                continue
            if 'require' in call.name:
                self.defCallChains.remove(call)
        return self.defCallChains
    def get_call_chain(self):
        if self.reverseCallChain is None:
            self.reverseCallChain = self.callChain.reverse()
        self.callChains = self.reverseCallChain.DFS(self.callFunction)
        for callChain in self.callChains:
            for call in callChain:
                if not hasattr(call, 'name'):
                    continue
                if 'require' in call.name or 'constructor' in call.name:
                    callChain.remove(call)
                if func_equal(call, self.callFunction) and call in callChain:
                    callChain.remove(call)
            if len(callChain)==0:
                self.callChains.remove(callChain)
        return self.callChains
    def findDirectCaller(self):
        self.findDirectCaller_nr(self.callFunction)

    def findDirectCaller_nr(self, callfunction):
        MAX_DEPTH = 10
        stack = [(callfunction, 1)]
        while stack:
            current_function, depth = stack.pop()
            for node in self.reverseCallChain.edges:
                now_node = node
                if type(now_node) == tuple:
                    now_node = now_node[1]
                if isinstance(now_node, SolidityFunction):
                    continue
                if not hasattr(now_node, 'signature_str'):
                    continue
                if func_equal(current_function, now_node):
                    if now_node.visibility == 'public' or now_node.visibility == 'external':
                        self.directCaller.extend(self.reverseCallChain.edges[node])
                    elif depth < MAX_DEPTH:
                        stack.append((now_node, depth + 1))
        return self.directCaller

