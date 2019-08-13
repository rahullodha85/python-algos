from rl.datastructs.stack.ArrayStack import Stack

class StackUsage():

    def balanced_parentheses(self, data) -> bool:
        stack = Stack()
        if not data or str(data).strip().__len__() < 1:
            return True

        key_map = {')': '(', '}': '{', ']': '['}

        for char in data:
            if char in key_map.values():
                stack.push(char)
            elif char in key_map.keys():
                if not stack.is_empty():
                    temp = stack.pop()
                    if temp != key_map.get(char):
                        return False
                else:
                    return False

        return stack.is_empty()
