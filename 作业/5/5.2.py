def interchange_dict(d):
    return {v: k for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}


dic1 = {'Wangbing': 97, 'Maling': 73, 'Xulei': 85}
print(interchange_dict(dic1))
