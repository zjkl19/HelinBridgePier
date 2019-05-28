# Helin 桥梁模型（8#、9#墩）

## 模型概况：
材料：C30混凝土
单元：C3D8R


## 文件说明：
1、HelinGravitySingle.py：仅考虑自重作用
2、HelinGravityWhole.py：除了考虑自重，还考虑相邻构件相互作用力（相互作用力根据对应midas整体结构模型自重工况得出）
3、HelinVehicleLoad.py：车辆加载
4、HelinVehicleLoad1.py：车辆加载1（与HelinVehicleLoad.py车辆布置位置不同）

## 图片说明
仅考虑自重作用的结构最大主拉应力云图：HelinGravitySingle.png
![仅考虑自重作用的结构最大主拉应力云图](https://github.com/zjkl19/HelinBridgePier/blob/master/HelinGravitySingle.png)

除了考虑自重，还考虑相邻构件相互作用力下的结构最大主拉应力云图：HelinGravityWhole.png
![除了考虑自重，还考虑相邻构件相互作用力下的结构最大主拉应力云图](https://github.com/zjkl19/HelinBridgePier/blob/master/HelinGravityWhole.png)

车辆加载结构U2位移云图：HelinVehicleLoad_U2.png
![车辆加载结构U2位移云图](https://github.com/zjkl19/HelinBridgePier/blob/master/HelinVehicleLoad_U2.png)
车辆加载结构应力云图：HelinVehicleLoad_S.png
![车辆加载结构应力云图](https://github.com/zjkl19/HelinBridgePier/blob/master/HelinVehicleLoad_S.png)