# # 文字人机游戏
# # 关键点：玩家，敌人、双方属性（攻击力、生命力）
# # 完成项目流程：明确项目目标——分析过程，拆解项目——逐步执行，代码实现
# # 版本1.0**自定义属性，人机pk
# # import time
# # print('【玩家】血量：100 攻击：50')
# # print('---------------------------')
# # time.sleep(1)
# # print('【敌人】血量：100 攻击：30')
# # print('---------------------------')
# # print('【玩家】发起了攻击，【敌人】血量50')
# # print('【敌人】发起了攻击，【玩家】血量70')
# # print('---------------------------')
# # time.sleep(1)
# # print('【玩家】发起了攻击，【敌人】血量0')
# # print('【敌人】发起了攻击，【玩家】血量20')
# # print('---------------------------')
# # time.sleep(1)
# # print('【敌人】被KO，【玩家】胜利')

# # 版本2.0随机属性，自动pk
# # import time,random
# # # 随机生成玩家属性
# # player_life=random.randint(150,200)
# # player_attack=random.randint(30,50)
# # # 随机生成敌人属性
# # enemy_life = random.randint(150,200) 
# # enemy_attack = random.randint(30,50)  
# # # 展示双方属性（待优化）
# # print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
# # print('---------------------------')
# # time.sleep(1)
# # print('【敌人】\n血量：{} \n攻击：{}'.format(player_attack,player_attack))
# # print('---------------------------')
# # time.sleep(1)
# # # 自动PK
# # # while 条件：（双方生命力大于0）：
# # while player_life>0 and enemy_life>0:
# #     player_life -= enemy_attack
# #     enemy_life -= player_attack
# #     print('【玩家】发起了攻击，【敌人】血量剩余%s'%(enemy_life))
# #     print('【敌人】发起了攻击，【玩家】血量剩余{}'.format(player_life))
# #     print('---------------------------')
# #     time.sleep(1)


# # 版本3.0 打印结果，三局两胜
# # a 增加单局战果（胜负平）
# # b 三局两胜，判断最终的胜负  （循环）
# # c 统计三局两胜的结果 （存储单次战果：设置初始值）

# # import time,random
# # player_victory = 0
# # enemy_victory = 0
# # for i in range(1,4):
# # # 随机生成玩家属性
# #     time.sleep(2)
# #     print('\n------------现在是第%s局---------------'%i)
# #     player_life=random.randint(150,200)
# #     player_attack=random.randint(30,50)
# #     # 随机生成敌人属性
# #     enemy_life = random.randint(150,200) 
# #     enemy_attack = random.randint(30,50)  
# #     # 展示双方属性（待优化）
# #     print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
# #     print('---------------------------')
# #     time.sleep(1)
# #     print('【敌人】\n血量：{} \n攻击：{}'.format(player_attack,player_attack))
# #     print('---------------------------')
# #     time.sleep(1)
# #     # 自动PK
# #     # while 条件：（双方生命力大于0）：
# #     while player_life>0 and enemy_life>0:
# #         player_life -= enemy_attack
# #         enemy_life -= player_attack
# #         print('【玩家】发起了攻击，【敌人】血量剩余%s'%(enemy_life))
# #         print('【敌人】发起了攻击，【玩家】血量剩余{}'.format(player_life))
# #         print('---------------------------')
# #         time.sleep(1)

# #     if player_life>0 and enemy_life<=0:
# #         player_victory+=1
# #         print('【敌方】大败，【玩家】赢')
# #     elif player_life <=0 and enemy_life > 0:
# #         enemy_victory+=1
# #         print('【敌方】赢，【玩家】失败')
# #     else:
# #         print('同归于尽')
# # if player_victory>enemy_victory:
# #     time.sleep(1)
# #     print('最终结果：【玩家】获胜')
# # elif player_victory<enemy_victory:
# #     time.sleep(1)
# #     print('最终结果：【敌人】获胜')
# # else:
# #     time.sleep(1)
# #     print('最终结果：双方平局')

# # 版本4.0 增加功能：询问是否继续？继续请输入1，如不继续，按任意键则退出游戏
# # input 条件判断???
# import time,random
# player_victory = 0
# enemy_victory = 0
# for i in range(1,4):
# # 随机生成玩家属性
#     time.sleep(2)
#     print('\n------------现在是第%s局---------------'%i)
#     player_life=random.randint(150,200)
#     player_attack=random.randint(30,50)
#     # 随机生成敌人属性
#     enemy_life = random.randint(150,200) 
#     enemy_attack = random.randint(30,50)  
#     # 展示双方属性（待优化）
#     print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
#     print('---------------------------')
#     time.sleep(1)
#     print('【敌人】\n血量：{} \n攻击：{}'.format(player_attack,player_attack))
#     print('---------------------------')
#     time.sleep(1)
#     # 自动PK
#     # while 条件：（双方生命力大于0）：
#     while player_life>0 and enemy_life>0:
#         player_life -= enemy_attack
#         enemy_life -= player_attack
#         print('【玩家】发起了攻击，【敌人】血量剩余%s'%(enemy_life))
#         print('【敌人】发起了攻击，【玩家】血量剩余{}'.format(player_life))
#         print('---------------------------')
#         time.sleep(1)

#     if player_life>0 and enemy_life<=0:
#         player_victory+=1
#         print('【敌方】大败，【玩家】赢')
#     elif player_life <=0 and enemy_life > 0:
#         enemy_victory+=1
#         print('【敌方】赢，【玩家】失败')
#     else:
#         print('同归于尽')
# if player_victory>enemy_victory:
#     time.sleep(1)
#     print('最终结果：【玩家】获胜')
# elif player_victory<enemy_victory:
#     time.sleep(1)
#     print('最终结果：【敌人】获胜')
# else:
#     time.sleep(1)
#     print('最终结果：双方平局')
#     #是否继续游戏
# continue1 = input('是否继续游戏，继续请按任意键，退出游戏请按0')
# if continue1 == '0':
#         again = False
#         print("你退出了游戏")
# elif continue1 != '0':
#         again = True
#         print('继续游戏')