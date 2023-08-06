class Session:
    """
    需要设置API_KEYS，即： `Session.API_KEYS = 'xxx'`
    之后通过 `Session.get('你好！')` 即可访问
    """
    API_KEYS: str = ''
    openai.organization = "org-LWXuQHqowCN5qo5102Ng2niB"
    url = "https://api.openai.com/v1/completions"
    headers = {'content-type': 'application/json'}
    data = {'max_tokens': 2048, 'model': 'text-davinci-003'}

    @classmethod
    def get(cls, words: str) -> list[str]:
        assert cls.API_KEYS, "API_KEYS 未设置！使用Session.API_KEYS = 'xxx'来设置！"
        openai.api_key = cls.API_KEYS
        resp = rq.post(url, headers=headers | {'Authorization': 'Bearer ' + cls.API_KEYS}, json=data | {"prompt": words})
        resp_data = resp.json()
        assert 'error' not in resp_data, f'请求发生错误！\n{resp_data["error"]}'
        return [choices['text'] for choices in resp_data['choices']]
