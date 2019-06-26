from aip import AipOcr, AipImageClassify


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def OCR(filePath):
    APP_ID = '16560947'
    API_KEY = 'zGEh2RF4tg8mauYuDUGv0eCP'
    SECRET_KEY = 'wndwge4cGXlp5sPHKNQYqN4NiTZ1SRay'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    filePath = "/home/lwf/scan_recognition/" + filePath
    image = get_file_content(filePath)
    client.basicGeneral(image)
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    ans = ""
    for i in client.basicGeneral(image, options)['words_result']:
        ans += i['words'] + '\n'
    return ans


def image_labels(filePath):
    APP_ID = '16562491'
    API_KEY = 'RjFLMA41ELxZG0A07A3UgxDV'
    SECRET_KEY = '4Kk6jdzfNliYwEVFCOrjwtUee7Ylu6QP'
    filePath = "/home/lwf/scan_recognition/" + filePath
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(filePath)
    client.advancedGeneral(image)
    options = {}
    options["baike_num"] = 5
    ret = client.advancedGeneral(image, options)
    return ret['result'][0]['root'] + ret['result'][0]['keyword']


if __name__ == '__main__':
    ans = image_labels("static/images/2019/06/18/123r.jpg")
    print(ans)
