import math
s = "ykudzhiixwttnvtesiwnbcjmsydidttiyabbwzlfbmmycwjgzwhbtvtxyvkkjgfehaypiygpstkhakfasiloaveqzcywsiujvixcdnxpvvtobxgroznswwwipypwmdhldsoswrzyqthaqlbwragjrqwjxgmftjxqugoonxadazeoxalmccfeyqtmoxwbnphxih"


count = 0
result = 0
result_list = []
variance_list = []

if len(set(s)) > 1:
    for i in range(2, len(s) + 1):
        for j in range(math.ceil(len(s)/i) + 1):
            z = j + i
            if z <= len(s):
                new_s = s[j: z]
                print(new_s)

                if len(set(new_s)) > 1:

                    while new_s != "":
                        current = new_s[0]
                        new_user = new_s

                        for k in new_user:
                            if k == current:
                                new_s = new_s.replace(new_s[new_s.index(k)], "", 1)
                                count = count + 1
                        result_list.append(count)
                        count = 0

                    result = max(result_list) - min(result_list)
                    variance_list.append(result)
                    result_list = []


print(variance_list)