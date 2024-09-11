import Output


def startUp():
    Output.writeText('@yinian')
    Output.press_once(ord('1'))
    Output.press_once(40)
    Output.press_once(13)
    # Output.sleep(1)
    Output.writeText('xiulian')
    Output.press_once(ord('1'))
    Output.press_once(13)


def trough():
    Output.writeText('@yinian')
    Output.press_once(ord('1'))
    Output.press_once(40)
    Output.press_once(13)
    # Output.sleep(1)
    Output.writeText('zhijie')
    Output.press_once(ord('1'))
    # Output.press_once(13)
    Output.writeText('tupo')
    Output.press_once(ord('1'))
    Output.press_once(13)

def getArmy():
    Output.writeText('@yinian')
    Output.press_once(ord('1'))
    Output.press_once(40)
    Output.press_once(13)
    # Output.sleep(1)
    Output.writeText('zhaohuan')
    Output.press_once(ord('1'))
    # Output.press_once(13)
    Output.writeText('lingqi')
    Output.press_once(ord('1'))
    Output.press_once(13)

def gooutside():
    Output.writeText('@yinian')
    Output.press_once(ord('1'))
    Output.press_once(40)
    Output.press_once(13)
    # Output.sleep(1)
    Output.writeText('youli')
    Output.press_once(ord('1'))
    Output.press_once(13)
    Output.press_once(13)

def caiyao():
    Output.writeText('@yinian')
    Output.press_once(ord('1'))
    Output.press_once(40)
    Output.press_once(13)
    # Output.sleep(1)
    Output.writeText('caiyao')
    Output.press_once(ord('1'))
    Output.writeText('guilai')
    Output.press_once(ord('1'))
    Output.press_once(13)

    youli()

    Output.writeText('@yinian')
    Output.press_once(ord('1'))
    Output.press_once(40)
    Output.press_once(13)
    # Output.sleep(1)
    Output.writeText('caiyao')
    Output.press_once(ord('1'))
    Output.press_once(13)
    Output.sleep(600)

def once():
    Output.press_once(1)
    startUp()
    trough()

def youli():
    Output.moveto(100, 750)
    Output.press_once(1)
    getArmy()
    gooutside()
    Output.sleep(60)

def xiulian():
    Output.moveto(100, 750)
    Output.press_once(1)
    once()
    # Output.sleep(1)
    Output.moveto(800, 750)
    Output.press_once(1)
    once()
    Output.sleep(32)

while True:
    xiulian()