import json, sys, os, time

try:
    if getattr(sys, 'frozen', False):
        f = open(os.path.join(sys._MEIPASS, 'theme.json'), encoding="utf-8")
    else:
        f = open('theme.json', encoding="utf-8")

    data = json.load(f)
    themename = input("Введите название новой темы: ")
    style = []
    for el, col in zip(['цвет фона заголовка', 'цвет фона', 'цвет спидометра'], ['249E37', '254739', '19ED3B']):
        newcol = input(f"Введите {el}, например #{col} или {col}: ")
        if not newcol.startswith("#"):
            newcol = f"#{newcol}"
        style.append(newcol)

    # themename = "тестhex"
    # styles = [['rgba(65, 122, 166, 1)', 'rgba(30, 39, 53, 1)', 'rgba(255, 184, 89, 1)'],
    #           ['rgba(60, 45, 132, 1)', 'rgba(30, 39, 53, 1)', 'rgba(223, 205, 131, 1)'],
    #           ['#FF249E37', '#FF254739', '#FF19ED3B'],
    #           ['#249E37', '#254739', '#19ED3B']]
    # style = styles[3]

    for index, widgettype in enumerate(data['WidgetStyles']['$values']):
        data['WidgetStyles']['$values'][index]['Title']['Background']['Color']['Color'] = style[0]
        data['WidgetStyles']['$values'][index]['Background']['Color']['Color'] = style[1]

    data['WidgetStyles']['$values'][15]['FillColor'] = style[2]
    data['Name'] = themename


    with open(f'{themename}.json', 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent='\t')
    f.close()
except Exception as e:
    print(e)
    time.sleep(5)