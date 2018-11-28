import requests
import os
from multiprocessing.pool import Pool
import random
import math
from datetime import datetime

# 文件夹位置
PATH = '/data2/offlinemap/'

# 高得地图层级为1-19
GD_ZOOM = 17

# 甘肃省 介于北纬32°11′~42°57′、东经92°13′~108°46′之间
LNG_WEST = float(92.216667)
LAT_NORTH = float(42.95)

LNG_EAST = float(108.766667)
LAT_SOUTH = float(32.183333)

header = {
    'Host':'www.amap.com',
    'Referer':'https://www.google.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

def download_image(xyz):
    try:    
        wprd = random.randint(1, 4)
        url = "http://wprd0{}.is.autonavi.com/appmaptile?style=7&x={}&y={}&z={}".format(wprd, xyz[0], xyz[1], xyz[2])
        image = requests.get(url)

        try:
            if not os.path.exists(PATH + '/' + str(xyz[2]) + '/' + str(xyz[1])):
                os.makedirs(PATH + '/' + str(xyz[2]) + '/' + str(xyz[1]))
                print('创建文件夹成功')
        except:
            print('创建文件夹失败')
        os.chdir(PATH + '/' + str(xyz[2]) + '/' + str(xyz[1]))

        name = '{}.png'.format(xyz[0])
        with open(name, 'ab') as f:
            f.write(image.content)
            print('写入成功' + name+'-'+'{}-{}-{}-'.format(xyz[0],xyz[1],xyz[2])+str(datetime.now()))
            f.close()
    except e:
        with open('error.log','a') as f:
            f.write('{}-{}-{}'.format(xyz[0],xyz[1],xyz[2]))
            f.write(e)


def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)


if __name__ == '__main__':
    for z in range(6, 9):
        #min_xy = deg2num(LAT_NORTH, LNG_WEST, z)
        #max_xy = deg2num(LAT_SOUTH, LNG_EAST, z)
        try:
            urls = ([x, y, z] for x in range(2**z) for y in range(2**z))
            pool = Pool(8)
            pool.map(download_image, urls)
            pool.close()
            pool.join()
        except:
            print("!!!!!!!!!!!!!!!!!!!!!!!!")
