import json
f = open('theme.json', encoding="utf-8")
data = json.load(f)

themename = "тестhex"
styles = [['rgba(65, 122, 166, 1)', 'rgba(30, 39, 53, 1)', 'rgba(255, 184, 89, 1)'],
          ['rgba(60, 45, 132, 1)', 'rgba(30, 39, 53, 1)', 'rgba(223, 205, 131, 1)'],
          ['#FF249E37', '#FF254739', '#FF19ED3B'],
          ['#249E37', '#254739', '#19ED3B']]
style = styles[3]

for index, widgettype in enumerate(data['WidgetStyles']['$values']):
    data['WidgetStyles']['$values'][index]['Title']['Background']['Color']['Color'] = style[0]
    data['WidgetStyles']['$values'][index]['Background']['Color']['Color'] = style[1]

data['WidgetStyles']['$values'][15]['FillColor'] = style[2]
data['Name'] = themename


with open(f'{themename}.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False, indent='\t')
f.close()