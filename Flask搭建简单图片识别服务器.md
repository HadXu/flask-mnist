# Flask搭建简单手写数字识别服务器 #

----------

###困惑我好几天的问题终于解决了，基础还是不太牢固啊，特写这篇文档记录一下，一步一步的开始用flask搭建分类服务器，主要分类MNIST数据集，从客户端（这里指浏览器）将图片传到服务器，通过服务器来判断该数字属于什么数字###

1.首先介绍一下flask框架

**Flask 是一个 Python 实现的 Web 开发微框架。**

*微* 并不代表这个框架不好，而是一种轻量级的框架，我在此之前没有搞过web开发，但这个框架却让我感到原来学习web开发可以这么简单。
在这里flask框架的搭建我就不说了。

    from flask import Flask,request
    from scipy import misc
    from sklearn.externals import joblib
    
    app = Flask(__name__)
 
    @app.route('/upload', methods=['POST'])
    def upload():
    	f = request.files['file']
    	im = misc.imread(f)	
    	img = im.reshape((1,784))  
    	clf = joblib.load('model/ok.m')
    	l = clf.predict(img)
    	return 'predict: %s ' % (l[0])
    
    @app.route('/')
    def index():
    	return '''
    	<!doctype html>
    	<html>
    	<body>
    	<form action='/upload' method='post' enctype='multipart/form-data'>
      		<input type='file' name='file'>
    	<input type='submit' value='Upload'>
    	</form>
    	'''    
    if __name__ == '__main__':
    	app.run()

首先导入库，使用scipy的misc模块来处理图片，因为从客户端post过来的文件，这里使用post接收文件，用misc来读取文件，并将读取到的图片转化成一维的，因为训练模型就是这样的。然后读取模型，判断。

    # -*- coding:utf-8 -*-
    
    import pandas as pd
    from scipy import misc
    
    data_test = pd.read_csv('Data/test.csv')
    X_test = data_test.values[2:3]
    
    im = X_test.reshape((28,28))
    
    misc.imsave('3.png',im)

这段代码是生成图片的功能，将训练的csv文件生成图片，然后保存起来，通过浏览器上传服务器，来判断属于什么数字。
效果如下：

![](http://i.imgur.com/483UsWn.png)

![](http://i.imgur.com/8PUd2f3.png)

注意图片是**0**，上传以后：

![](http://i.imgur.com/sINkJwx.png)

这样效果就出来了。

