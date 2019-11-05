class IsUnique:

    def is_unique_with_dict(self, input: str) -> bool:
        temp = set()
        for ch in input:
            if ch in temp:
                return False
            temp.add(ch)
        return True

    def is_unique_without_extra_memory(self, input: str) -> bool:
        input = list(input)
        input.sort()

        for index in range(len(input)):
            if index < len(input) - 1:
                if input[index] == input[index+1]:
                    return False

        return True

print(IsUnique().is_unique_without_extra_memory('cba'))

print(IsUnique().is_unique_without_extra_memory('cbaaa'))

print(IsUnique().is_unique_without_extra_memory(''))