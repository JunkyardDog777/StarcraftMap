from eudplib import *
try:
    InitialWireframe
except NameError:

    def init_wireframe():
        WireFrameDataEditor.WireFrameInit()
        WireFrameDataEditor.ChangeWireframe(80, 204)
        WireFrameDataEditor.ChangeTranframe(80, 0)
        WireFrameDataEditor.ChangeGrpframe(80, 0)
        WireFrameDataEditor.ChangeWireframe(82, 204)
        WireFrameDataEditor.ChangeTranframe(82, 0)
        WireFrameDataEditor.ChangeGrpframe(82, 0)
        WireFrameDataEditor.ChangeWireframe(86, 7)
        WireFrameDataEditor.ChangeTranframe(86, 7)
        WireFrameDataEditor.ChangeGrpframe(86, 7)
        WireFrameDataEditor.ChangeWireframe(87, 7)
        WireFrameDataEditor.ChangeTranframe(87, 7)
        WireFrameDataEditor.ChangeGrpframe(87, 7)
        WireFrameDataEditor.ChangeWireframe(88, 7)
        WireFrameDataEditor.ChangeTranframe(88, 7)
        WireFrameDataEditor.ChangeGrpframe(88, 7)
        WireFrameDataEditor.ChangeWireframe(89, 6)
        WireFrameDataEditor.ChangeTranframe(89, 6)
        WireFrameDataEditor.ChangeGrpframe(89, 6)
        WireFrameDataEditor.ChangeWireframe(90, 7)
        WireFrameDataEditor.ChangeTranframe(90, 7)
        WireFrameDataEditor.ChangeGrpframe(90, 7)
        WireFrameDataEditor.ChangeWireframe(91, 7)
        WireFrameDataEditor.ChangeTranframe(91, 7)
        WireFrameDataEditor.ChangeGrpframe(91, 7)
        WireFrameDataEditor.ChangeWireframe(92, 7)
        WireFrameDataEditor.ChangeTranframe(92, 7)
        WireFrameDataEditor.ChangeGrpframe(92, 7)
        WireFrameDataEditor.ChangeWireframe(93, 7)
        WireFrameDataEditor.ChangeTranframe(93, 7)
        WireFrameDataEditor.ChangeGrpframe(93, 7)
        WireFrameDataEditor.ChangeWireframe(94, 7)
        WireFrameDataEditor.ChangeTranframe(94, 7)
        WireFrameDataEditor.ChangeGrpframe(94, 7)
        WireFrameDataEditor.ChangeWireframe(95, 6)
        WireFrameDataEditor.ChangeTranframe(95, 6)
        WireFrameDataEditor.ChangeGrpframe(95, 6)
        WireFrameDataEditor.ChangeWireframe(96, 6)
        WireFrameDataEditor.ChangeTranframe(96, 6)
        WireFrameDataEditor.ChangeGrpframe(96, 6)
        WireFrameDataEditor.ChangeWireframe(105, 21)
        WireFrameDataEditor.ChangeTranframe(105, 21)
        WireFrameDataEditor.ChangeGrpframe(105, 21)
        WireFrameDataEditor.ChangeWireframe(205, 204)
        WireFrameDataEditor.ChangeWireframe(206, 204)
        WireFrameDataEditor.ChangeWireframe(209, 204)

