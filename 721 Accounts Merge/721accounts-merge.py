class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        rootToName = {}
        parent = {}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            idk1 = find(x)
            idk2 = find(y)
            if idk1 != idk2:
                parent[idk1] = idk2

        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in parent:
                parent[first_email] = first_email

            rootToName[first_email] = name

            for i in range(1, len(account)):
                if account[i] not in parent:
                    parent[account[i]] = account[i]
                rootToName[account[i]] = name
                union(first_email, account[i])  


        emailGroups = {}

        for email in parent:
            root = find(email)
            if root not in emailGroups:
                emailGroups[root] = []
            emailGroups[root].append(email)
        
        res = []
        for root, emails in emailGroups.items():
            res.append([rootToName[root]] + sorted(emails))
        
        return res
        

            
