from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Draw(ActionBase):
        """
        抽取一张奥秘卡 出卡(source.job==33?(source.level>=50?及小奥秘卡:):)会变为抽到的奥秘卡技能 追加效果：恢复自身最大魔力的8%

        826, 抽卡, Card Drawn, 抽出一张卡片
        """
        id = 3590
        name = {'Draw', '抽卡'}

    class Redraw(ActionBase):
        """
        重新抽取一张与现有卡不同的奥秘卡 积蓄次数：3 发动条件：抽卡状态中

        """
        id = 3593
        name = {'Redraw', '重抽'}

    class Benefic(ActionBase):
        """
        恢复目标的体力 恢复力：400(source.level>=36?(source.job==33? 追加效果（发动几率15%）：下次福星必定会发动暴击 持续时间：15秒:):)

        """
        id = 3594
        name = {'Benefic', '吉星'}

    class AspectedBenefic(ActionBase):
        """
        恢复目标的体力 恢复力：200 “白昼学派”状态中追加效果：目标体力持续恢复 恢复力：200 持续时间：15秒 该持续恢复效果只能同时附加1个 (source.level>=50?(source.job==33?“黑夜学派”状态中追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量250%的伤害 持续时间：30秒 无法与学者的鼓舞效果共存 发动条件：白昼学派或黑夜学派状态中:发动条件：白昼学派状态中):发动条件：白昼学派状态中)

        835, 吉星相位, Aspected Benefic, 体力会随时间逐渐恢复
        """
        id = 3595
        name = {'Aspected Benefic', '吉星相位'}

    class Malefic(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：150

        """
        id = 3596
        name = {'Malefic', '凶星'}

    class MaleficIi(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：170

        """
        id = 3598
        name = {'Malefic II', '灾星'}

    class Combust(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：40 持续时间：18秒

        838, 烧灼, Combust, 体力逐渐减少
        """
        id = 3599
        name = {'Combust', '烧灼'}

    class Helios(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：330

        """
        id = 3600
        name = {'Helios', '阳星'}

    class AspectedHelios(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：200 “白昼学派”状态中追加效果：目标体力持续恢复 恢复力：100 持续时间：15秒 该持续恢复效果只能同时附加1个 (source.level>=50?(source.job==33?“黑夜学派”状态中追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量125%的伤害 持续时间：30秒 无法与学者的鼓舞效果共存 发动条件：白昼学派或黑夜学派状态中:发动条件：白昼学派状态中):发动条件：白昼学派状态中)

        836, 阳星相位, Aspected Helios, 体力会随时间逐渐恢复
        """
        id = 3601
        name = {'Aspected Helios', '阳星相位'}

    class Ascend(ActionBase):
        """
        令无法战斗的目标以衰弱状态重新振作起来

        """
        id = 3603
        name = {'Ascend', '生辰'}

    class DiurnalSect(ActionBase):
        """
        自身的部分治疗系技能会附加持续恢复体力效果 再次发动时则取消该状态 持续时间：永久 (source.level>=50?(source.job==33?无法与黑夜学派同时使用 与黑夜学派共享复唱时间 自身处于战斗状态时无法取消该状态或切换至黑夜学派状态:自身处于战斗状态时无法取消该状态):自身处于战斗状态时无法取消该状态)

        839, 白昼学派, Diurnal Sect, 自身的一部分治疗技能会附加持续恢复体力效果
        """
        id = 3604
        name = {'Diurnal Sect', '白昼学派'}

    class NocturnalSect(ActionBase):
        """
        自身的部分治疗系技能会附加能够抵消一定伤害的防护罩 同时，吉星相位消耗的魔力会有所增加 再次发动时则取消该状态 持续时间：永久 无法与白昼学派同时使用 与白昼学派共享复唱时间 自身处于战斗状态时无法取消该状态或切换至白昼学派状态

        840, 黑夜学派, Nocturnal Sect, 自身的一部分治疗技能会附加能够抵消一定伤害的防护罩
        """
        id = 3605
        name = {'Nocturnal Sect', '黑夜学派'}

    class Lightspeed(ActionBase):
        """
        一定时间内，自身的魔法咏唱时间缩短2.5秒 持续时间：15秒

        841, 光速, Lightspeed, 魔法的咏唱时间缩短
        1403, 光速, Lightspeed, 咏唱魔法不需要咏唱时间，同时消耗的魔力减半
        """
        id = 3606
        name = {'Lightspeed', '光速'}

    class CombustIi(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：50 持续时间：30秒

        843, 炽灼, Combust II, 体力逐渐减少
        """
        id = 3608
        name = {'Combust II', '炽灼'}

    class BeneficIi(ActionBase):
        """
        恢复目标的体力 恢复力：700

        """
        id = 3610
        name = {'Benefic II', '福星'}

    class Synastry(ActionBase):
        """
        指定一名队员为配对目标，在对自身或队员咏唱单体治疗魔法时，配对目标也会恢复治疗量40%的体力 持续时间：20秒

        845, 星位合图, Synastry, 对队员发动单体治疗魔法时，额外恢复特定队员的体力
        846, 星位合图, Synastry, 附加此效果的占星术士对某一队员发动单体治疗魔法时，身附此效果的队员会恢复额外的体力
        1336, 星位合图, Synastry, 对队员发动单体治疗魔法时，额外恢复特定队员的体力
        1337, 星位合图, Synastry, 附加此效果的占星术士对某一队员发动单体治疗魔法时，身附此效果的队员会恢复额外的体力
        """
        id = 3612
        name = {'Synastry', '星位合图'}

    class CollectiveUnconscious(ActionBase):
        """
        以自身为中心产生命运之轮 “白昼学派”状态中的效果：范围内的自身及队员所受到的伤害减轻10% 持续时间：18秒 同时，范围内的自身及队员还会附加体力持续恢复的效果 恢复力：100 持续时间：15秒 “黑夜学派”状态中的效果：持续恢复范围内自身及队员的体力 恢复力：100 持续时间：18秒 同时，范围内的自身及队员还会附加所受伤害减轻10%的效果 持续时间：20秒 效果时间内发动技能或进行移动、转身都会使命运之轮立即消失 发动条件：白昼学派或黑夜学派状态中 发动之后会停止自动攻击

        847, 命运之轮, Collective Unconscious, 产生能够令范围内队员恢复体力的区域
        848, 命运之轮, Collective Unconscious, 产生减轻伤害的防护区域
        849, 命运之轮, Collective Unconscious, 减轻所受到的伤害
        956, 命运之轮, Wheel of Fortune, 体力会随时间逐渐恢复
        1206, 命运之轮, Wheel of Fortune, 减轻所受到的伤害
        2283, 命运之轮, Collective Unconscious, 产生减轻伤害的防护区域
        """
        id = 3613
        name = {'Collective Unconscious', '命运之轮'}

    class EssentialDignity(ActionBase):
        """
        恢复目标的体力 恢复力：400～1100 目标剩余体力越少，恢复力越高(source.job==33?(source.level>=78? 积蓄次数：2:):)

        """
        id = 3614
        name = {'Essential Dignity', '先天禀赋'}

    class Gravity(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：140

        """
        id = 3615
        name = {'Gravity', '重力'}

    class TheBalance(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以近身攻击为主的职业提高6%，其他职业提高3%(source.job==33?(source.level>=50? 追加效果：若自身处于战斗状态，则在占卜量谱中附加日之标识:):) ※该技能无法设置到热键栏

        829, 太阳神之衡, The Balance, 攻击所造成的伤害提高
        1338, 太阳神之衡, The Balance, 攻击所造成的伤害提高
        1882, 太阳神之衡, The Balance, 攻击所造成的伤害提高
        """
        id = 4401
        name = {'the Balance', '太阳神之衡'}

    class TheArrow(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以近身攻击为主的职业提高6%，其他职业提高3%(source.job==33?(source.level>=50? 追加效果：若自身处于战斗状态，则在占卜量谱中附加月之标识:):) ※该技能无法设置到热键栏

        831, 放浪神之箭, The Arrow, 自动攻击间隔缩短，同时战技与魔法的咏唱及复唱时间也会缩短
        1884, 放浪神之箭, The Arrow, 攻击所造成的伤害提高
        """
        id = 4402
        name = {'the Arrow', '放浪神之箭'}

    class TheSpear(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以近身攻击为主的职业提高6%，其他职业提高3%(source.job==33?(source.level>=50? 追加效果：若自身处于战斗状态，则在占卜量谱中附加星之标识:):) ※该技能无法设置到热键栏

        832, 战争神之枪, The Spear, 暴击发动率提高
        1885, 战争神之枪, The Spear, 攻击所造成的伤害提高
        """
        id = 4403
        name = {'the Spear', '战争神之枪'}

    class TheBole(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以远程攻击为主的职业提高6%，其他职业提高3%(source.job==33?(source.level>=50? 追加效果：若自身处于战斗状态，则在占卜量谱中附加日之标识:):) ※该技能无法设置到热键栏

        830, 世界树之干, The Bole, 受到攻击的伤害减少
        1339, 世界树之干, The Bole, 受到攻击的伤害减少
        1883, 世界树之干, The Bole, 攻击所造成的伤害提高
        """
        id = 4404
        name = {'the Bole', '世界树之干'}

    class TheEwer(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以远程攻击为主的职业提高6%，其他职业提高3%(source.job==33?(source.level>=50? 追加效果：若自身处于战斗状态，则在占卜量谱中附加月之标识:):) ※该技能无法设置到热键栏

        833, 河流神之瓶, The Ewer, 魔力持续恢复
        1340, 河流神之瓶, The Ewer, 魔力持续恢复
        1886, 河流神之瓶, The Ewer, 攻击所造成的伤害提高
        """
        id = 4405
        name = {'the Ewer', '河流神之瓶'}

    class TheSpire(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以远程攻击为主的职业提高6%，其他职业提高3%(source.job==33?(source.level>=50? 追加效果：若自身处于战斗状态，则在占卜量谱中附加星之标识:):) ※该技能无法设置到热键栏

        834, 建筑神之塔, The Spire, 技力持续恢复
        1341, 建筑神之塔, The Spire, 技力持续恢复
        1887, 建筑神之塔, The Spire, 攻击所造成的伤害提高
        """
        id = 4406
        name = {'the Spire', '建筑神之塔'}

    class EarthlyStar(ActionBase):
        """
        在指定地点设置地星，并为自身附加地星主宰状态 持续时间：10秒 地星主宰持续时间内再次使用此技能，则会发动星体破裂，对范围内的敌人进行无属性魔法攻击 威力：100 追加效果：恢复范围内自身与队员的体力 恢复力：540 持续时间结束后，地星获得强化，并为自身附加巨星主宰状态 持续时间：10秒 巨星主宰的持续时间结束时，或时间内再次使用此技能，则会发动星体爆炸，对范围内的敌人进行无属性魔法攻击 威力：150 追加效果：恢复范围内自身与队员的体力 恢复力：720

        """
        id = 7439
        name = {'Earthly Star', '地星'}

    class MaleficIii(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：210

        """
        id = 7442
        name = {'Malefic III', '祸星'}

    class MinorArcana(ActionBase):
        """
        发动抽卡后，该技能变为抽到的奥秘卡技能 抽到太阳神之衡、放浪神之箭、战争神之枪时发动该技能，抽取的奥秘卡将变为王冠之领主 抽到世界树之干、河流神之瓶、建筑神之塔时发动该技能，抽取的奥秘卡将变为王冠之贵妇 对自身或一名队员使用该技能，可令奥秘卡生效 只能同时附加1种奥秘卡效果 发动条件：抽卡状态中

        """
        id = 7443
        name = {'Minor Arcana', '小奥秘卡'}

    class LordOfCrowns(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以近身攻击为主的职业提高8%，其他职业提高4% ※该技能无法设置到热键栏

        1451, 王冠之领主, Lord of Crowns, 攻击所造成的伤害提高
        1876, 王冠之领主, Lord of Crowns, 攻击所造成的伤害提高
        """
        id = 7444
        name = {'Lord of Crowns', '王冠之领主'}

    class LadyOfCrowns(ActionBase):
        """
        令自身或其他一名队员发动攻击造成的伤害提高 持续时间：15秒 以远程攻击为主的职业提高8%，其他职业提高4% ※该技能无法设置到热键栏

        1452, 王冠之贵妇, Lady of Crowns, 受到攻击的伤害减少
        1877, 王冠之贵妇, Lady of Crowns, 攻击所造成的伤害提高
        """
        id = 7445
        name = {'Lady of Crowns', '王冠之贵妇'}

    class SleeveDraw(ActionBase):
        """
        抽取一张标识还未附加在占卜量谱中的奥秘卡 若当前占卜量谱中没有附加任何标识或已附加全部标识，则从六张奥秘卡中随机抽取一张 出卡与小奥秘卡会变为抽到的奥秘卡技能 追加效果：恢复自身最大魔力的8%

        1926, 袖内抽卡, Sleeve Draw, 使用出卡、小奥秘卡或将奥秘卡废弃后会立即抽取一张奥秘卡
        """
        id = 7448
        name = {'Sleeve Draw', '袖内抽卡'}

    class StellarDetonation(ActionBase):
        """
        发动设置在地面的地星 “地星主宰”状态中：对范围内的敌人发动无属性魔法攻击 威力：100 追加效果：恢复范围内自身与队员的体力 恢复力：540 “巨星主宰”状态中：对范围内的敌人发动无属性魔法攻击 威力：150 追加效果：恢复范围内自身与队员的体力 恢复力：720

        """
        id = 8324
        name = {'Stellar Detonation', '星体爆轰'}

    class Undraw(ActionBase):
        """
        将抽到的奥秘卡废弃 发动条件：奥秘卡抽卡状态中

        """
        id = 9629
        name = {'Undraw', '奥秘卡废弃'}

    class Divination(ActionBase):
        """
        令自身与周围队员发动攻击造成的伤害提高 该技能的效果量随占卜量谱的日、月、星的种类数目而变化 1种标识时效果量：4% 2种标识时效果量：5% 3种标识时效果量：6% 持续时间：15秒 自身处于战斗状态时使用卡片技能，可以获得占卜量谱的“日”“月”“星”标识 发动条件：占卜量谱的标识数积累到3个

        1878, 占卜, Divination, 攻击所造成的伤害提高
        2034, 占卜, Divination, 攻击所造成的伤害提升 受到攻击的伤害减少
        """
        id = 16552
        name = {'Divination', '占卜'}

    class CelestialOpposition(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：200 “白昼学派”状态中追加效果：目标体力持续恢复 恢复力：100 持续时间：15秒 该持续恢复效果只能同时附加1个 “黑夜学派”状态中追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量125%的伤害 持续时间：30秒 发动条件：白昼学派或黑夜学派状态中

        """
        id = 16553
        name = {'Celestial Opposition', '天星冲日'}

    class CombustIii(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：60 持续时间：30秒

        1881, 焚灼, Combust III, 体力逐渐减少
        2041, 焚灼, Combust III, 发动攻击所造成的伤害及自身发动的体力恢复效果降低
        """
        id = 16554
        name = {'Combust III', '焚灼'}

    class MaleficIv(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：250

        """
        id = 16555
        name = {'Malefic IV', '煞星'}

    class CelestialIntersection(ActionBase):
        """
        恢复自身或一名队员的体力 恢复力：200 “白昼学派”状态中追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量200%的伤害 持续时间：30秒 “黑夜学派”状态中追加效果：目标体力持续恢复 恢复力：150 持续时间：15秒 该持续恢复效果只能同时附加1个 发动条件：白昼学派或黑夜学派状态中

        """
        id = 16556
        name = {'Celestial Intersection', '天星交错'}

    class Horoscope(ActionBase):
        """
        对自身和周围队员附加天宫图状态 持续时间：10秒 天宫图持续时间内受到自身发动的阳星或阳星相位时，天宫图状态变为阳星天宫图状态 持续时间：30秒 天宫图及阳星天宫图状态的持续时间结束或持续时间内再次使用此技能，会恢复附加了天宫图及阳星天宫图状态的自身及周围队员的体力 天宫图状态恢复力：200 阳星天宫图状态恢复力：400

        1890, 天宫图, Horoscope, 可以受到天宫图带来的治疗效果
        """
        id = 16557
        name = {'Horoscope', '天宫图'}

    class Horoscope(ActionBase):
        """
        恢复自身及周围队员的体力 该技能的恢复力受目标附加的状态影响 天宫图状态恢复力：200 阳星天宫图状态恢复力：400 发动后会取消天宫图及阳星天宫图状态

        1890, 天宫图, Horoscope, 可以受到天宫图带来的治疗效果
        """
        id = 16558
        name = {'Horoscope', '天宫图'}

    class NeutralSect(ActionBase):
        """
        一定时间内，自身发动治疗魔法的治疗量提高20% 追加效果：使用吉星相位及阳星相位时，同时发动白昼学派和黑夜学派双方的追加效果 持续时间：20秒

        1892, 中间学派, Neutral Sect, 发动治疗魔法的治疗量提高
        2044, 中间学派, Neutral Sect, 魔法的咏唱时间和复唱时间缩短
        """
        id = 16559
        name = {'Neutral Sect', '中间学派'}

    class Play(ActionBase):
        """
        抽卡后，此技能变为抽到的奥秘卡技能 对自身或一名队员使用该技能，可令奥秘卡生效 一个目标身上只能同时存在一个奥秘卡效果 发动条件：抽卡

        """
        id = 17055
        name = {'Play', '出卡'}

    class AspectedBenefic(ActionBase):
        """
        恢复目标的体力 恢复力：200 “白昼学派”状态中追加效果：目标体力持续恢复 恢复力：200 持续时间：15秒 该持续恢复效果只能同时附加1个 (source.level>=50?(source.job==33?“黑夜学派”状态中追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量250%的伤害 持续时间：30秒 无法与学者的鼓舞效果共存 发动条件：白昼学派或黑夜学派状态中:发动条件：白昼学派状态中):发动条件：白昼学派状态中)

        835, 吉星相位, Aspected Benefic, 体力会随时间逐渐恢复
        """
        id = 17151
        name = {'Aspected Benefic', '吉星相位'}

    class AspectedHelios(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：200 “白昼学派”状态中追加效果：目标体力持续恢复 恢复力：100 持续时间：15秒 该持续恢复效果只能同时附加1个 (source.level>=50?(source.job==33?“黑夜学派”状态中追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量125%的伤害 持续时间：30秒 无法与学者的鼓舞效果共存 发动条件：白昼学派或黑夜学派状态中:发动条件：白昼学派状态中):发动条件：白昼学派状态中)

        836, 阳星相位, Aspected Helios, 体力会随时间逐渐恢复
        """
        id = 17152
        name = {'Aspected Helios', '阳星相位'}