else:
    InitialWireframe.wirefram(80, 204)
    InitialWireframe.tranwire(80, 0)
    InitialWireframe.grpwire(80, 0)
    InitialWireframe.wirefram(82, 204)
    InitialWireframe.tranwire(82, 0)
    InitialWireframe.grpwire(82, 0)
    InitialWireframe.wirefram(86, 7)
    InitialWireframe.tranwire(86, 7)
    InitialWireframe.grpwire(86, 7)
    InitialWireframe.wirefram(87, 7)
    InitialWireframe.tranwire(87, 7)
    InitialWireframe.grpwire(87, 7)
    InitialWireframe.wirefram(88, 7)
    InitialWireframe.tranwire(88, 7)
    InitialWireframe.grpwire(88, 7)
    InitialWireframe.wirefram(89, 6)
    InitialWireframe.tranwire(89, 6)
    InitialWireframe.grpwire(89, 6)
    InitialWireframe.wirefram(90, 7)
    InitialWireframe.tranwire(90, 7)
    InitialWireframe.grpwire(90, 7)
    InitialWireframe.wirefram(91, 7)
    InitialWireframe.tranwire(91, 7)
    InitialWireframe.grpwire(91, 7)
    InitialWireframe.wirefram(92, 7)
    InitialWireframe.tranwire(92, 7)
    InitialWireframe.grpwire(92, 7)
    InitialWireframe.wirefram(93, 7)
    InitialWireframe.tranwire(93, 7)
    InitialWireframe.grpwire(93, 7)
    InitialWireframe.wirefram(94, 7)
    InitialWireframe.tranwire(94, 7)
    InitialWireframe.grpwire(94, 7)
    InitialWireframe.wirefram(95, 6)
    InitialWireframe.tranwire(95, 6)
    InitialWireframe.grpwire(95, 6)
    InitialWireframe.wirefram(96, 6)
    InitialWireframe.tranwire(96, 6)
    InitialWireframe.grpwire(96, 6)
    InitialWireframe.wirefram(105, 21)
    InitialWireframe.tranwire(105, 21)
    InitialWireframe.grpwire(105, 21)
    InitialWireframe.wirefram(205, 204)
    InitialWireframe.wirefram(206, 204)
    InitialWireframe.wirefram(209, 204)


def onPluginStart():
    try:
        init_wireframe()
    except NameError:
        pass
    DoActions([ # 스테이터스인포메이션
        SetMemory(0x519764, SetTo, 4344192),
        SetMemory(0x519768, SetTo, 4353872),
        SetMemory(0x51977C, SetTo, 4343040),
        SetMemory(0x519780, SetTo, 4349664),
        SetMemory(0x5197E8, SetTo, 4344192),
        SetMemory(0x5197EC, SetTo, 4353872),
        SetMemory(0x5197F4, SetTo, 4344192),
        SetMemory(0x5197F8, SetTo, 4353872),
        SetMemory(0x519890, SetTo, 4344192),
        SetMemory(0x519894, SetTo, 4353872),
        SetMemory(0x519D70, SetTo, 4343040),
        SetMemory(0x519D74, SetTo, 4349664),
    ])
    # 버튼셋
    bytebuffer = bytearray([1,0,229,0,96,142,66,0,176,52,66,0,89,0,89,0,74,2,0,0,2,0,128,0,96,142,66,0,176,52,66,0,91,0,91,0,74,2,0,0,3,0,132,1,96,142,66,0,176,52,66,0,94,0,94,0,74,2,0,0,4,0,128,0,96,142,66,0,176,52,66,0,90,0,90,0,74,2,0,0,6,0,128,0,96,142,66,0,176,52,66,0,92,0,92,0,74,2,0,0,8,0,128,0,96,142,66,0,176,52,66,0,93,0,93,0,74,2,0,0,9,0,133,1,96,142,66,0,176,52,66,0,88,0,88,0,74,2,0,0])
    btnptr94 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,32,132,66,0,64,68,66,0,0,0,0,0,152,2,0,0,1,0,0,0,96,142,66,0,176,52,66,0,0,0,0,0,74,2,0,0,2,0,229,0,32,132,66,0,240,51,66,0,0,0,0,0,153,2,0,0,2,0,32,0,96,142,66,0,176,52,66,0,32,0,32,0,76,2,190,2,3,0,1,0,96,142,66,0,176,52,66,0,1,0,1,0,75,2,189,2,4,0,34,0,96,142,66,0,176,52,66,0,34,0,34,0,10,5,14,5,6,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,9,0,27,1,240,131,66,0,48,60,66,0,0,0,111,0,158,2,0,0,9,0,26,1,208,135,66,0,48,50,66,0,0,0,0,0,159,2,0,0,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,0,0,9,0,236,0,32,137,66,0,208,50,66,0,0,0,0,0,182,2,0,0])
    btnptr111 = Db(bytebuffer)
    DoActions([
        SetMemory(0x518BAC, SetTo, btnptr94),
        SetMemory(0x518BA8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518BC4, SetTo, 0),
        SetMemory(0x518BC0, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518BF4, SetTo, 0),
        SetMemory(0x518BF0, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C00, SetTo, 0),
        SetMemory(0x518BFC, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C0C, SetTo, 0),
        SetMemory(0x518C08, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C18, SetTo, 0),
        SetMemory(0x518C14, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C24, SetTo, 0),
        SetMemory(0x518C20, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C30, SetTo, 5339360),
        SetMemory(0x518C2C, SetTo, 9),
    ])
    DoActions([
        SetMemory(0x518C3C, SetTo, 0),
        SetMemory(0x518C38, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C48, SetTo, 0),
        SetMemory(0x518C44, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C54, SetTo, 0),
        SetMemory(0x518C50, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C60, SetTo, 0),
        SetMemory(0x518C5C, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C6C, SetTo, 0),
        SetMemory(0x518C68, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518CD8, SetTo, 5340440),
        SetMemory(0x518CD4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518D20, SetTo, btnptr111),
        SetMemory(0x518D1C, SetTo, 11),
    ])
    inputData = open('../temp/RequireData', 'rb').read()
    inputData_db = Db(inputData)
    inputDwordN = (len(inputData) + 3) // 4

    addrEPD = EPD(0x514178)
    f_repmovsd_epd(addrEPD, EPD(inputData_db), inputDwordN)


