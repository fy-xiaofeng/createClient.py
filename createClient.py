import psutil
from socket import AddressFamily

local_addrs = []


def find_ip():
    for name, info in psutil.net_if_addrs().items():
        # print ("xxx   ",name)
        for addr in info:
            # 只放入IPv4的地址
            if AddressFamily.AF_INET == addr.family:
                # if addr.address[0:3] == class_ip:
                local_addrs.append(addr.address)
                print(psutil.net_if_addrs().items())

    print(local_addrs[0])


if __name__ == '__main__':
    find_ip()

# with open("fuwuqi.wb", "w") as fuwuqi:
#     fuwuqi.write(local_addrs[0] + ":545")
# return (local_addrs[0] + ":545")


# if __name__ == '__main__':
#     try:
#         find_ip("192")
#     except IndexError as e:
#         try:
#             find_ip("172")
#         except IndexError as e:
#             try:
#                 find_ip("10.")
#             except IndexError as e:
#                 print("自行查看ipv4地址，改为ipv4+:545格式")
