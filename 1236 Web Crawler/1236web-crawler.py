# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        visited = set()

        def crawler(startUrl):
            if startUrl in visited:
                return []

            urls = htmlParser.getUrls(startUrl)
            first = startUrl.split("/")

            visited.add(startUrl)

            res = [startUrl]
            for url in urls:
                idk = url.split("/")
                #print(first[2], idk[2])
                if first[2] == idk[2]:
                    res += crawler(url)
            
            return res
        
        return crawler(startUrl)

        