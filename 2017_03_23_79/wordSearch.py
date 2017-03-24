ass Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if self.dfs(word, board, i, j):
                    return True
        return False
                
    def dfs(self, word, board, i, j):
        if len(word) == 0:
            return True
        if j < 0 or j > len(board[0])-1 or i < 0 or i > len(board)-1 or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        newWord = word[1:]
        if self.dfs(newWord, board, i+1, j) or self.dfs(newWord, board, i, j+1) or self.dfs(newWord, board, i-1, j) or self.dfs(newWord, board, i, j-1):
            board[i][j] = tmp
            return True
        board[i][j] = tmp
        return False
            
# reference: https://discuss.leetcode.com/topic/22788/python-dfs-solution-with-comments
# optimization: https://discuss.leetcode.com/topic/10263/python-dfs-solution