def beforeTriggerExec():
    DoActions([
        SetMemory(0x660A70 + 0, SetTo, 393217),
        SetMemory(0x660A70 + 4, SetTo, 786439),
        SetMemory(0x660A70 + 8, SetTo, 1179648),
        SetMemory(0x660A70 + 12, SetTo, 1638400),
        SetMemory(0x660A70 + 16, SetTo, 2293790),
        SetMemory(0x660A70 + 20, SetTo, 2818048),
        SetMemory(0x660A70 + 24, SetTo, 50),
        SetMemory(0x660A70 + 28, SetTo, 58),
        SetMemory(0x660A70 + 32, SetTo, 0),
        SetMemory(0x660A70 + 36, SetTo, 0),
        SetMemory(0x660A70 + 40, SetTo, 0),
        SetMemory(0x660A70 + 44, SetTo, 0),
        SetMemory(0x660A70 + 48, SetTo, 0),
        SetMemory(0x660A70 + 52, SetTo, 0),
        SetMemory(0x660A70 + 56, SetTo, 0),
        SetMemory(0x660A70 + 60, SetTo, 0),
        SetMemory(0x660A70 + 64, SetTo, 63),
        SetMemory(0x660A70 + 68, SetTo, 69),
        SetMemory(0x660A70 + 72, SetTo, 4980736),
        SetMemory(0x660A70 + 76, SetTo, 5505104),
        SetMemory(0x660A70 + 80, SetTo, 5767168),
        SetMemory(0x660A70 + 84, SetTo, 6160475),
        SetMemory(0x660A70 + 88, SetTo, 6881381),
        SetMemory(0x660A70 + 92, SetTo, 7405677),
        SetMemory(0x660A70 + 96, SetTo, 0),
        SetMemory(0x660A70 + 100, SetTo, 120),
        SetMemory(0x660A70 + 104, SetTo, 0),
        SetMemory(0x660A70 + 108, SetTo, 0),
        SetMemory(0x660A70 + 112, SetTo, 0),
        SetMemory(0x660A70 + 116, SetTo, 124),
        SetMemory(0x660A70 + 120, SetTo, 8978565),
        SetMemory(0x660A70 + 124, SetTo, 142),
        SetMemory(0x660A70 + 128, SetTo, 9896083),
        SetMemory(0x660A70 + 132, SetTo, 10354842),
        SetMemory(0x660A70 + 136, SetTo, 10616832),
        SetMemory(0x660A70 + 140, SetTo, 11010213),
        SetMemory(0x660A70 + 144, SetTo, 11534508),
        SetMemory(0x660A70 + 148, SetTo, 0),
        SetMemory(0x660A70 + 152, SetTo, 0),
        SetMemory(0x660A70 + 156, SetTo, 0),
        SetMemory(0x660A70 + 160, SetTo, 183),
        SetMemory(0x660A70 + 164, SetTo, 12124344),
        SetMemory(0x660A70 + 168, SetTo, 12648637),
        SetMemory(0x660A70 + 172, SetTo, 13172936),
        SetMemory(0x660A70 + 176, SetTo, 13304010),
        SetMemory(0x660A70 + 180, SetTo, 13435084),
        SetMemory(0x660A70 + 184, SetTo, 13566158),
        SetMemory(0x660A70 + 188, SetTo, 13697232),
        SetMemory(0x660A70 + 192, SetTo, 210),
        SetMemory(0x660A70 + 196, SetTo, 0),
        SetMemory(0x660A70 + 200, SetTo, 0),
        SetMemory(0x660A70 + 204, SetTo, 13828096),
        SetMemory(0x660A70 + 208, SetTo, 14221312),
        SetMemory(0x660A70 + 212, SetTo, 14549210),
        SetMemory(0x660A70 + 216, SetTo, 15335652),
        SetMemory(0x660A70 + 220, SetTo, 15859950),
        SetMemory(0x660A70 + 224, SetTo, 16515319),
        SetMemory(0x660A70 + 228, SetTo, 17170689),
        SetMemory(0x660A70 + 232, SetTo, 17826059),
        SetMemory(0x660A70 + 236, SetTo, 277),
        SetMemory(0x660A70 + 240, SetTo, 282),
        SetMemory(0x660A70 + 244, SetTo, 19136799),
        SetMemory(0x660A70 + 248, SetTo, 19792169),
        SetMemory(0x660A70 + 252, SetTo, 0),
        SetMemory(0x660A70 + 256, SetTo, 0),
        SetMemory(0x660A70 + 260, SetTo, 20119552),
        SetMemory(0x660A70 + 264, SetTo, 20709687),
        SetMemory(0x660A70 + 268, SetTo, 21365057),
        SetMemory(0x660A70 + 272, SetTo, 22020427),
        SetMemory(0x660A70 + 276, SetTo, 22872405),
        SetMemory(0x660A70 + 280, SetTo, 23921000),
        SetMemory(0x660A70 + 284, SetTo, 25166197),
        SetMemory(0x660A70 + 288, SetTo, 388),
        SetMemory(0x660A70 + 292, SetTo, 392),
        SetMemory(0x660A70 + 296, SetTo, 25952256),
        SetMemory(0x660A70 + 300, SetTo, 0),
        SetMemory(0x660A70 + 304, SetTo, 0),
        SetMemory(0x660A70 + 308, SetTo, 26345871),
        SetMemory(0x660A70 + 312, SetTo, 26804630),
        SetMemory(0x660A70 + 316, SetTo, 27000832),
        SetMemory(0x660A70 + 320, SetTo, 416),
        SetMemory(0x660A70 + 324, SetTo, 27787684),
        SetMemory(0x660A70 + 328, SetTo, 28311980),
        SetMemory(0x660A70 + 332, SetTo, 28836276),
        SetMemory(0x660A70 + 336, SetTo, 29097984),
        SetMemory(0x660A70 + 340, SetTo, 29688256),
        SetMemory(0x660A70 + 344, SetTo, 457),
        SetMemory(0x660A70 + 348, SetTo, 0),
        SetMemory(0x660A70 + 352, SetTo, 0),
        SetMemory(0x660A70 + 356, SetTo, 0),
        SetMemory(0x660A70 + 360, SetTo, 0),
        SetMemory(0x660A70 + 364, SetTo, 0),
        SetMemory(0x660A70 + 368, SetTo, 0),
        SetMemory(0x660A70 + 372, SetTo, 0),
        SetMemory(0x660A70 + 376, SetTo, 0),
        SetMemory(0x660A70 + 380, SetTo, 0),
        SetMemory(0x660A70 + 384, SetTo, 0),
        SetMemory(0x660A70 + 388, SetTo, 0),
        SetMemory(0x660A70 + 392, SetTo, 0),
        SetMemory(0x660A70 + 396, SetTo, 0),
        SetMemory(0x660A70 + 400, SetTo, 0),
        SetMemory(0x660A70 + 404, SetTo, 0),
        SetMemory(0x660A70 + 408, SetTo, 0),
        SetMemory(0x660A70 + 412, SetTo, 0),
        SetMemory(0x660A70 + 416, SetTo, 0),
        SetMemory(0x660A70 + 420, SetTo, 0),
        SetMemory(0x660A70 + 424, SetTo, 0),
        SetMemory(0x660A70 + 428, SetTo, 0),
        SetMemory(0x660A70 + 432, SetTo, 0),
        SetMemory(0x660A70 + 436, SetTo, 0),
        SetMemory(0x660A70 + 440, SetTo, 0),
        SetMemory(0x660A70 + 444, SetTo, 0),
        SetMemory(0x660A70 + 448, SetTo, 0),
        SetMemory(0x660A70 + 452, SetTo, 0),
        SetMemory(0x6558C0 + 0, SetTo, 851969),
        SetMemory(0x6558C0 + 4, SetTo, 2424857),
        SetMemory(0x6558C0 + 8, SetTo, 4456499),
        SetMemory(0x6558C0 + 12, SetTo, 5898319),
        SetMemory(0x6558C0 + 16, SetTo, 7471206),
        SetMemory(0x6558C0 + 20, SetTo, 9175166),
        SetMemory(0x6558C0 + 24, SetTo, 11206810),
        SetMemory(0x6558C0 + 28, SetTo, 12648630),
        SetMemory(0x6558C0 + 32, SetTo, 13697228),
        SetMemory(0x6558C0 + 36, SetTo, 14024704),
        SetMemory(0x6558C0 + 40, SetTo, 14680283),
        SetMemory(0x6558C0 + 44, SetTo, 15335653),
        SetMemory(0x6558C0 + 48, SetTo, 16122095),
        SetMemory(0x6558C0 + 52, SetTo, 17039613),
        SetMemory(0x6558C0 + 56, SetTo, 17629448),
        SetMemory(0x6558C0 + 60, SetTo, 18153745),
        SetMemory(0x6558C0 + 64, SetTo, 18678041),
        SetMemory(0x6558C0 + 68, SetTo, 19202337),
        SetMemory(0x6558C0 + 72, SetTo, 19726633),
        SetMemory(0x6558C0 + 76, SetTo, 20250929),
        SetMemory(0x6558C0 + 80, SetTo, 20775225),
        SetMemory(0x6558C0 + 84, SetTo, 21299521),
        SetMemory(0x6558C0 + 88, SetTo, 329),
        SetMemory(0x6558C0 + 92, SetTo, 21823488),
        SetMemory(0x6558C0 + 96, SetTo, 22151168),
        SetMemory(0x6558C0 + 100, SetTo, 22478848),
        SetMemory(0x6558C0 + 104, SetTo, 23200093),
        SetMemory(0x6558C0 + 108, SetTo, 359),
        SetMemory(0x6558C0 + 112, SetTo, 0),
        SetMemory(0x6558C0 + 116, SetTo, 0),
        SetMemory(0x656198 + 0, SetTo, 393217),
        SetMemory(0x656198 + 4, SetTo, 1048587),
        SetMemory(0x656198 + 8, SetTo, 1376256),
        SetMemory(0x656198 + 12, SetTo, 1703936),
        SetMemory(0x656198 + 16, SetTo, 2359327),
        SetMemory(0x656198 + 20, SetTo, 3014697),
        SetMemory(0x656198 + 24, SetTo, 3670016),
        SetMemory(0x656198 + 28, SetTo, 3932160),
        SetMemory(0x656198 + 32, SetTo, 4456512),
        SetMemory(0x656198 + 36, SetTo, 4980808),
        SetMemory(0x656198 + 40, SetTo, 5505104),
        SetMemory(0x656198 + 44, SetTo, 88),
        SetMemory(0x656198 + 48, SetTo, 6422620),
        SetMemory(0x656198 + 52, SetTo, 6750208),
        SetMemory(0x656198 + 56, SetTo, 7077888),
        SetMemory(0x656198 + 60, SetTo, 7798897),
        SetMemory(0x656198 + 64, SetTo, 124),
        SetMemory(0x656198 + 68, SetTo, 0),
        SetMemory(0x656198 + 72, SetTo, 0),
        SetMemory(0x656198 + 76, SetTo, 0),
        SetMemory(0x656198 + 80, SetTo, 0),
        SetMemory(0x656198 + 84, SetTo, 0),
        SetMemory(0x6562F8 + 0, SetTo, 1048577),
        SetMemory(0x6562F8 + 4, SetTo, 2818082),
        SetMemory(0x6562F8 + 8, SetTo, 3670069),
        SetMemory(0x6562F8 + 12, SetTo, 5046343),
        SetMemory(0x6562F8 + 16, SetTo, 6619222),
        SetMemory(0x6562F8 + 20, SetTo, 8585326),
        SetMemory(0x6562F8 + 24, SetTo, 10944673),
        SetMemory(0x6562F8 + 28, SetTo, 11993264),
        SetMemory(0x6562F8 + 32, SetTo, 13697217),
        SetMemory(0x6562F8 + 36, SetTo, 14942430),
        SetMemory(0x6562F8 + 40, SetTo, 16318704),
        SetMemory(0x6562F8 + 44, SetTo, 17498370),
        SetMemory(0x6562F8 + 48, SetTo, 17957134),
        SetMemory(0x6562F8 + 52, SetTo, 18546688),
        SetMemory(0x6562F8 + 56, SetTo, 19071263),
        SetMemory(0x6562F8 + 60, SetTo, 19530022),
        SetMemory(0x6562F8 + 64, SetTo, 302),
        SetMemory(0x6562F8 + 68, SetTo, 307),
        SetMemory(0x6562F8 + 72, SetTo, 0),
        SetMemory(0x6562F8 + 76, SetTo, 0),
        SetMemory(0x6562F8 + 80, SetTo, 0),
        SetMemory(0x6562F8 + 84, SetTo, 0),
        SetMemory(0x665580 + 0, SetTo, 327682),
        SetMemory(0x665580 + 4, SetTo, 786440),
        SetMemory(0x665580 + 8, SetTo, 1310736),
        SetMemory(0x665580 + 12, SetTo, 1835032),
        SetMemory(0x665580 + 16, SetTo, 2621476),
        SetMemory(0x665580 + 20, SetTo, 3145772),
        SetMemory(0x665580 + 24, SetTo, 3670068),
        SetMemory(0x665580 + 28, SetTo, 4194364),
        SetMemory(0x665580 + 32, SetTo, 0),
        SetMemory(0x665580 + 36, SetTo, 5308484),
        SetMemory(0x665580 + 40, SetTo, 7405677),
        SetMemory(0x665580 + 44, SetTo, 7929973),
        SetMemory(0x665580 + 48, SetTo, 8126464),
        SetMemory(0x665580 + 52, SetTo, 8650880),
        SetMemory(0x665580 + 56, SetTo, 9568395),
        SetMemory(0x665580 + 60, SetTo, 10289305),
        SetMemory(0x665580 + 64, SetTo, 10813601),
        SetMemory(0x665580 + 68, SetTo, 11337897),
        SetMemory(0x665580 + 72, SetTo, 177),
        SetMemory(0x665580 + 76, SetTo, 11730944),
        SetMemory(0x665580 + 80, SetTo, 12124342),
        SetMemory(0x665580 + 84, SetTo, 0),
        SetMemory(0x665580 + 88, SetTo, 0),
        SetMemory(0x665580 + 92, SetTo, 192),
        SetMemory(0x665580 + 96, SetTo, 12910592),
        SetMemory(0x665580 + 100, SetTo, 13697225),
        SetMemory(0x665580 + 104, SetTo, 15139039),
        SetMemory(0x665580 + 108, SetTo, 16187631),
        SetMemory(0x665580 + 112, SetTo, 17629445),
        SetMemory(0x665580 + 116, SetTo, 18678037),
        SetMemory(0x665580 + 120, SetTo, 19726629),
        SetMemory(0x665580 + 124, SetTo, 309),
        SetMemory(0x665580 + 128, SetTo, 21102909),
        SetMemory(0x665580 + 132, SetTo, 21364736),
        SetMemory(0x665580 + 136, SetTo, 21626880),
        SetMemory(0x665580 + 140, SetTo, 22085965),
        SetMemory(0x665580 + 144, SetTo, 341),
        SetMemory(0x665580 + 148, SetTo, 345),
        SetMemory(0x665580 + 152, SetTo, 22806528),
        SetMemory(0x665580 + 156, SetTo, 23789921),
        SetMemory(0x665580 + 160, SetTo, 24183150),
        SetMemory(0x665580 + 164, SetTo, 372),
        SetMemory(0x665580 + 168, SetTo, 24772983),
        SetMemory(0x665580 + 172, SetTo, 381),
        SetMemory(0x665580 + 176, SetTo, 0),
        SetMemory(0x665580 + 180, SetTo, 384),
        SetMemory(0x665580 + 184, SetTo, 25559427),
        SetMemory(0x665580 + 188, SetTo, 26149260),
        SetMemory(0x665580 + 192, SetTo, 26411008),
        SetMemory(0x665580 + 196, SetTo, 0),
        SetMemory(0x665580 + 200, SetTo, 26804630),
        SetMemory(0x665580 + 204, SetTo, 27787686),
        SetMemory(0x665580 + 208, SetTo, 431),
        SetMemory(0x665580 + 212, SetTo, 28508160),
        SetMemory(0x665580 + 216, SetTo, 439),
        SetMemory(0x665580 + 220, SetTo, 29229056),
        SetMemory(0x665580 + 224, SetTo, 449),
        SetMemory(0x665580 + 228, SetTo, 0),
        SetMemory(0x665580 + 232, SetTo, 0),
        SetMemory(0x665580 + 236, SetTo, 0),
        SetMemory(0x665580 + 240, SetTo, 0),
        SetMemory(0x665580 + 244, SetTo, 29622272),
        SetMemory(0x665580 + 248, SetTo, 29884416),
        SetMemory(0x665580 + 252, SetTo, 30409164),
        SetMemory(0x665580 + 256, SetTo, 30933460),
        SetMemory(0x665580 + 260, SetTo, 31719900),
        SetMemory(0x665580 + 264, SetTo, 32178176),
        SetMemory(0x665580 + 268, SetTo, 32702958),
        SetMemory(0x665580 + 272, SetTo, 504),
        SetMemory(0x665580 + 276, SetTo, 0),
        SetMemory(0x665580 + 280, SetTo, 512),
        SetMemory(0x665580 + 284, SetTo, 0),
        SetMemory(0x665580 + 288, SetTo, 0),
        SetMemory(0x665580 + 292, SetTo, 0),
        SetMemory(0x665580 + 296, SetTo, 0),
        SetMemory(0x665580 + 300, SetTo, 0),
        SetMemory(0x665580 + 304, SetTo, 516),
        SetMemory(0x665580 + 308, SetTo, 34078720),
        SetMemory(0x665580 + 312, SetTo, 34734080),
        SetMemory(0x665580 + 316, SetTo, 0),
        SetMemory(0x665580 + 320, SetTo, 0),
        SetMemory(0x665580 + 324, SetTo, 0),
        SetMemory(0x665580 + 328, SetTo, 34996224),
        SetMemory(0x665580 + 332, SetTo, 36569626),
        SetMemory(0x665580 + 336, SetTo, 38470206),
        SetMemory(0x665580 + 340, SetTo, 40567384),
        SetMemory(0x665580 + 344, SetTo, 0),
        SetMemory(0x665580 + 348, SetTo, 41811968),
        SetMemory(0x665580 + 352, SetTo, 42336898),
        SetMemory(0x665580 + 356, SetTo, 650),
        SetMemory(0x665580 + 360, SetTo, 0),
        SetMemory(0x665580 + 364, SetTo, 654),
        SetMemory(0x665580 + 368, SetTo, 0),
        SetMemory(0x665580 + 372, SetTo, 0),
    ])
    

