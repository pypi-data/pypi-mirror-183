from setuptools import setup
setup(
      name='chargpt_lfanke',
      version='0.0.1',
      description='from charget_lfanke import Session',
      author='Lfan_ke',
      author_email='chengkelfan@qq.com',
      requires= ['requests','openai'], # 定义依赖哪些模块
      py_modules=['__init__'],
      license="apache 3.0"
      )

