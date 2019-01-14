import requests
from bs4 import BeautifulSoup

jr_url = "https://search.51job.com/list/040000,000000,0000,03,9,99,%2B,2,1.html?" \
         "lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&" \
         "companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&" \
         "specialarea=00&from=&welfare="

jr_50_url = "https://search.51job.com/list/040000,000000,0000,03,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=01&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
jr_50_150_url = "https://search.51job.com/list/040000,000000,0000,03,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=02&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
yx_50_url = "https://search.51job.com/list/040000,000000,0000,40,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=01&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
yx_150_url = "https://search.51job.com/list/040000,000000,0000,40,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=02&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
ds_50_url = "https://search.51job.com/list/040000,000000,0000,32,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=01&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
ds_150_url = "https://search.51job.com/list/040000,000000,0000,32,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=02&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
qt_50_url = "https://search.51job.com/list/040000,000000,0000,01%252C31%252C37%252C38%252C02,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=01&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
qt_150_url ="https://search.51job.com/list/040000,000000,0000,01%252C31%252C37%252C38%252C02,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=02&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="


def getHTMLText(url):
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Referer': '{}'.format(url),
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 获取行业公司url
def getCompanyUrlList(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'lxml')
    company_url = soup.find('div', attrs={'class': 'dw_table'}).find_all('span', attrs={'class': 't2'})
    lst_url = []
    for url in company_url:
        try:
            lst_url.append(url.find('a')['href'])
        except:
            pass
    return lst_url


# 获取公司职位信息
def getCompanyJobsInfo(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'lxml')
    jobs_info = soup.find('div', attrs={'id': 'joblistdata'}).find_all('div', attrs={'class': 'el'})
    for info in jobs_info:
        try:
            job_company = soup.title.text
            job_name = info.find('a').text
            job_yaoqiu = info.find('span', attrs={'class': 't2'}).text
            job_addr = info.find('span', attrs={'class': 't3'}).text
            job_money = info.find('span', attrs={'class': 't4'}).text
            with open('qt150.txt', 'a') as f:
                f.write('{} + {} + {} + {} + {} \n'.format(job_company, job_name, job_yaoqiu, job_addr, job_money))
        except:
            pass


def main():
    all_jr_url = getCompanyUrlList(qt_150_url)
    for url in all_jr_url:
        getCompanyJobsInfo(url)
main()
