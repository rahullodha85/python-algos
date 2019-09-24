class IsUnique:

    def is_unique_with_dict(self, input: str) -> bool:
        temp = set()
        for ch in input:
            if ch in temp:
                return False
            temp.add(ch)
        return True