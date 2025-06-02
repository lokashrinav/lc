class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        sent = sentence.split(" ")

        for i in range(len(sent)):
            rep = None
            for p in range(len(dictionary)):
                if dictionary[p] == sent[i][:len(dictionary[p])] and rep is None:
                    rep = dictionary[p]
                elif dictionary[p] == sent[i][:len(dictionary[p])]:
                    rep = min(rep, dictionary[p])
            
            if rep is not None:
                sent[i] = rep
        
        return ' '.join(sent)

            

        


        