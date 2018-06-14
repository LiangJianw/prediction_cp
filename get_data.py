import requests
from bs4 import BeautifulSoup


class GetData(object):
    def __init__(self):
        self.url = ""
        self.headers = {}

    def get_data(self):
        # 需要的data格式：{1:[1,2,3,4,5,6,7], 2:[3,2,3,2,3,2,3,2], ...}
        data = dict()
        resp = requests.get(url=self.url, headers=self.headers)
        resp.encoding = "UTF-8"
        if resp.status_code == 200:
            soap = BeautifulSoup(resp.text, 'lxml')
            nums = soap.select()
            for temp in nums:
                data[123] = temp

        return data