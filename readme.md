我的习惯工作环境是Linux，文字编辑离不开markdown。我用为知笔记来做归档、跨平台共享（写文档不用为知笔记），这就有一个问题：图片。

# 1. 我的需求
1. 断网的情况下，我linux下的文档要依然可以查看，为知笔记的markdown格式不标准，不要使用为知笔记存在本地的图片来实现。因此，图片必须要存在本地。
2. 文档通过为知笔记存档，我在手机上要能看得见图片，因此为知笔记上的图片必须要有外部链接。

这个需求真的很变态，几乎无法简便的实现，但是我们可以尽量简化一些手动工作：
# 2. 解决方案
1. 截图时，设置快捷键，存储在本地。
2. 将存储在本地的图片，上传到云，返回外部链接复制到剪切板。
3. linux下编辑的文档仍然采用本地图片，但文件名与云上的图片相同，因此经过简单的修改(可再编写一个简单的自动化脚本更改图片的前缀)即可用于归档。

# 3. 使用方式
脚本很简单， 见[github](https://github.com/ssst0n3/screenAutoUp)
## 3.1 注册七牛云账户
添加一个对象存储，记录一下存储空间名称以及测试域名（或者绑定自己的域名）
## 3.2 在密钥管理中记录一下AccessKey/SecretKey
## 3.3 下载源码，在config中，配置以下参数
```
# 密钥
ACCESS_KEY = "***"
SECRET_KEY = "***"
# 存储空间名称
BUCKET_NAME = "***"
# 存储空间的测试域名
BUCKET_URL = "http://***.bkt.clouddn.com/"
# 截图本地保存路径，请确保路径存在，且是绝对路径
SCREEN_SHOT_PATH = "/home/{user}/{screen_shot_path}"
```
## 3.4 配置依赖环境
```
pip install pyperclip
pip install qiniu
```
## 3.5 测试是否成功
如果一切没有问题的话，运行代码并截图后将返回外部链接，可以ctrl+v黏贴出来。我们再增加一个快捷键。
## 3.6 编译可执行文件
```
# 安装pyinstaller
pip install pyinstaller
cd screenAutoUp
pyinstaller -F main.py
cp dist/screenAutoUp ~/bin/
```
## 3.7 添加快捷键
现在可以通过`screenAutoUp`命令运行这个脚本，下面添加一下自己喜欢的键盘映射即可
