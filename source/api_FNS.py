import requests
from pprint import pprint


TOKEN = 'd4c857706efb450114aea988b0c9543167630c38'
BASE_URL_1 = 'https://api-fns.ru/api/search'

# params = {'q': '5905064232', 'key': TOKEN}
# resp = requests.get(BASE_URL_1, params=params)
# pprint(resp.json())

# main_info = resp.json()

# for x in main_info['items']:
#     adress = x['ЮЛ']['АдресПолн']
#     data_ogrn = x['ЮЛ']['ДатаОГРН']
#     inn = x['ЮЛ']['ИНН']
#     name = x['ЮЛ']['НаимПолнЮЛ']
#     name_s = x['ЮЛ']['НаимСокрЮЛ']
#     ogrn = x['ЮЛ']['ОГРН']
#     main_work = x['ЮЛ']['ОснВидДеят']
#     status = x['ЮЛ']['Статус']
#     text = (f'Адрес: {adress} \n'
#             f'Дата регистрации ОГРН: {data_ogrn}\n'
#             f'ИНН: {inn}\n'
#             f'Полное наименование: {name}\n'
#             f'Полное наименование: {name}\n'
#             f'Сокращенное название: {name_s}\n'
#             f'Основной вид деятельности:{main_work}\n'
#             f'Статус: {status}')
#     print(text)

text_1 = '''Адрес: край Пермский, г. Пермь, ул. Композитора Глинки, д.15, кв.46 
Дата регистрации ОГРН: 2020-05-22
ИНН: 5905064232
Полное наименование: ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ ЮРИДИЧЕСКАЯ КЛИНИКА "МОЗГ"
Сокращенное название: ООО ЮК "МОЗГ"
Основной вид деятельности:Деятельность в области права
Статус: Находится в стадии ликвидации'''

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)

pdf.add_page()

pdf.set_font('DejaVu', size=14)
pdf.cell(40, 10, txt='привет')
pdf.output('demo.pdf')




# BASE_url_2 = 'https://api-fns.ru/api/egr'
# params = {'req': '5905064232', 'key': TOKEN}
#
# resp = requests.get(BASE_url_2, params=params)
# pprint(resp.json())

