class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        idk = re.split(r'\W+', paragraph.lower())
        banned_set = set(banned)  


        filtered_words = [word for word in idk if word and word not in banned_set]
        word_counts = Counter(filtered_words)
        most_common_word, _ = word_counts.most_common(1)[0]

        return most_common_word