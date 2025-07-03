class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:

        res = []

        for elem in responses:
            curr = elem.split(" ")
            res.append(set(curr))
        
        count = defaultdict(int)

        def func(a, b):
            if count[a] > count[b]:
                return -1
            elif count[b] > count[a]:
                return 1
            else:
                return -1 if indices[a] < indices[b] else 1
        
        indices = {}
        for i in range(len(features)):
            indices[features[i]] = i

        for elem in features:
            for p in res:
                if elem in p:
                    count[elem] += 1
        
        idk = features[::]

        idk.sort(key=cmp_to_key(func))

        print(count)

        return idk



        