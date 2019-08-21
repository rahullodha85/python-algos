class Multiple3and5:

    def brute_force(self, data):
        output = 0
        for num in range(1, data):
            if num % 3 == 0 or num % 5 == 0:
                output = output + num

        return output

    def math(self, data):
        return self.__math(data, 3) + self.__math(data, 5)

    def __math(self, data, key):
        temp = 0
        output = 0
        for i in range(data-1, 1, -1):
            if i % key == 0:
                temp = i / key
                break
        output = output + key * ((temp / 2) * (temp + 1))
        return output
