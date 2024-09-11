"""
脚本流程：
进入游戏：
    查看是否完成每日
    未完成：
        开始执行->刮刮乐->喝咖啡->上架录像带->完成
    完成：
        查看体力->判断需求材料->刷取材料{跳转副本->战斗}
    判断退出：
"""

import Output

Output.setGameWindow('米哈游启动器')
Output.startAction('报刊亭刮卡')

