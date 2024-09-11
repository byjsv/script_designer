import os

from action import ASCII_Turn


# 判断字符串是否只有数字
def only_num(str_num):
    return all(char.isdigit() for char in str_num)


# 判断是否符合长度
def if_length(stl, length):
    return len(stl) < length


# 判断是否为ASCII的关键字
def if_ASCII(stl):
    return stl in ASCII_Turn.key_map


def is_valid_path(path_str):
    """检查字符串是否符合有效的路径格式"""
    # 检查路径是否为有效的绝对路径、相对路径或文件名
    try:
        # 尝试标准化路径
        norm_path = os.path.normpath(path_str)
        return os.path.isabs(norm_path) or bool(norm_path.strip())
    except (TypeError, ValueError):
        return False


def is_accessible_path(path_str):
    """检查路径是否存在并且可以被访问（读写）"""
    try:
        with open(path_str, 'r') as file:
            pass

    except FileNotFoundError:
        return False
    except IOError:
        return False
    except Exception as e:
        return False
    return True


