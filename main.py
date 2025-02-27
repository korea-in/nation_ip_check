# 판별하고자 하는 아이피 주소
target_ip = "14.10.100.30"

# KISA 사이트에서 다운받은 국가별 IP 대역대 파일 로드
f = open("ipv4.csv", "r")

def ipToInt(ip):
    octet1 = ip.split(".")[0]
    octet2 = ip.split(".")[1]
    octet3 = ip.split(".")[2]
    octet4 = ip.split(".")[3]
    
    return int("%03d%03d%03d%03d" % (int(octet1), int(octet2), int(octet3), int(octet4)))

# 첫줄은 항목명이 적혀있어 호출하여 제거한다.
f.readline()

# 1줄씩 읽으면서 아이피 대역대에 포함되는 국가 확인
while True:
    data = f.readline()
    if not data: break 
    
    # csv 파일은 콤마(,)로 데이터를 구분하기 때문에 split 함수로 필요한 부분만 추출한다.
    nation_code = data.split(",")[1]
    from_ip     = data.split(",")[2]
    to_ip       = data.split(",")[3]
    
    # target_ip가 from_ip ~ to_ip 사이에 들어가 있는지 검증한다.
    if((ipToInt(target_ip) >= ipToInt(from_ip)) and (ipToInt(target_ip) <= ipToInt(to_ip))):
        print("IP(%s)가 속한 대역대를 확인하였습니다. [%s]국가, [%s] ~ [%s] 대역대" % (target_ip, nation_code, from_ip, to_ip))
        break