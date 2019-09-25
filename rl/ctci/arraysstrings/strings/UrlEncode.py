class UrlEncode:

    def encode(self, url):
        url = list(url)
        count = 0
        for ch in url:
            if ch == ' ':
                count += 1
        for i in range(0, count*2):
           url.append('_')

        for i in range(url.__len__()-1, 0, -1):
            if url[i] == '_':
                pass
            else:
                if url[i] == ' ':
                    url[i+count*2]='0'
                    url[i-1 + count*2]='2'
                    url[i-2 + count*2]= '%'
                    count -= 1
                else:
                    url[i + (count * 2)] = url[i]

        print(url)
        return len(url)


test = UrlEncode()
test.encode('Mr John Smith')