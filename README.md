# anti-asoul
本插件是基于[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)做的开发

##安装
将`antiasoul`文件夹，复制到`HoshinoBot/hoshino/modules`目录下
修改`HoshinoBot/hoshino/config/__bot__.py`中
```python
# 启用的模块
MODULES_ON = {
    ...
    'antiasoul',#这个是新添的
    ...
}
```
再将`antiasoul`文件夹复制到`HoshinoBot/res/img`目录下

###使用方法
机器人会自动识别，嘉然，然然，捏等关键字，并让发言者滚（指禁言）
（你也可以通过修改关键词和图库来指定其他的
