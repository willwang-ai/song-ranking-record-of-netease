import datetime
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy
import requests


class MusicRanking:
    def __init__(self):
        self.url = 'https://music.163.com/weapi/v1/play/record?csrf_token='
        self.post_data = {
            'params': 'ZWnd2UK9b+MMmt3y9u6v0BufLaBUsSZD23f0ovQRbYfdQ9yvw5pKsGUOyImmC3FAnzxEor2KmlRpygt51lKVpK+Xv2mBrcNc+duITT1Y2E2SUCgvdEBXqY0jQqQFvt3iOEwQFVH1sPTKA92qSrfTEo+GCrYbdYDr6acTOHVPRAsjBsVTj8Vs3VLSVEbtNVRd',
            'encSecKey': '41deae8ec9a95ae1be39369faeaa744e8d14f8aa236007c4d984cee82af7e1c0d4ab8e5fc332c52b0a7c84e37aa0ec081070dd48e81e4ff08173cda969513ecbc2ef13159d73c0bfbbc3ec3523a8ee6f3895de1174d5af7cb9605790b1399defadc6fa737558e3082142ab55d1fb8fc7ef5c03343081db94275693c0229a5055'
        }
        matplotlib.rc("font", family='MicroSoft YaHei')
        self.now = datetime.datetime.now()
        self.time_now = f"{self.now.year}-{self.now.month}-{self.now.day}"

    def week_ranking(self):
        r = requests.post(url=self.url, data=self.post_data)
        weekData = r.json()['weekData']
        scores = []  # 比例
        names = []  # 歌曲名
        explode = []  # 爆炸图

        for single in weekData:
            if single['score']:
                scores.append(single['score'])
                names.append(f"{single['song']['name']} {single['score']}%")
                if single['score'] < 5:
                    explode.append(1)
                else:
                    explode.append(0)

        print(scores, names)

        plt.pie(numpy.array(scores), explode=explode, labels=names, textprops={'fontsize': 5}, rotatelabels=True)

        plt.title(f'小阿雀_ 的听歌周排行 {self.time_now}')

        plt.savefig(f'{self.time_now}.jpg', dpi=1000, bbox_inches='tight')


if __name__ == '__main__':
    while True:
        mr = MusicRanking()
        mr.week_ranking()
        time.sleep(24 * 60 * 60)
