import os
from functools import lru_cache
from typing import List

__all__ = [
    'SysCmd', 'has_Chinese', 'listDedup',
    'ListSort', 'isChinese', 'num_len',
    'C', 'A', 'str2dict', 'str2list', 'str2bool',
]


class SysCmd:
    """
    系统命令包
    仅限 Windows
    """

    @staticmethod
    def cmd(command='help'): os.system(command)

    @staticmethod
    def mkdir(_file_name): os.makedirs(f'./{_file_name}/')

    @staticmethod
    def md(_file_name): SysCmd.mkdir(_file_name)

    @staticmethod
    def del_file(path): os.remove(path)

    @staticmethod
    def rmdir(path): os.rmdir(path)

    @staticmethod
    def rd(path): SysCmd.rmdir(path)

    @staticmethod
    def cd(work_path=None):
        if work_path is not None:
            os.chdir(work_path)
        print(os.getcwd())


def has_Chinese(string):
    """
    检测字符串内是否存在汉字
    """

    for char in string:
        if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字
            return True
    return False


def isChinese(string: str) -> bool:
    for char in string:
        if not (u'\u4e00' <= char <= u'\u9fa5'):
            return False
    return True


def num_len(num: int | float):
    """
    返回数字的长度

    Returns:
        int: 数字的长度
        tuple[int, int]: 整数部分和小数部分的长度
    """
    if not (isinstance(num, int) or isinstance(num, float)):
        raise TypeError("输入必须是一个数字")
    if isinstance(num, float):
        return tuple(
            [len(i) for i in str(num).split('.')]
        )
    else:
        return len(str(num))


def listDedup(_list: List) -> List:
    """
    给列表不打乱顺序地去重
    """
    result = []
    for i in _list:
        if i not in result:
            result.append(i)
    return result


class ListSort:
    """
    列表排序
    """

    # 选择排序
    @staticmethod
    def select(li):
        for i in range(len(li) - 1):
            _min = i
            for j in range(i + 1, len(li)):
                if li[j] < li[_min]:
                    _min = j
            li[i], li[_min] = li[_min], li[i]
        return li

    # 插入排序
    @staticmethod
    def insert(li):
        for i in range(1, len(li)):
            for j in range(i, 0, -1):
                if li[j] < li[j - 1]:
                    li[j], li[j - 1] = li[j - 1], li[j]
        return li

    # 快速排序
    @staticmethod
    def quick(li):
        if len(li) <= 1:
            return li
        pivot = li[0]
        left = [i for i in li[1:] if i < pivot]
        right = [i for i in li[1:] if i >= pivot]
        return left + [pivot] + right

    # 冒泡排序
    @staticmethod
    def bubble(li):
        for i in range(len(li) - 1):
            for j in range(len(li) - 1 - i):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
        return li

    # 希尔排序
    @staticmethod
    def shell(li):
        gap = len(li) // 2
        while gap > 0:
            for i in range(gap, len(li)):
                j = i
                while j >= gap and li[j] < li[j - gap]:
                    li[j], li[j - gap] = li[j - gap], li[j]
                    j -= gap
            gap //= 2
        return li

    # 计数排序
    @staticmethod
    def count(li):
        max_num = max(li)
        count_list = [0] * (max_num + 1)
        for i in li:
            count_list[i] += 1
        result = []
        for i in range(len(count_list)):
            result += [i] * count_list[i]
        return result

    # 桶排序
    @staticmethod
    def bucket(li):
        max_num = max(li)
        bucket_list = [[] for _ in range(max_num + 1)]
        for i in li:
            bucket_list[i].append(i)
        result = []
        for i in bucket_list:
            result += i
        return result


def get_FileList(path: str) -> list:
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


@lru_cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


@lru_cache
def C(m: int, n: int) -> int:
    """
    组合数
    :return: $C^{m}_{n}$的值
    """
    if m > (n - m):
        m = n - m
    if m == 0:
        return 1
    if m == 1:
        return n
    return C(m - 1, n - 1) + C(m, n - 1)


@lru_cache
def A(m: int, n: int) -> int:
    """排列数"""
    res = 1
    for k in range(m):
        # 排列数公式:
        # A^{m}_{n}
        #   = n! / (n-m)!
        #   = (n-0) * (n-1) * ... * [n-(m-1)]
        res *= n - k
    return res


def str2bool(obj: str) -> bool:
    """
    str to bool

    Args:
        obj: str

    Returns:
        bool

    Raises:
        TypeError: 输入类型不是 str
        ValueError: obj 不是有效的 bool 数据
    """

    if not isinstance(obj, str):
        raise TypeError('输入必须是 str')
    if obj.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif obj.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise ValueError(f"{obj} 不是有效的 bool 数据")


def str2dict(obj: str) -> dict:
    """
    str to dict

    Args:
        obj: str

    Returns:
        dict

    Raises:
        TypeError: 输入类型不是 str
        ValueError: 字符串不是有效的 dict
        OtherException: 字符串不是有效的 python 对象
    """

    if not isinstance(obj, str):
        raise TypeError('输入必须是 str')
    try:
        res = eval(obj)
    except BaseException:
        raise
    else:
        if not isinstance(res, dict):
            raise TypeError(f"{obj} 不是有效的 dict")
        return res


def str2list(obj: str) -> list:
    """
    str to list

    Args:
        obj: str

    Returns:
        list

    Raises:
        TypeError: 输入类型不是 str
        ValueError: 字符串不是有效的 list
        OtherException: 字符串不是有效的 python 对象
    """

    if not isinstance(obj, str):
        raise TypeError('输入必须是 str')
    try:
        res = eval(obj)
    except BaseException:
        raise
    else:
        if not isinstance(res, list):
            raise TypeError(f"{obj} 不是有效的 list")
        return res


class Disable:
    def __init__(self, obj):
        self.obj = obj
        self.disable_obj = True

    def __repr__(self):
        if not self.disable_obj:
            return self.obj
        return Disable.DisableError

    def disable(self):
        self.disable_obj = True

    def enable(self):
        self.disable_obj = False

    class DisableError(Exception):
        pass


def cut(string: str, cut_length: int, *, from_back=False) -> List[str]:
    if from_back:
        return [
                   item[::-1]
                   for item in cut(
                string[::-1], cut_length, from_back=False
            )
               ][::-1]
    return [string[i:i + cut_length] for i in range(0, len(string), cut_length)]


def intToChineseNumber(number: int) -> str:
    number_list = cut(str(number), 4, from_back=True)
    len_number_list = len(number_list)
    big_units = ['', '万', '亿']
    char_map = '零一二三四五六七八九'

    def transform(s):
        units = ['', '十', '百', '千']
        lens = len(s)
        result = ''
        last_is_zero = False

        if s == '0000':
            return char_map[0]

        for index in range(lens):
            char = int(s[index])

            c = char_map[char]
            u = units[lens - index - 1]

            if char != 0:
                result += c + u
                last_is_zero = False
                continue
            if not last_is_zero:
                result += c
                last_is_zero = True

        return result.rstrip('零')

    res = ''

    for index in range(len_number_list):
        item = number_list[index]

        c = transform(item)
        u = big_units[len_number_list - index - 1]

        if c == char_map[0]:
            u = ''
        res += c + u

    return res.rstrip('零')
