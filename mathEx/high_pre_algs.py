class HighPrecisionAlgorithms:
    """
    高精度算法
    """

    def __init__(self):
        self.add = self.addition = self.Addition()
        self.sub = self.subtract = self.subtraction = self.Subtraction()
        self.mul = self.multiply = self.multiplication = self.Multiplication()

    class Addition:
        def int(self, a: int, b: int) -> int:
            """
            高精度加法(整数)
            """
            if not (type(a) == type(b) == int):
                raise TypeError("输入必须为整数 Input must be an integer.")

            # 将输入的数字转化为列表
            # 倒序是为了方便计算
            num1 = [int(x) for x in str(a)[::-1]]
            num2 = [int(x) for x in str(b)[::-1]]

            # 设置一个 res 列表，位数为两数最长位数 +1
            # 全部预设为 0
            res = [0] * (max(len(num1), len(num2)) + 1)
            # 补全两数位数
            num1 += [0] * (len(res) - len(num1))
            num2 += [0] * (len(res) - len(num2))

            # 进行进位计算
            for index in range(len(res)):
                res[index] = num1[index] + num2[index]
                if res[index] > 9:  # 进位
                    res[index] -= 10
                    res[index + 1] += 1

            # 数字不能直接拼起来，先转化为字符串
            res_str = [str(x) for x in res]
            # 使用 int() 转换时前面多余的 0 会自动去除
            res_int = int("".join(res_str[::-1]))

            return res_int

        def float(self, a: float, b: float) -> float:
            """
            高精度计算(小数/浮点数)
            """
            if not (type(a) == type(b) == float):
                raise TypeError("输入必须为小数 Input must be a float.")

            # 将小数从小数点 (.) 拆分
            # float 类型不能直接拆，先转化为 str
            a_list = str(a).split(".")
            b_list = str(b).split(".")
            a_int, a_dec = [int(x) for x in a_list]
            b_int, b_dec = [int(x) for x in b_list]

            # 整数部分相加，直接调用高精度加法
            res_int = self.int(a_int, b_int)

            # 小数部分是要对齐小数点计算
            # 计算最长的位数
            max_len = max(len(str(a_dec)), len(str(b_dec)))
            # 补全，位数不够的补 0
            a_dec = int(str(a_dec) + '0' * (max_len - len(str(a_dec))))
            b_dec = int(str(b_dec) + '0' * (max_len - len(str(b_dec))))
            # 计算
            res_dec = self.int(a_dec, b_dec)
            # 注意小数的进位，最高的会进到整数部分
            if res_dec > 10 ** max_len - 1:
                res_dec -= 10 ** max_len
                res_int += 1

            # 拼起来，返回答案
            res = f"{res_int}.{res_dec}"
            return float(res)

        def __call__(self, a: int|float, b: int|float) -> int|float:
            '''
            """
            高精度加法——自动匹配算法
            允许输入两个数字(不分整数小数)
            """
            if type(a) == type(b) == int:
                return self.int(a, b)
            if int(a) == a and int(b) == b:
                return self.int(int(a), int(b))
            return self.float(float(a), float(b))

    class Subtraction:
        def int(self, a: int, b: int) -> int:
            """
            高精度减法(整数)
            """
            if not (type(a) == type(b) == int):
                raise TypeError("输入必须为整数 Input must be an integer.")

            # 将被减数与减数转换成列表并反转
            a_list = [int(x) for x in str(a)[::-1]]
            b_list = [int(x) for x in str(b)[::-1]]

            # 定义 res 列表，位数为两数最长位数
            res = [0] * max(len(a_list), len(b_list))
            # 将位数补齐
            a_list += [0] * (len(res) - len(a_list))
            b_list += [0] * (len(res) - len(b_list))

            # 使用 for 循环遍历计算
            for index in range(len(res)):
                # 退位计算
                if a_list[index] < b_list[index]:
                    a_list[index + 1] -= 1
                    a_list[index] += 10
                # 被减数减减数
                res[index] = a_list[index] - b_list[index]

            # 计算完成，转化为 int 时 python 会自动去除前面的 0
            res_int = int("".join([str(x) for x in res[::-1]]))
            return res_int

        def float(self, a: float, b: float) -> float:
            """
            高精度减法(小数/浮点数)
            """
            if not (type(a) == type(b) == float):
                raise TypeError("输入必须为小数 Input must be a float.")

            # 将小数从小数点拆分
            a_list = str(a).split(".")
            b_list = str(b).split(".")
            a_int, a_dec = [int(x) for x in a_list]
            b_int, b_dec = [int(x) for x in b_list]

            # 整数部分的计算直接调用
            res_int = self.int(a_int, b_int)

            # 小数部分的计算要注意个位的退位
            # 个位退位会到十分位
            if a_dec < b_dec:
                res_int -= 1
                a_dec = int('1' + str(a_dec))
            res_dec = self.int(a_dec, b_dec)

            # 将结果拼起来
            # int 类型不能直接拼，要转化为 str
            res = float(f"{res_int}.{res_dec}")
            return res

        def __call__(self, a: int|float, b: int|float) -> int|float:
            '''
            """
            高精度减法——自动匹配算法
            允许输入两个数字(不分整数小数)
            """
            if type(a) == type(b) == int:
                return self.int(a, b)
            if int(a) == a and int(b) == b:
                return self.int(int(a), int(b))
            return self.float(float(a), float(b))

    class Multiplication:
        def int(self, a: int, b: int) -> int:
            """
            高精度乘法(整数)
            """
            if not (type(a) == type(b) == int):
                raise TypeError("输入必须为整数 Input must be an integer.")

            # 确定符号
            a_str, b_str = str(a), str(b)
            sym = 1
            if a_str[0] == '-':
                sym *= -1
                a_str = a_str[1:]
            if b_str[0] == '-':
                sym *= -1
                b_str = b_str[1:]

            # 将数字拆分成列表并反转
            a_list = [int(x) for x in a_str[::-1]]
            b_list = [int(x) for x in b_str[::-1]]
            a_len, b_len = len(a_list), len(b_list)

            # 初始化结果列表，使用 0 填充
            res_list = [0] * (a_len + b_len)

            # 逐位相乘
            for i in range(a_len):
                for j in range(b_len):
                    res_list[i + j] += a_list[i] * b_list[j]

            # 处理进位
            for i in range(len(res_list)):
                if res_list[i] > 9:
                    res_list[i + 1] += res_list[i] // 10
                    res_list[i] %= 10

            # 转化成 int
            res = int(''.join([str(x) for x in res_list[::-1]]))
            return sym * res

        def float(self, a: float, b: float) -> float:
            """高精度乘法(小数)"""
            if not (type(a) == type(b) == float):
                raise TypeError("输入必须为小数 Input must be a float.")

            # 确定符号
            a_str, b_str = str(a), str(b)
            sym = 1
            if a_str[0] == '-':
                sym *= -1
                a_str = a_str[1:]
            if b_str[0] == '-':
                sym *= -1
                b_str = b_str[1:]

            # 将小数从小数点拆分
            a_int, a_dec = str(a).split(".")
            b_int, b_dec = str(b).split(".")
            a_int, a_dec = a_str.split(".")
            b_int, b_dec = b_str.split(".")

            # 小数乘法的重点是结果小数位数
            # 小数位数 = 乘数小数位数和
            res_dec_len = len(a_dec) + len(b_dec)

            # 小数乘法计算
            # 直接把整数部分，小数部分拼起来
            # 然后带入 self.int() 计算
            res = self.int(
                int(a_int + a_dec),
                int(b_int + b_dec)
            )

            res = str(res)
            # 确定小数点的位置
            res = \
                res[:-res_dec_len] + "." + \
                res[-res_dec_len:]

            return sym * float(res)

        def __call__(self, a: int|float, b: int|float) -> int|float:
            '''
            """
            高精度乘法——自动匹配算法
            允许输入两个数字(不分整数小数)
            """
            if type(a) == type(b) == int:
                return self.int(a, b)
            if int(a) == a and int(b) == b:
                return self.int(int(a), int(b))
            return self.float(float(a), float(b))

    def divide_int(self, a: int, b: int) -> int:
        """高精度除法(整数)"""
        if not (type(a) == type(b) == int):
            raise TypeError("输入必须为整数 Input must be an integer.")

        from .exceptions import DisableError
        raise DisableError('未写好的方法')
