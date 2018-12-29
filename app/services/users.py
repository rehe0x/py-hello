from app import db
import requests
import time
from common import FileUtils

def find_user(pageNo,pageSize):
    no = pageNo if pageNo > 0 else 1;
    size = pageSize * (no - 1);

    params,dict_params = [],{}
    dict_params['pageNo'] = size
    dict_params['pageSize'] = pageSize
   
    params.append(dict_params)

    user = db.session.execute('select sticker_id,thumb_url,mediumPic,sticker_url from t_sticker where state=0 limit :pageNo,:pageSize',params)
    
    return user.fetchall()

def handle_sticker_400(threadName,pageNo,pageSize,url):
    re = find_user(pageNo,pageSize)
    if len(re)==0:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>null"+str(pageNo))
    else:
        for i in re:
            try:
                r = requests.get(url + i[3])
                #r1 = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
                if r.status_code == 404:
                    #print(r.status_code)
                    FileUtils.in_file('sticker_error.txt',i[0]+'==='+i[3])
                    print ("%s: %s" % (threadName, time.ctime(time.time())))
                else:
                    r1 = requests.get(url + i[1])
                    if r1.status_code == 404:
                        FileUtils.in_file('sticker_error.txt',i[0]+'==='+i[1])
                        print ("%s: %s" % (threadName, time.ctime(time.time())))

            except Exception as e:
                 FileUtils.in_file('sticker_error.txt',i[0]+'==='+i[3])
                 print('error>>>>>>>>>>>',e)