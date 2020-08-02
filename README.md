# SYSZUXocr
一个高质量的用于NSFW（涉黄检测等领域）的测试集          

SYSZUXnsfw具有如下特点：

- 划分为porn(涉黄)、 sexy(性感)、 neutral(中立)三部分，每部分300张测试图片；
- 划分为标准：裸露敏感部位或者明显性行为判定为涉黄、穿着少裸露大面积皮肤但未暴露隐私部位判定为性感、其余为中立；                   
- 贴近实际环境，分数高低直接体现算法落地的成熟度；             
- 标准的nsfwReport模块来打分，公平程度犹如高考；               

dataset目录中的图片文件使用git lfs维护，克隆该项目前，你需要首先安装git-lfs：
```bash
#on Linux
apt install git-lfs

#on macOS
brew install git-lfs
```
然后：
```bash
#克隆该项目
git clone https://github.com/DeepVAC/SYSZUXnsfw

#拉取dataset图片
git lfs pull
```

## 使用说明

项目的目录说明如下：     

|  目录   |  说明   |  上传进度  |
|---------|---------|------------|
|dataset  |数据集   |
|porn     |涉黄图片 |未上传      |
|sexy     |性感图片 |更新20200730|
|neutral  |中立图片 |更新20200730|
|src      |测试示例代码|未上传   |


## 如何计算分数

测试集上的分数可以通过deepvac项目lib库的syszux_report模块（NsfwReport类，来自https://github.com/DeepVAC/deepvac/blob/master/lib/syszux_report.py ）给出。NsfwReport类会给三分类的混淆矩阵和评估指标。

#### 混淆矩阵

|      | 涉黄 | 性感 | 中立 |
|------|------|------|------|
| 涉黄 | 295  | 5    | 0    |
| 性感 | 9    | 290  | 1    |
| 中立 | 0    | 3    | 297  |
   
#### 混淆矩阵说明：
- 第一行说明300张涉黄图片295张预测为涉黄即分类正确，5张预测为性感即分类错误，0张预测为中立；               
- 第二行说明300张性感图片9张预测为涉黄即分类错误，290张预测为性感即分类正确，1张预测为中立即分类错误；               
- 第一行说明300张中立图片0张预测为涉黄，3张预测为性感即分类错误，297张预测为中立即分类正确；               

|    | 1   | 0   |
|----|-----|-----|
| 1  | TP  | FN  |
| 0  | FP  | TN  |

#### 评估指标
预测正确样本数量(numcorrect)：(TP+TN)；              
准确率(accuracy)：(TP+TN) / (TP+FN+FP+TN)；  
每一类的精准率(precision)：FP / (TP+FP)；         
每一类的召回率(precision)：FP / (TP+FN)；        
每一类的F1-Score：F1-score = 2TP/(2TP+FP+FN)；     
准确率accuracy和精确率precision都高的情况下，F1 score也会显得很高；          

#### 使用NsfwReport模块来进行以上分数的计算
```python
#use the NsfwReport class
```
程序会输出markdown格式的报告：

## 使用许可
本项目仅限用于纯粹的学术研究，如：
- 个人学习；
- 比赛排名；
- 公开发表且开源其实现的论文；

不得用于任何形式的商业牟利，包括但不限于：
- 任何形式的商业获利行为；
- 任何形式的商务机会获取；
- 任何形式的商业利益交换；


## 项目贡献
我们欢迎各种形式的贡献，包括但不限于：
- 提交自己的作品/产品在SYSZUXnsfw上的成绩；
- 发现和Fix项目的bug；
- 提交高质量的测试集数据；
