import ipaddress

# 从文件中读取网段
with open('cfip.list', 'r') as file:
    subnets = [line.strip() for line in file if line.strip()]

# 初始化结果列表
filtered_ips = []

# 遍历网段
for subnet in subnets:
    # 创建IP网络对象
    network = ipaddress.IPv4Network(subnet)
    # 遍历子网中的所有IP
    for ip in network:
        # 检查最后一位是否为0
        if ip.packed[-1] == 0:
            filtered_ips.append(str(ip))

# 输出结果
print("符合条件的IP地址：")
for ip in filtered_ips:
    print(ip)
