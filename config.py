"""
配置文件，模板已写好，直接调用就行

使用方法:
使用前需要打下面三行代码
1. `from mymodule.config import Config`
2. `config = Config()`
3. `config.default_config = ...`
然后就可以用了

`default_config`储存默认配置
`config`储存读取的配置

一些方法：
* load()                    读取配置文件，储存在config.config这个字典里
* save()                    保存配置文件
* create_default_config()   生成默认配置文件
* update_config_value()     更新配置文件的值，使用 “.” 来表示子字典
                                例如 `a.b.c` 等价于 `config[a][b][c]`
* check()                   检查配置文件是否完整，在调用`load()`时会自动调用
"""

import os
import yaml
from math import isclose

from logger import logger


class Config:
    """
    配置文件，模板已写好，直接调用就行

    使用方法:
    使用前需要打下面几行代码
    1. `from mymod.config import Config`
    2. `config = Config()`
    3. `config.default_config = ...`
    然后就可以用了

    `default_config`储存默认配置
    `config`储存读取的配置

    一些方法：
    * load()                    读取配置文件，储存在config.config这个字典里
    * save()                    保存配置文件
    * create_default_config()   生成默认配置文件
    * update_config_value()     更新配置文件的值，使用 “.” 来表示子字典
                                    例如 `a.b.c` 等价于 `config[a][b][c]`
                                    就像这样：update_config_value('a.b.c', new_value)
    * check()                   检查配置文件是否完整，在调用`load()`时会自动调用
    """

    default_config = {}
    config = {}
    path: str
    cfg_file_name: str

    def __init__(self, default_config, path: str = './', cfg_file_name: str = 'config.yml'):
        self.path = path
        self.cfg_file_name = cfg_file_name
        self.default_config = default_config

    def check(self, config: dict, default_config: dict) -> None:
        def recursive_check(config: dict, default_config: dict):
            for key, value in default_config.items():
                if key not in config:
                    logger.warning(f'检测到配置错误: 配置文件缺少 {key}')
                    logger.warning('使用默认值代替')
                    config[key] = value
                elif not isinstance(config[key], type(value)):
                    try:
                        raise TypeError(f'配置文件中键 {key} 的值不是 {type(value)} 类型数据')
                    except TypeError as e:
                        logger.catch_exc('捕捉异常：TypeError')
                        logger.catch_exc(e)
                        logger.warning('检测到配置错误，使用默认值代替')
                        config[key] = value
                elif type(value) == type(config[key]) == dict:
                    recursive_check(config[key], value)

        recursive_check(config, default_config)
        self.save()

    def create_default_config(self) -> None:
        if not os.path.exists(self.path): os.mkdir(self.path)
        with open(self.path + self.cfg_file_name, 'w', encoding='utf-8') as f:
            yaml.dump(self.default_config, f, allow_unicode=True)

    def load(self) -> dict:
        # check whether exist config file
        if not os.path.exists(self.path + self.cfg_file_name):
            logger.warning('未找到配置文件！')
            logger.warning('即将创建默认配置文件')
            self.create_default_config()

        # read config
        with open(self.path + self.cfg_file_name, encoding='utf-8') as f:
            for cfgs in yaml.safe_load_all(f):
                self.config.update(cfgs)

        while self.config == {}:
            if self.config == {}:
                logger.warning('默认配置为空！')
                logger.warning('请使用"config.default_config = "添加默认配置')
                raise SystemExit(-1)
            if isclose(os.path.getsize(self.path + self.cfg_file_name), 0, abs_tol=512, rel_tol=512):
                logger.warning('配置文件为空文件！')
                logger.warning('即将创建默认配置文件')
                self.create_default_config()
                break
            logger.crit('配置文件读取失败！')
            logger.crit('请在Github上提交一个PR反映此问题')
            raise SystemExit(-1)
        self.check(self.config, self.default_config)
        return self.config

    def save(self) -> None:
        with open(self.path + self.cfg_file_name, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, allow_unicode=True)

    def update_config_value(self, key, value) -> None:
        def recursive_update(cfg, key_list, value):
            if len(key_list) == 1:
                cfg[key_list[0]] = value
            else:
                recursive_update(
                    cfg[key_list[0]], key_list[1:], value
                )

        key_list = key.split('.')
        recursive_update(self.config, key_list, value)

    def get_value(self, key) -> any:
        def recursive_get(cfg, key_list):
            if len(key_list) == 1:
                return cfg[key_list[0]]
            else:
                return recursive_get(
                    cfg[key_list[0]], key_list[1:]
                )

        key_list = key.split('.')
        return recursive_get(self.config, key_list)

    def get_config(self) -> dict:
        return self.config
