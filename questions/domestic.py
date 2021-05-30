#https://icpc.iisf.or.jp/past-icpc/domestic2018/contest/all_ja.html

def average():
    input_file = open('domestic.txt')
    for data in input_file.readlines():
        data_list = list(map(int, data.split())) #map関数でlist丸ごとintに変換
        under_avg = 0
        if len(data_list) == 1:
            n = data_list[0]
            if n == 0:
                break
        else:
            avg = sum(data_list) / n
            for l in data_list:
                if l <= avg:
                    under_avg += 1
            print(under_avg)

        
average()