class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title = title.split()
        for word in range(len(title)):
            if len(title[word]) > 2:
                title[word] = title[word][0].upper() + title[word][1:]
        return ' '.join(title)
        