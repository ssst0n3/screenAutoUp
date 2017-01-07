# coding=utf-8
from qiniu import Auth, put_file
from config import ACCESS_KEY, SECRET_KEY, BUCKET_NAME, BUCKET_URL, SCREEN_SHOT_PATH
import os
import time
import pyperclip


def upload(local_file_path, upload_path):
    """
    上传操作
    :param local_file_path: 本地图片地址
    :param upload_path:     上传地址
    :return: image_url:     返回外部链接
    """
    # 构建鉴权对象
    q = Auth(ACCESS_KEY, SECRET_KEY)
    # 生成上传Token, 可以制定过期时间等
    token = q.upload_token(BUCKET_NAME, upload_path, 3600)
    put_file(token, upload_path, local_file_path)
    image_url = BUCKET_URL + upload_path
    return image_url


def screen_shot():
    time_stamp = time.time()
    date = time.strftime('%Y-%m-%d', time.localtime(time_stamp))
    file_name = "{date}-{time_stamp}.png".format(date=date, time_stamp=str(time_stamp).replace(".", "_"))
    local_file_path = SCREEN_SHOT_PATH + file_name
    os.system("gnome-screenshot -a -f " + local_file_path)
    image_url = upload(local_file_path, file_name)
    pyperclip.copy(image_url)


if __name__ == "__main__":
    screen_shot()