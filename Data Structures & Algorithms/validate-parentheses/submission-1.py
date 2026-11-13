class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in close_to_open: # If c is a closing bracket
                if stack and stack[-1] == close_to_open[c]: # Check if current opener matches
                    stack.pop() # Remove from stack if it matches
                else:
                    return False # Return false if it's a mistach
            else:
                stack.append(c) # Append if c is an opening bracket
        return True if not stack else False # Check if stack is empty and return True