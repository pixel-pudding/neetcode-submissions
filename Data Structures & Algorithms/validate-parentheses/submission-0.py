class Solution:
    def isValid(self, s: str) -> bool:
        bracket = []  # stack to store opening brackets

        for char in s: #iterating through all the characters int he string
            
            # If we encounter an opening bracket
            if char == '(' or char == '[' or char == '{':
                bracket.append(char) #add it to the stack 

            # If we encounter a closing bracket
            else:
                
                # No opening bracket to match it
                if len(bracket) == 0:
                    return False

                # Check the top of the stack #in stack we can only access top
                top = bracket[-1]

                # Check whether the brackets match
                if char == ')' and top == '(':
                    bracket.pop()

                elif char == ']' and top == '[':
                    bracket.pop()

                elif char == '}' and top == '{':
                    bracket.pop()

                # Closing bracket doesn't match top
                else:
                    return False

        # Valid only if no opening brackets are left
        if len(bracket) == 0:
            return True

        return False