
date_6=['令','老鲤','灵知','耀骑士临光','焰尾','远牙','琴柳','假日威龙陈','水月','帕拉斯','卡涅利安','浊心斯卡蒂','凯尔希','歌蕾蒂娅','异客','灰烬','夕','嵯峨','空弦','山','迷迭香','泥岩','瑕光','史尔特尔','森蚺','棘刺','铃兰','早露','W','温蒂','傀影','风笛','刻俄柏','年','阿','煌','莫斯提马','麦哲伦','赫拉格','黑','陈','斯卡蒂','银灰','塞雷娅','星熊','夜莺','闪灵','安洁莉娜','艾雅法拉','伊芙利特','推进之王','能天使']

date_5=['夜半','寒芒克洛丝','九色鹿','暮落','极光','耶拉','蚀清','野鬃','蜜莓','灰毫','桑葚','羽毛笔','龙舌兰','绮良','贝娜','赤冬','熔泉','暴雨','霜华','闪击','战车','乌有','炎狱炎熔','图耶','爱丽丝','卡夫卡','罗宾','阿米娅（近卫）','絮雨','奥斯塔','鞭刃','四月','簿绿','燧石','特米米','安哲拉','贾维','蜜蜡','稀音','断崖','亚叶','莱恩哈特','苦艾','月禾','石棉','极境','巫恋','铸铁','慑砂','柏喙','惊蛰','吽','雪雉','灰喉','布洛卡','苇草','槐琥','拜松','微风','送葬人','炎客','星极','格劳克斯','锡兰','诗怀雅','格拉尼','夜魔','暴行','食铁兽','狮蝎','空','真理','初雪','崖心','守林人','普罗旺斯','火神','可颂','雷蛇','红','临光','华法琳','赫默','梅尔','天火','阿米娅','陨星','白金','蓝毒','幽灵鲨','拉普兰德','因陀罗','芙兰卡','德克萨斯','凛冬','白面鸮']

date_4=['布丁','罗比菈塔','深靛','豆苗','松果','杰克','泡泡','芳汀','酸糖','孑','卡达','波登可','刻刀','断罪者','宴','清流','安比尔','梅','伊桑','红云','坚雷','桃金娘','苏苏洛','格雷伊','猎蜂','阿消','地灵','深海色','古米','蛇屠箱','角峰','调香师','嘉维尔','末药','暗索','砾','慕斯','艾斯黛尔','霜叶','缠丸','杜宾','红豆','清道夫','迅使','白雪','流星','杰西卡','远山','夜烟']

date_3=['斑点','泡普卡','月见夜','空爆','梓兰','史都华德','安赛尔','芙蓉','炎熔','安德切尔','克洛丝','米格鲁','卡缇','玫兰莎','翎羽','香草','芬']

date_2=['12F','杜林','巡林者','黑角','夜刀']

date_1=['正义骑士号','THRM-EX','Castle-3','Lancet-2']

print(len(date_1)+len(date_2)+len(date_3)+len(date_4)+len(date_5)+len(date_6))

import random
import time

i=random.randint(1,50)#概率数与抽到的数相等时的概率固定为
print(f'概率数为{i}')
draw=random.randint(1,50)
print(f'抽中了{draw}')

if draw==i:             #0.02概率
    print(f'抽中了6星角色：')
    time.sleep(1)
    card=random.randint(0,len(date_6)-1)
    print(f'{date_6[card]}')

elif draw<=25:
    if i==draw+2 or i==draw+1:
        print('抽中了5星角色：')

        card=random.randint(0,len(date_5)-1)
        print(f'{date_5[card]}')
    elif draw+3<=i and draw+15:
        print('抽中了4星角色：')

        card=random.randint(0,len(date_4)-1)
        print(f'{date_4[card]}')
    else:
        print('抽中了三星角色：')

        card=random.randint(0,len(date_3)-1)
        print(f'{date_3[card]}')

elif draw>25:
    if i==draw-2 or i==draw-1:
        print('抽中了5星角色：')

        card = random.randint(0, len(date_5) - 1)
        print(f'{date_5[card]}')
    elif draw-3>=i and draw-14<=i:
        print('抽中了四星角色：')

        card=random.randint(0,len(date_4)-1)
        print(f'{date_4[card]}')
    else:
        print('抽中了三星角色：')

        card = random.randint(0, len(date_3) - 1)
        print(f'{date_3[card]}')