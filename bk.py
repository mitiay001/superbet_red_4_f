import requests
from bs4 import BeautifulSoup
from time import sleep
import datetime
import traceback

def error_log(text, e, string):
    d = datetime.datetime.now()
    d = d.strftime('%d.%m.%Y %H:%M:%S')
    d = '-------='+d+'=-------\n'
    with open ('logs.txt', 'a', encoding='utf-8') as file:
        file.write('##############-'+text+'-##############'+'\n')
        file.write(d)
        file.write(string)
        file.write(str(traceback.format_exc())+'\n')
    print((traceback.format_exc()))
    print('###########-=ERROR=-###########')

def get_data(ses):
    url = 'https://su.surebet.com/valuebets?utf8=%E2%9C%93&selector%5Bmin_group_size%5D=2&selector%5Bsettled_in%5D=0&selector%5Bmin_odds%5D=1.5&selector%5Bmax_odds%5D=5.0&selector%5Bmin_probability%5D=60.0&selector%5Bmax_probability%5D=100.0&selector%5Bmin_overvalue%5D=25.0&selector%5Bmax_overvalue%5D=&selector%5Bbookies_settings%5D=0%3A67%3A%3A%3B0%3A105%3A%3A%3B0%3A72%3A%3A%3B0%3A66%3A%3A%3B0%3A76%3A%3A%3B0%3A93%3A%3A%3B4%3A182%3A%3A%3B4%3A74%3A%3A%3B0%3A37%3A%3A%3B0%3A148%3A%3A%3B0%3A211%3A%3A%3B0%3A114%3A%3A%3B0%3A260%3A%3A%3B0%3A101%3A%3A%3B0%3A132%3A%3A%3B0%3A42%3A%3A%3B0%3A40%3A%3A%3B0%3A225%3A%3A%3B0%3A126%3A%3A%3B0%3A201%3A%3A%3B4%3A21%3A%3A%3B0%3A70%3A%3A%3B0%3A263%3A%3A%3B0%3A246%3A%3A%3B0%3A26%3A%3A%3B0%3A139%3A%3A%3B0%3A111%3A%3A%3B0%3A36%3A%3A%3B0%3A150%3A%3A%3B0%3A202%3A%3A%3B0%3A151%3A%3A%3B0%3A23%3A%3A%3B0%3A204%3A%3A%3B0%3A200%3A%3A%3B0%3A203%3A%3A%3B4%3A60%3A%3A%3B0%3A116%3A%3A%3B0%3A32%3A%3A%3B0%3A138%3A%3A%3B0%3A1%3A%3A%3B0%3A65%3A%3A%3B0%3A161%3A%3A%3B0%3A29%3A%3A%3B0%3A10%3A%3A%3B0%3A107%3A%3A%3B0%3A106%3A%3A%3B0%3A45%3A%3A%3B0%3A228%3A%3A%3B0%3A34%3A%3A%3B0%3A77%3A%3A%3B0%3A58%3A%3A%3B0%3A253%3A%3A%3B0%3A165%3A%3A%3B0%3A100%3A%3A%3B0%3A153%3A%3A%3B0%3A95%3A%3A%3B0%3A180%3A%3A%3B0%3A208%3A%3A%3B0%3A48%3A%3A%3B0%3A14%3A%3A%3B0%3A197%3A%3A%3B0%3A152%3A%3A%3B0%3A11%3A%3A%3B0%3A188%3A%3A%3B0%3A38%3A%3A%3B0%3A147%3A%3A%3B0%3A52%3A%3A%3B0%3A198%3A%3A%3B0%3A55%3A%3A%3B0%3A187%3A%3A%3B0%3A33%3A%3A%3B0%3A13%3A%3A%3B0%3A68%3A%3A%3B0%3A176%3A%3A%3B4%3A125%3A%3A%3B0%3A248%3A%3A%3B0%3A236%3A%3A%3B0%3A49%3A%3A%3B0%3A215%3A%3A%3B0%3A113%3A%3A%3B0%3A62%3A%3A%3B0%3A75%3A%3A%3B0%3A12%3A%3A%3B0%3A177%3A%3A%3B0%3A193%3A%3A%3B0%3A157%3A%3A%3B0%3A90%3A%3A%3B0%3A46%3A%3A%3B0%3A229%3A%3A%3B0%3A210%3A%3A%3B0%3A146%3A%3A%3B0%3A117%3A%3A%3B0%3A135%3A%3A%3B0%3A24%3A%3A%3B0%3A92%3A%3A%3B0%3A88%3A%3A%3B0%3A73%3A%3A%3B0%3A171%3A%3A%3B0%3A53%3A%3A%3B0%3A261%3A%3A%3B0%3A144%3A%3A%3B0%3A121%3A%3A%3B0%3A154%3A%3A%3B0%3A129%3A%3A%3B0%3A214%3A%3A%3B0%3A56%3A%3A%3B0%3A170%3A%3A%3B0%3A104%3A%3A%3B0%3A108%3A%3A%3B0%3A230%3A%3A%3B0%3A22%3A%3A%3B0%3A158%3A%3A%3B0%3A145%3A%3A%3B0%3A136%3A%3A%3B0%3A109%3A%3A%3B0%3A257%3A%3A%3B0%3A5%3A%3A%3B0%3A162%3A%3A%3B4%3A6%3A%3A%3B0%3A112%3A%3A%3B0%3A245%3A%3A%3B0%3A235%3A%3A%3B0%3A175%3A%3A%3B0%3A224%3A%3A%3B0%3A190%3A%3A%3B0%3A4%3A%3A%3B0%3A183%3A%3A%3B0%3A242%3A%3A%3B0%3A213%3A%3A%3B0%3A244%3A%3A%3B0%3A30%3A%3A%3B0%3A15%3A%3A%3B0%3A212%3A%3A%3B0%3A219%3A%3A%3B0%3A128%3A%3A%3B0%3A233%3A%3A%3B0%3A50%3A%3A%3B4%3A9%3A%3A%3B0%3A259%3A%3A%3B0%3A179%3A%3A%3B0%3A178%3A%3A%3B4%3A41%3A%3A%3B0%3A85%3A%3A%3B0%3A169%3A%3A%3B0%3A84%3A%3A%3B0%3A130%3A%3A%3B0%3A133%3A%3A%3B0%3A247%3A%3A%3B4%3A3%3A%3A%3B0%3A131%3A%3A%3B0%3A240%3A%3A%3B0%3A8%3A%3A%3B0%3A118%3A%3A%3B4%3A89%3A%3A%3B0%3A166%3A%3A%3B0%3A124%3A%3A%3B0%3A226%3A%3A%3B0%3A209%3A%3A%3B0%3A82%3A%3A%3B0%3A63%3A%3A%3B0%3A83%3A%3A%3B0%3A98%3A%3A%3B0%3A99%3A%3A%3B0%3A61%3A%3A%3B0%3A167%3A%3A%3B0%3A137%3A%3A%3B0%3A141%3A%3A%3B0%3A19%3A%3A%3B0%3A142%3A%3A%3B0%3A164%3A%3A%3B0%3A249%3A%3A%3B0%3A39%3A%3A%3B0%3A174%3A%3A%3B4%3A31%3A%3A%3B0%3A54%3A%3A%3B0%3A51%3A%3A%3B0%3A181%3A%3A%3B0%3A2%3A%3A%3B0%3A87%3A%3A%3B4%3A143%3A%3A%3B0%3A122%3A%3A%3B0%3A7%3A%3A%3B0%3A189%3A%3A%3B0%3A172%3A%3A%3B0%3A237%3A%3A%3B0%3A168%3A%3A%3B0%3A156%3A%3A%3B0%3A47%3A%3A%3B0%3A262%3A%3A%3B0%3A134%3A%3A%3B0%3A218%3A%3A%3B0%3A123%3A%3A%3B0%3A94%3A%3A%3B0%3A254%3A%3A%3B0%3A25%3A%3A%3B0%3A69%3A%3A%3B0%3A140%3A%3A%3B0%3A119%3A%3A%3B0%3A16%3A%3A%3B0%3A207%3A%3A%3B0%3A232%3A%3A%3B0%3A223%3A%3A%3B0%3A163%3A%3A%3B0%3A256%3A%3A%3B0%3A97%3A%3A%3B0%3A173%3A%3A%3B0%3A191%3A%3A%3B0%3A186%3A%3A%3B0%3A192%3A%3A%3B0%3A43%3A%3A%3B0%3A243%3A%3A%3B0%3A199%3A%3A%3B0%3A103%3A%3A%3B0%3A159%3A%3A%3B0%3A184%3A%3A%3B4%3A18%3A%3A%3B0%3A35%3A%3A%3B0%3A59%3A%3A%3B0%3A64%3A%3A%3B0%3A216%3A%3A%3B0%3A86%3A%3A%3B0%3A120%3A%3A%3B0%3A205%3A%3A%3B0%3A149%3A%3A%3B0%3A127%3A%3A%3B0%3A115%3A%3A%3B0%3A17%3A%3A%3B0%3A160%3A%3A%3B0%3A110%3A%3A%3B0%3A238%3A%3A%3B0%3A102%3A%3A%3B0%3A239%3A%3A%3B0%3A217%3A%3A%3B0%3A96%3A%3A%3B0%3A28%3A%3A%3B0%3A220%3A%3A%3B0%3A222%3A%3A%3B0%3A250%3A%3A%3B0%3A252%3A%3A%3B4%3A44%3A%3A%3B0%3A196%3A%3A%3B0%3A227%3A%3A%3B0%3A206%3A%3A%3B0%3A155%3A%3A%3B0%3A221%3A%3A%3B0%3A71%3A%3A%3B0%3A79%3A%3A%3B0%3A80%3A%3A%3B0%3A78%3A%3A%3B0%3A57%3A%3A%3B0%3A81%3A%3A%3B4%3A27%3A%3A&selector%5Bexclude_sports_ids_str%5D=1+47+46+48+49+59+53+54+58+62+61+50+51&commit=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C&narrow='
    response = ses.get(url)
    #print(response.text)
    #print(response)
    return response.text

