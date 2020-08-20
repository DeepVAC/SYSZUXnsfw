# **阿里云图片审核在SYSZUXnsfw数据集上的性能指标**

## 准备工作
- [创建AccessKey并授权](https://help.aliyun.com/document_detail/53045.html)
- [安装python依赖](https://help.aliyun.com/document_detail/50191.html)
```bash
pip3 install aliyun-python-sdk-core-v3==2.13.10
pip3 install -v aliyun-python-sdk-green==3.6.1
pip3 install oss2 
```
- [下载扩展包](https://aligreen-shanghai-share.oss-cn-shanghai.aliyuncs.com/aliyun-python-sdk-green-extension.zip)
解压扩展包，将解压后aliyun-python-sdk-green-extension/aliyun-python-sdk-green-extension目录下的aliyunsdkgreenextension目录移动到当前./src目录下       
- 下载deepvac库
```bash
git clone https://github.com/DeepVAC/deepvac
```

## 配置
相关配置在config.py文件中，包含：      
- config.AccessKeyId
- config.AccessKeySecret
- config.Location, 可选["cn-shanghai", "cn-beijing", "cn-shenzhen", "ap-southeast-1", "us-west-1"]
- config.input_dir测试图片路径

## 运行
```python
python3 test.py
```

## 结果
- DATASET: SYSZUXnsfw
- ACCURACY: 0.905
- CONFUSION-MATRIX

    | SYSZUXnsfw | cls0 | cls1 | cls2 
    |---|---|---|---
    | cls0 | 289 | 3 | 16 
    | cls1 | 0 | 302 | 0 
    | cls2 | 1 | 67 | 235 

- TEST NSFW REPORT

    | SYSZUXnsfw | cls0 | cls1 | cls2 
    |---|---|---|---
    | precision | 0.997 | 0.812 | 0.936 
    | recall | 0.938 | 1.000 | 0.776 
    | f1-score | 0.967 | 0.896 | 0.848

- cls0: normal  cls1: porn  cls2: sexy
