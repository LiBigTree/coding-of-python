# 爬取亚马逊的一本书
# https://www.amazon.cn/dp/B07QCRP2NY/ref=
# s9_acsd_hps_bw_r2_r0_2_t?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-
# 3&pf_rd_r=1SQ5079Q98SHARMZ9DX0&pf_rd_t=101&pf_rd_p=7f1b720e-1fe0-4946-
# a03d-04047234ab61&pf_rd_i=1849660071
import requests
import sys

sys.path.append(r'D:\CS\python\python_basic\draft\applications')
from applications.config import config as cf


def amazon_crawl(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('1:', r.status_code)
        print('2:', r.encoding)
        print('3:', r.text)
    except:
        print("爬取失败")


if __name__ == '__main__':
    # 网站通过来源审查限制爬虫获取信息，所以要模拟用户
    url = "https://www.amazon.cn/dp/B07QCRP2NY/ref=s9_acsd_hps_bw_r2_r0_2_t?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised" \
          "-search-3&pf_rd_r=1SQ5079Q98SHARMZ9DX0&pf_rd_t=101&pf_rd_p=7f1b720e-1fe0-4946-a03d-04047234ab61&pf_rd_i" \
          "=1849660071 "
    hd = {
        'Cookie': cf.ConfigCrawl.cok,  # 在config下设置相关信息
        'User-Agent': cf.ConfigCrawl.user
    }

    amazon_crawl(url, headers=hd)
