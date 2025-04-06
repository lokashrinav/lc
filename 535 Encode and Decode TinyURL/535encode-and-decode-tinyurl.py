class Codec:

    def __init__(self):
        self.hmap = {}
        self.count = defaultdict(int)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        idk = longUrl.split("//")
        self.hmap['h0'] = idk[0] + "//"
        self.count['h'] += 1
        
        probs = idk[1].split("/")

        str1 = ""
        for elem in probs:
            if elem:
                first = elem[0]
                self.hmap[first + str(self.count[first])] = elem
                diff = '-' if str1 else ''
                str1 += diff + first + str(self.count[first])
                self.count[first] += 1
        
        return self.hmap['h0'] + str1 + ('-' if longUrl[-1] == '/' else '')
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        idk1 = shortUrl.split("//")
        idk = idk1[1].split("-")

        str1 = ""
        for elem in idk:
            if elem:
                diff = "/" if str1 else ""
                str1 += diff + self.hmap[elem]
        
        return self.hmap['h0'] + str1 + ('/' if shortUrl[-1] == '-' else '')
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))