def autoriz():
    ses = requests.Session()
    url = 'https://su.surebet.com/users/sign_in'
    response = ses.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    token = soup.find('input', {'name': 'authenticity_token'}).get('value')
    with open('login.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    login = data[0].replace('\n', '')
    password = data[1].replace('\n', '')
    payload = {
        'utf8': '✓',
        'authenticity_token': token,
        'user[email]': login,
        'user[password]': password,
        'user[remember_me]': '1',
        'commit': 'Вход',
    }
    response = ses.post(url, data=payload)
    return ses

def parse_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    bloks = soup.find('table', {'class':'app-table app-wide'}).find_all('tbody')
    p_data = []
    for blok in bloks:
        string = ''
        string+=blok.find('td', {'class':'booker booker-first'}).find('a').get_text().replace('\u200b', '')+';'
        string+='https://su.surebet.com'+blok.find('td', {'class':'booker booker-first'}).find('a').get('href')+';'
        string+=blok.find('td', {'class':'booker booker-first'}).find('span').get_text()+';'
        t = str(blok.find('td', {'class':'time'})).split('>',1)[1].split('</td>')[0]
        string+=t.replace(f'<br/>', ';')+';'
        string+=blok.find('td', {'class':'event'}).find('a').get_text()+';'
        string+='https://su.surebet.com'+blok.find('td', {'class':'event'}).find('a').get('href')+';'
        string+=blok.find('td', {'class':'event'}).find('span').get_text()+';'
        coef=blok.find('td', {'class':'coeff'})
        if coef.find('sup'):
            string+=coef.get_text().replace(coef.find('sup').get_text(), '')+';'
        else:
            string+=coef.get_text()+';'
        string+=blok.find('td', {'class':'value'}).get_text(strip=True)+';'
        string+='https://su.surebet.com'+blok.find('td', {'class':'value'}).find('a').get('href')+';'
        string+=blok.find_all('td', {'class':'text-center'})[0].get_text()+';'
        string+=blok.find_all('td', {'class':'text-center'})[1].get_text()
        p_data.append(string)
    if p_data == []:
        return None
    else:
        return p_data

def send_telegram_message(mess):
    bot_token = '6982606566:AAF-m6QNCdEdaFVP2EIB4-5RplN5--82now'
    chat_id = '-1002098970878'
    mess = mess.split(';')
    #print(mess[0])
    message = ''
    if '1Win' in mess[0]:
        link = 'https://1win.pro/'
    elif '1xBet' in mess[0]:
        link = 'https://www.1xbet.it/'
    elif 'BaltBet' in mess[0]:
        link = 'https://baltbet.ru/'
    elif 'Leon' in mess[0]:
        link = 'https://leon.bet/'
    elif 'LigaStavok' in mess[0]:
        link = 'https://www.ligastavok.ru/'
    elif 'Marathon' in mess[0]:
        link = 'https://www.marathonbet.com/'
    elif 'MelBet' in mess[0]:
        link = 'https://melbet.com/ru'
    elif 'BetBoom' in mess[0]:
        link = 'https://sport.betboom.ru/'
    elif 'Olimp' in mess[0]:
        link = 'https://21olimp.com/'
    elif 'Pin-up' in mess[0]:
        link = 'https://sport.pin-up.bet/'
    elif 'Tennisi' in mess[0]:
        link = 'https://www.tennisi.com/'
    elif 'Winline' in mess[0]:
        link = 'https://winline.ru/'
    elif 'FonBet' in mess[0]:
        link = 'https://www.fon.bet/'
    elif 'Zenit' in mess[0]:
        link = 'https://zenitnow486.top/'
    elif 'BetCity' in mess[0]:
        link = 'https://betcityru.com/'
    message+=f'<b>Букмекер:</b> <a href="{link}">{mess[0]}</a> ({mess[2]})\n'
    message+=f'<b>Время начала:</b> {mess[3]} {mess[4]}\n'
    message+=f'<b>Событие:</b> {mess[5]} ({mess[7]})\n'
    message+=f'<b>Ставка:</b> {mess[8]}\n'
    message+=f'<b>Коэффициент:</b> {mess[9]}\n'
    message+=f'<b>Вероятность:</b> {mess[11]}\n'
    message+=f'<b>Переоценённость:</b> {mess[12]}'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message, 'parse_mode': 'HTML', 'disable_web_page_preview': True}
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(message)

    response = requests.post(url, params=params)

if __name__ == "__main__":
    while True:
        ses = requests.Session()#autoriz()
        data = get_data(ses)
        with open('base.txt', 'r', encoding='utf-8') as f:
            b_data = f.readlines()
        base_data = []
        for i in b_data:
            base_data.append(';'.join(i.split(';')[:9]))
        p_data = parse_data(data)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(datetime.datetime.now().strftime("%d %m %Y %H:%M:%S")+'\n')
        if p_data:
            for string in p_data:
                if ';'.join(string.split(';')[:9]) not in base_data:
                    try:
                        send_telegram_message(string)
                        with open('base.txt', 'a', encoding='utf-8') as f:
                            f.write(string+'\n')
                        sleep(2)
                    except Exception as e:
                        error_log('Отправка', e, string)
                else:
                    with open('log.txt', 'a', encoding='utf-8') as f:
                        f.write('есть в базе'+'\n')
        else:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write('Нет данных'+'\n')
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('Сплю\n#######\n')
        ses.close()
        sleep(120)
