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

    def next_greater_element(self, data) -> dict:
        stack = Stack()

        return_dict = {}
        for next in data:
            if not stack.is_empty():
                element = stack.pop()

                while element < next:
                    return_dict.update({element: next})
                    if stack.is_empty():
                        break
                    element = stack.pop()

                if element > next:
                    stack.push(element)

            else:
                stack.push(next)

        return return_dict
