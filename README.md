# flappy bird

编程语言：python，使用的是pygame

### 游戏规则：
  游戏中有两个角色（一只鸟，一只皮卡丘（简称pika）），可以通过上，左，右键控制鸟，w，s键控制pika，按空格键可控制pika发射子弹击中气球。两个角色是同步移动的，但是当皮卡掉到地上就只能人为的把他拉上去。右下角还会不停地扔出一个精灵球（简称球吧）。其实就是将flappy bird 与打气球游戏结合在一起了。能力有限，做得非常简陋。因为感觉叫做flappy bird也没问题，所以名字就草率的决定叫flappy bird了。

### 游戏特点：
  地图的移动（好像也不是特点），其实也就是将两张一样的图片一起移动，你也可以贴几朵云，只是我懒得加。。。
  碰撞检测：制作过程中做了许多碰撞检测（鸟，皮卡与管道，气球，地面以及球的碰撞的碰撞，子弹与气球的碰撞），完成后的我一度不想再做碰撞检测了。



```markdown


因为文件很乱，在这里我解释一下我的文件吧
main.py -- 主程序（我好像放了好多乱七八糟的东西）
map.py --  地图（主要是实现了地图的滚动）
ball.py -- 就是右下角仍的那个球
bobo.py -- 那只别扭的鸟
pika.py --  违和的金皮卡
bullet.py -- 子弹
pip.py  -- 管道
qiqiu.py -- 气球
scoreboard.py -- 记录分数
button.py  -- 制作按键（就是那个简陋的“开始”键）
game_function -- 游戏功能实现（虽然有好多被我移到main里去了）
剩下的基本就是图片了。。。


```



```markdown



```
### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/crwen/flappy-bird/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
