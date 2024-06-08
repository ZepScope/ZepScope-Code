from collections import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.references = []  # List of (list index, string index) references

def insert(root, word, ref):
    """Insert a word into the trie along with its reference."""
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True
    node.references.append(ref)


def search_substrings(root, word):
    """Search for substrings of the word in the trie with updated conditions."""
    substrings = []
    for i in range(len(word)):
        node = root
        j = i
        while j < len(word) and word[j] in node.children:
            node = node.children[word[j]]
            if node.is_end_of_word:
                # Ensure that the character after the substring is neither a lowercase nor an uppercase letter
                if j + 1 == len(word) or (not word[j + 1].islower() and not word[j + 1].isupper()):
                    substrings.append((i, j, node.references))  # Starting and ending index of substring and its references
            j += 1
    return substrings



def aho_search_efficient(root, word, lists):
    """Efficiently search for patterns in the word using Aho-Corasick trie and gather match indices."""
    node = root
    matches = []
    
    i = 0
    while i < len(word):
        char = word[i]
        while node and char not in node.children:
            node = node.fail
        if not node:
            node = root
            i += 1
            continue
        node = node.children[char]
        
        temp = node
        while temp:
            if temp.end_of_word:
                for k, l in temp.references:
                    substring = lists[k][l]
                    if i + 1 == len(word) or (not word[i + 1].islower() and not word[i + 1].isupper()):
                        matches.append((i-len(substring)+1, i, k))
            temp = temp.fail
        i += 1
            
    return matches


def generate_replacements_conditional(word, matches, lists):
    """Generate replacement strings using the gathered match indices considering the canReplace condition."""
    if not matches:
        return [word]

    # Sort matches based on start index to handle replacements in order
    matches.sort(key=lambda x: x[0])

    # Filter overlapping matches
    non_overlap_matches = []
    prev_end = -1
    now_list_num=0
    for match in matches:
        start, end, list_idx = match
        if start > prev_end and can_replace(word[start:end+1], word):
            non_overlap_matches.append(match)
            # prev_end = end
        if start==0 and end==len(word)-1:
            now_list_num=list_idx   

    non_overlap_matches=list(set(non_overlap_matches))
    new_str_list=set()
    for item in non_overlap_matches:
        replace_sta=item[0]
        replace_end=item[1]
        list_num=item[2]
        if list_num<0 or list_num>=len(lists) or list_num==now_list_num or replace_sta==replace_end:
            continue 
        for replace_str in lists[list_num]:
            if replace_str==word:
                continue
            new_str_list.add(word[:replace_sta]+replace_str+word[replace_end+1:])
    with_replacement =set()
    for item in lists[now_list_num]:
        with_replacement.add(item)
    with_replacement=with_replacement.union(new_str_list)
    with_replacement=list(with_replacement)
        

    return with_replacement




def combine_lists_optimization(lists):
    root = build_aho_tree(lists)
    final_lists = []

    for sublist in lists:
        new_sublist = set(sublist)
        for string in sublist:
            matches = aho_search_efficient(root, string, lists)
            replacements = generate_replacements_conditional(string, matches, lists)
            new_sublist.update(replacements)
        final_lists.append(list(new_sublist))
        
    return final_lists

class AhoNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.end_of_word = False
        self.references = []

def build_aho_tree(lists):
    """Build the Aho-Corasick trie."""
    root = AhoNode()
    
    # Phase 1: Construct basic trie structure
    for i, sublist in enumerate(lists):
        for j, string in enumerate(sublist):
            node = root
            for char in string:
                if char not in node.children:
                    node.children[char] = AhoNode()
                node = node.children[char]
            node.end_of_word = True
            node.references.append((i, j))

    # Phase 2: Construct fail links
    queue = deque([root])
    while queue:
        current = queue.popleft()
        for char, child in current.children.items():
            if current == root:
                child.fail = root
            else:
                temp = current.fail
                while temp and char not in temp.children:
                    temp = temp.fail
                child.fail = temp.children[char] if temp else root
            queue.append(child)
    
    return root


class UnionFind:
    def __init__(self, lists_of_strs):
        self.str_to_id = {}
        self.id_to_str = {}
        count = 0
        

        for lst in lists_of_strs:
            for s in lst:
                if s not in self.str_to_id:
                    self.str_to_id[s] = count
                    self.id_to_str[count] = s
                    count += 1

        self.parent = [i for i in range(count)]
        self.rank = [0] * count


        for lst in lists_of_strs:
            for i in range(len(lst) - 1):
                self.union(lst[i], lst[i+1])

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, str1, str2):
        x = self.str_to_id[str1]
        y = self.str_to_id[str2]
        
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def to_lists(self):
        groups = {}
        for s in self.str_to_id.keys():
            root = self.find(self.str_to_id[s])
            if root not in groups:
                groups[root] = []
            groups[root].append(s)
        return [sorted(group) for group in groups.values()]
    
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



        
