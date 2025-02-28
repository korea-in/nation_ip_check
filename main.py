import math
import time

start = time.time()

nation_ip_arr = []
target_ip_arr = []

f1 = open("ipv4.csv", "r")
f2 = open("data.txt", "r")
f1.readline()

def ipToInt(ip):
    octet1 = ip.split(".")[0]
    octet2 = ip.split(".")[1]
    octet3 = ip.split(".")[2]
    octet4 = ip.split(".")[3]
    return int("%03d%03d%03d%03d" % (int(octet1), int(octet2), int(octet3), int(octet4)))

# 20160515,KR,14.192.80.0,14.192.95.255,/20,20100920
# { "nation_code": "KR", "from_ip": 14192080000, "to_ip": 14192095255 }
while True: 
    data = f1.readline().replace("\n", "")
    if not data: break
    tmp = {}
    tmp["nation_code"] = data.split(",")[1]
    tmp[    "from_ip"] = ipToInt(data.split(",")[2])
    tmp[      "to_ip"] = ipToInt(data.split(",")[3])
    nation_ip_arr.append(tmp)
    
while True: 
    data = f2.readline().replace("\n", "")
    if not data: break 
    target_ip_arr.append(ipToInt(data))

# nation_ip_arr의 값인 object의 from_ip key로 정렬한다.
# target_ip_arr는 정수형 데이터만 갖고 있음 그냥 정렬한다.
nation_ip_arr.sort(key = lambda x :x["from_ip"])
target_ip_arr.sort()

etc_ip_cnt = 0 # 사설IP 개수
nation_ip_cnt = {}
idx = 0
for i in range(len(target_ip_arr)):
    target_ip = target_ip_arr[i]
    for j in range(idx, len(nation_ip_arr)):
        nation_ip = nation_ip_arr[j]
        nation_code = nation_ip["nation_code"]
        from_ip     = nation_ip["from_ip"]
        to_ip       = nation_ip["to_ip"]

        if((target_ip >= from_ip) and (target_ip <= to_ip)):
            if nation_ip_cnt.get(nation_code) == None:
                nation_ip_cnt[nation_code] = 1
            else:
                nation_ip_cnt[nation_code] = nation_ip_cnt[nation_code] + 1
            break
        if(nation_ip == nation_ip_arr[len(nation_ip_arr)-1]):
            etc_ip_cnt = etc_ip_cnt + 1
    idx = j - 1

sorted_nation_ip_cnt = sorted(nation_ip_cnt, key= lambda x: nation_ip_cnt[x], reverse=True)
for i in range(5):
    print("%d번째 유입량이 많은 국가코드: %s, 유입량: %d건" %(i+1, sorted_nation_ip_cnt[i], nation_ip_cnt[sorted_nation_ip_cnt[i]]))
    
end = time.time()
print("총 실행시간은 %.2f초" % (end - start))