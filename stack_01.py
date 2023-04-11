class Solution():
    """
    @param s: a string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        stack = []
        for ch in s:
            # push in stack
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    # stack is empty
                    return False
                if ch == ']' and stack[-1] != '[' or ch == '}' and stack[-1] == '{' or ch == ')' and stack[-1] != '(':
                    return False

                # pop the stack
                stack.pop()
        return not stack  # if stack is empty return True, else return False


input = Solution()
#input.isValidParentheses('(){}[]')
input.isValidParentheses('(}[{')
