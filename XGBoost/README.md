<!--
 * @Description: 
 * @Author: YuanZi
 * @Github: https://github.com/yzmean
 * @Date: 2019-08-23 14:18:41
 * @LastEditTime: 2019-08-23 14:36:38
 -->
# Baseline
将老人的数据按时间排列,每 7 天为一个单位,若 7 天中有一个指标出现过异常,则认为第 8 天老人会出现异常.
# XGBoost
将老人的数据按时间排列,每 7 天的数据(体温,呼吸率,脉率,血压(高),血压(低),血氧饱和度)作为特征,一共 7*6=42 个特征,第 8 天的正常与否作为标签. 一共有 12095 条数据.取 前 10000 条作为训练数据,后 2095 条作为测试数据,通过 XGBoost 进行分类训练.
# Result
## PR curve
![](https://github.com/yzmean/COPD_DATA/blob/master/XGBoost/PR-curve.png)
## ROC curve
![](https://github.com/yzmean/COPD_DATA/blob/master/XGBoost/ROC-curve.png)
## Score
||Baseline|XGBoost|
|:----:|:----:|:----:|
|F1 Score|0.71597|0.84914|
|Precision Score|0.96336|0.76566|
|Recall Score|0.56967|0.95306|
|ROC-AUC|0.76|0.86|