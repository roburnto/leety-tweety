# Last updated: 1/12/2026, 1:41:29 PM
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # Build graph of synonyms
        graph = defaultdict(list)
        for word1, word2 in synonyms:
            graph[word1].append(word2)
            graph[word2].append(word1)
        
        # Perform BFS to find all synonyms for a given word
        def find_synonyms(word):
            visited = set()
            queue = deque([word])
            synonyms_set = set()
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    synonyms_set.add(current)
                    queue.extend(graph[current])
            return sorted(synonyms_set)  # Return sorted synonyms
        
        # Build a mapping of each word to its synonyms
        synonym_map = {}
        for word in graph:
            if word not in synonym_map:
                synonyms = find_synonyms(word)
                for synonym in synonyms:
                    synonym_map[synonym] = synonyms

        # Split the input text into words
        words = text.split()

        # Backtracking to generate all sentences
        result = []

        def backtrack(index, path):
            if index == len(words):
                result.append(" ".join(path))
                return
            
            word = words[index]
            if word in synonym_map:
                for synonym in synonym_map[word]:
                    backtrack(index + 1, path + [synonym])
            else:
                backtrack(index + 1, path + [word])
        
        backtrack(0, [])
        return sorted(result)  # Return sorted sentences
