m_Code = "MH19"
s_code = ["AB", "KC", "ZX"]
count = 0

for i in s_code:
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    print(f"{m_Code} {i} {j}{k}{l}{m}")
                    count += 1

print(count)
