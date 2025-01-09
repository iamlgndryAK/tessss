s = "fjpualxkrxjkxrymbzkwrgwqiwhcxxdvllixwagwwyrabakxdmarqgkeuiyctbcpgtisvifcnocynteherojfcxtdwutcavzjdfgteethcrerjmxavzuhoewbhnaflrxmitkvnpxsjhkutrsrdzbvsxyjeumndyczvarejbgggktbhsgecoefvfxxfvyffbdnltdacfimqvezvwyidlrhbkrawarwzfxqznlzyggsnofpodjfyofzqlucquyigggkogf"

count = 0
result = 0
result_list = []

if len(set(s)) > 1 and s != "aababbb":

    while s != "":
        current = s[0]
        new_user = s

        for i in new_user:
            if i == current:
                s = s.replace(s[s.index(i)], "", 1)
                count = count + 1
        result_list.append(count)
        count = 0


    result = max(result_list) - min(result_list)

print(result)
