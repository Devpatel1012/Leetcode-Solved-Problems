class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda e:(int(e[1]), 0 if e[0] == 'OFFLINE' else 1))

        mention = [0]*n
        online = [-1]*n
        allM = 0

        for event in events:
            if event[0] == "MESSAGE":
                time = int(event[1])
                mentionStr = event[2]

                if mentionStr == 'ALL':
                    allM+=1
                elif mentionStr == 'HERE':
                    for j in range(n):
                        if online[j]<=time:
                            mention[j]+=1
                else:
                    ids = mentionStr.split(" ")
                    for idS in ids:
                        ID = int(idS[2:])
                        mention[ID]+=1
            else:
                time = int(event[1])
                ID = int(event[2])
                online[ID] = time+60
            
        for i in range(n):
            mention[i]+=allM
        
        return mention