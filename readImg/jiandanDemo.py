# -*- coding: utf-8 -*-
import urllib.request
import os
import sys
import logs

def download_mm(folder='OOXXgif'):
    os.mkdir(folder)
    os.chdir(folder)#切换到文件夹里面
    log = logs.logger()
    url='http://jandan.net/ooxx/'
    page_num = int(get_page(url))#获取页数
    print(page_num)
   
    for i in range(page_num):
        page_num-=1
        page_url = url+'page-'+str(page_num)+'#comments'
        img_addrs = find_imgs(log,page_url)
        save_imgs(folder,img_addrs)
        
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36')
    reponse = urllib.request.urlopen(req)
    html = reponse.read()
    return html

#获取当前的页数
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    return html[a:b]
    
#获取图片的地址   
def find_imgs(log,url):

    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('org_src=')

    while a!=-1:
        b = html.find('.gif',a,a+100)

        hisL = html.find("http",a,a+100)
        if b!=-1:
            if hisL == -1:
                img_addrs.append("http:"+html[a+9:b+4])
            else:
                img_addrs.append(html[a+9:b+4])
        else:

            b=a+9

        a= html.find('img src=',b)
        
    for each in img_addrs:
        log.info(each)
        print(each)
       
    return img_addrs
    



def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)



if __name__ == '__main__':
   download_mm()