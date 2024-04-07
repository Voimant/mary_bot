from dadata import Dadata
from pprint import pprint
from datetime import datetime
import time
from email import utils

TOKEN = "4a98ea1f3c9b7ca64b90a1d12696348acfae029a"
# dadata = Dadata(token)
# result = dadata.find_by_id(name='party', query="5907037509")
# print(result)
def test_api(inn):
    dadata = Dadata(TOKEN)
    try:
        result = dadata.find_by_id(name='party', query=inn)
        for x in result:
            state = x['data']['state']
            name = x['value']
            enn = x['data']['inn']
            manager_name = x['data']['management']['name']
            manager_ryk = x['data']['management']['post']
            adress = x['data']['address']
            area = adress['data']['source']
            status = state['status']
            actuality_date = state['actuality_date']
            registration_date = state['registration_date']
            dt = datetime.fromtimestamp(actuality_date / 1000)
            formated = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            print(formated)
            text = (f'Название Компании: {name}\n'
                    f'ИНН: {enn}\n'
                    f'Имя руководителя: {manager_name}\n'
                    f'Должность руководителя: {manager_ryk}\n\n'
                    f'Адрес: {area}\n'
                    f'СОСТОЯНИЕ\n'
                    f'Дата последних изменений: {formated}\n'
                    f'Стадия существования: {status} ')
            print(state)
            return text
    except Exception as e:
        return 'Что то пошло не так, проверьте ИНН'



    
