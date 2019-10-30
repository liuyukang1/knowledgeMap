import json

def readJson(data):
    list = []
    for num in range(0, len(json.loads(data))):
        try:
            anounce = json.loads(data)[num]['good']
        except:
            continue
        for innum in range(0, len(anounce)):
            list.append(anounce[innum])
    return list

if __name__ == '__main__':
    data = [{
        "type": 1,
        "id": 1,
        "tenderContent": "1",
        "tenderContentName": "成交",
        "good": [{
            "title": "HPLaserJet MFP M72630dn 黑白激光数码复合机",
            "amount": 0,
            "count": 14700.0,
            "univalent": 0.0,
            "quantum": 0,
            "providerName": "重庆市香晓科技有限责任公司",
            "providerID": "130117343190712482",
            "projectDirectoryCode": "A",
            "feeScale": "无",
            "feeMoney": 0.0,
            "resultType": 1,
            "providerRealName": "万小礼",
            "providerMobile": "18983335336",
            "sum": 0.0
        }]
    }]
    readJson(data)

