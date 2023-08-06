import os
import re
import sys
import bs4
import json
import time
import httpx
from tqdm import tqdm
ocr_status = False
if os.name == 'nt':
    try:
        import ddddocr
        ocr_status = True
    except ImportError:
        sys.stderr.write('如果想使用验证码自动识别功能，请先安装ddddocr库，命令为：pip install ddddocr\n')


class OJ:

    def __init__(self,
                 user_id,  # 用户ID
                 password,  # 密码
                 mode='校外',  # 访问模式 [校内/校外]
                 nickname=None,  # 昵称
                 email=None,  # 邮箱
                 school=None,  # 学校
                 code_mode='自动' if ocr_status else '手动',  # 验证码识别模式 [自动/手动]
                 wvpn_token=None,  # 校内访问模式下的wvpn_token
                 ):
        """
        :param user_id: 用户ID
        :param password: 密码
        :param mode: 访问模式 [校内/校外]
        :param nickname: 昵称
        :param email: 邮箱
        :param school: 学校
        :param code_mode: 验证码识别模式 [自动/手动]
        :param wvpn_token: 校内访问模式下的wvpn_token
        """
        self.user_id = user_id
        self.nick = nickname or user_id
        self.school = '山东工商学院'
        self.password = password
        self.email = email or '1838696034@qq.com'
        self.mode = mode if mode in ['校内', '校外'] else '校外'
        self.code_mode = code_mode if code_mode in ['自动', '手动'] else '手动'
        self.cookies = None
        self.wvpn_token = wvpn_token
        self.base_url = 'https://acm.sdtbu.edu.cn/' if self.mode == '校内' else 'https://wvpn.sdtbu.edu.cn/https/77726476706e69737468656265737421f1f44cd234347c526b468ca88d1b203b/'
        if wvpn_token:
            self.cookies = {
                'show_vpn': '0',
                'show_faq': '0',
                'wengine_vpn_ticketwvpn_sdtbu_edu_cn': wvpn_token
            }
        self._info = None

    def _get_vcode(self, s):
        if self.code_mode == '自动':
            img = s.get(f'{self.base_url}JudgeOnline/vcode.php?nowtime={int(time.time())}').content
            return ddddocr.DdddOcr(show_ad=False).classification(img)
        else:
            print(f'打开网址获取验证码: {self.base_url}JudgeOnline/vcode.php?nowtime={int(time.time())}')
            return input('请输入验证码：')

    def _set_wvpn_cookie(self, s):
        """
        设置wvpn_token
        :param s: httpx.Client
        :return: None
        """
        s.cookies.set('wengine_vpn_ticketwvpn_sdtbu_edu_cn', self.wvpn_token)
        s.cookies.set('show_vpn', '0')
        s.cookies.set('show_faq', '0')

    def login(self):
        """
        登录
        :return: None
        """
        with httpx.Client() as s:
            self.wvpn_token and self._set_wvpn_cookie(s)
            while True:
                result = self._get_vcode(s)
                s.post(f'{self.base_url}JudgeOnline/loginD.php', data={
                    'user_id': self.user_id,
                    'password': self.password,
                    'vcodeD': result
                })
                _r = s.get(f'{self.base_url}JudgeOnline/loginpageD.php')
                if re.search('Please logout First!</a>', _r.text):
                    print(f'{self.user_id}登录成功!')
                    self.cookies = s.cookies
                    return self
                else:
                    print(f'{self.user_id}登录失败，正在重试...')
                    continue

    def register(self):
        """
        注册
        :return: None
        """
        with httpx.Client() as s:
            self.wvpn_token and self._set_wvpn_cookie(s)
            print(f'{self.user_id}正在注册:')
            while True:
                result = self._get_vcode(s)
                r = s.post(f'{self.base_url}JudgeOnline/register.php', data={
                    'user_id': self.user_id,
                    'nick': self.user_id,
                    'password': self.password,
                    'rptpassword': self.password,
                    'school': self.school,
                    'email': self.email,
                    'vcode': result,
                })
                try:
                    result = re.search("alert\('(.*?)'\);", r.text)[1]
                    if result == r'Vcode Wrong!\n':
                        print(f'{self.user_id}注册失败，正在重试 [验证码错误]')
                        continue
                    elif result == r'User Existed!\n':
                        print(f'{self.user_id}注册失败 [ 用户已存在 ]')
                        return False
                except Exception:
                    print(f'{self.user_id}注册成功!')
                    self.cookies = s.cookies
                    return self

    def modify(self, nickname=None, email=None, password=None):
        """
        修改信息
        :param nickname: 新昵称
        :param email: 新邮箱
        :param password: 新密码
        """
        data = httpx.get(f'{self.base_url}JudgeOnline/modifypage.php', cookies=self.cookies)
        post_key = bs4.BeautifulSoup(data.text, 'lxml').find_all('table')[-1].find_all('tr')[1].find_all('input')[0].get('value')
        httpx.post(f'{self.base_url}JudgeOnline/modify.php', data={
            'postkey': post_key,
            'nick': nickname or self.nick,
            'opassword': self.password,
            'npassword': password or '',
            'rpassword': password or '',
            'school': self.school,
            'email': email or self.email,
            'submit': 'Submit'
        }, cookies=self.cookies)
        self.nick = nickname or self.nick
        self.email = email or self.email
        self.password = password or self.password
        print(f'{self.user_id}修改成功!')

    def submit(self, _id, language, _code):
        """
        提交代码
        :param _id: 题目ID
        :param language: 程序语言[C / C++ / Java / Python / Ruby / Pascal]
        :param _code: 代码
        :return:
        """
        if language == 'C':
            language = 0
        elif language == 'C++':
            language = 1
        elif language == 'Pascal':
            language = 2
        elif language == 'Java':
            language = 3
        elif language == 'Ruby':
            language = 4
        elif language == 'Python':
            language = 6
        httpx.post(f'{self.base_url}JudgeOnline/submit.php', data={
            'id': _id,
            'language': language,
            'source': _code
        }, cookies=self.cookies)

    def get_code_by_sid(self, sid):
        """
        根据sid获取代码
        :param sid: 提交ID
        :return:
        """
        _r = httpx.get(f'{self.base_url}JudgeOnline/submitpage.php?id=99999&sid={sid}', cookies=self.cookies)
        return _r.text[re.search('<textarea cols=80 rows=20 id="source" name="source">', _r.text).span()[1]:
                       re.search('</textarea>', _r.text).span()[0]]

    def check_problem_exist(self, _id):
        """
        检查题目是否存在
        :param _id: 题目ID
        :return: bool
        """
        r = httpx.get(f'{self.base_url}JudgeOnline/problem.php', params={
            'id': _id
        })
        return not re.search('Problem is not Available!!', r.text)

    def info(self, refresh=False):
        """
        获取用户信息
        :param refresh: 是否刷新
        :return:
        """
        if self._info and not refresh:
            return self._info
        next_page_url = f'{self.base_url}JudgeOnline/status.php'
        datas = {}
        while True:
            r = httpx.get(next_page_url, params={
                'user_id': self.user_id,
                'jresult': 4
            }, cookies=self.cookies)
            soup = bs4.BeautifulSoup(r.text, 'lxml')
            tabel = soup.find_all('table')[-1]
            trs = tabel.find_all('tr')[1:]
            for tr in trs:
                tds = tr.find_all('td')
                datas[tds[2].text] = {
                    'sid': int(tds[0].text),
                    'code': tds[6].text.split('/')[0],
                }
            if len(trs) != 20:
                self._info = datas
                return datas
            next_page_url = f'{self.base_url}JudgeOnline/' + soup.find_all('center')[0].find_all('a')[-1].get('href')

    def save(self, path, simple_mode=False):
        """
        保存用户信息
        :param path: 保存路径
        :param simple_mode: 简单模式
        """
        print('正在保存, 模式: ', '简单' if simple_mode else '详细')
        if not simple_mode:
            datas = tqdm(self.info().items())
            for key, value in datas:
                datas.set_description(f'正在获取代码: {key}')
                sid = value['sid']
                code = self.get_code_by_sid(sid)
                self._info[key]['content'] = code
        print('正在保存到文件...')
        with open(path, 'w') as f:
            json.dump(self.info(), f)
        print('保存成功!')

    def load_and_submit(self, path, interval=10):
        """
        从文件加载并提交
        :param interval: 题目提交间隔时间（单位: 秒），速度过快可能会导致提交失败
        :param path: 文件路径
        """
        with open(path, 'r') as f:
            datas = json.load(f)
        if 'content' not in list(datas.values())[0]:
            print('文件格式错误，请检查是否以非简单模式保存!')
            return
        datas = tqdm(datas.items())
        for key, value in datas:
            datas.set_description(f'正在提交代码: {key}')
            if key in self.info():
                continue
            self.submit(key, value['code'], value['content'])
            time.sleep(interval)

    def submit_test_code(self, interval=11):
        """
        测试提交代码
        :param interval: 题目提交间隔时间（单位: 秒），速度过快可能会导致提交失败
        :param path: 文件路径
        """
        sys.stderr.write('您正在使用内部测试代码，请正确使用该方法进行测试，如若用于不法用途，后果自负，如果您不知道这是什么，请忽略此消息\n')
        sys.stderr.write(
            '这些测试代码由广大网友分享提供，如果您也想贡献代码，您可以将该库生成的完整数据文件通过邮件发送至邮箱1838696034@qq.com，万分感激\n')
        sys.stderr.write('您可以通过指令: 「 pip install --upgrade sdtbu-acm-tool 」将数据库更新至最新版本\n')
        self.load_and_submit(os.path.join(os.path.dirname(__file__), 'base_code.py'), interval)
