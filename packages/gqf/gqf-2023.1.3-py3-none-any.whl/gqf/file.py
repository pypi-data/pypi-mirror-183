import pathlib
from qf.time import timeit
from re import findall

from loguru import logger
from pyzipper import AESZipFile


@timeit
def get_files(path: str, ext=''):
    """
    递归获取路径所有文件
    支持过滤后缀
    """
    pattern = '*.*' if ext == '' else f'*.{ext}'
    # rglob 相当于在 pattern 前加上了 “**/”，启用了递归
    l = list(pathlib.Path(path).rglob(pattern))
    logger.info(f'获取文件完成，共 {len(l)} 个')
    return l


def extract_aes(zip_file: str, password: str):
    with AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as f:
        f.setpassword(password.encode('utf-8'))
        try:
            f.extractall()  # 使用密码尝试解压
            logger.info("找到密码：" + password)
        except:
            pass  # 解压失败说明密码错误，跳过


def get_py_func_name():
    """
    获取 py 文件中的函数名

    示例输出
    beautify.py ['separator']
    crypto.py ['asciis2char', 'b64decode', 'MD5', 'MD5_16']
    dict.py ['get_values_of_key']
    file.py ['get_files', 'extract_aes', 'get_func_name']
    HTTP.py ['set_proxy', 'get_img_src', 'download', 'github_releases_latest_version']
    mouse.py ['scroll', 'echo_mouse_pos']
    process.py ['proc_exist']
    str.py ['up_n_low', 'random_string']
    """
    pys = get_files('D:\portable-soft\py3\Lib\qf', 'py')
    # 剔除 __init__.py
    del pys[-1]
    for py in pys:
        with open(py, 'r', encoding='utf-8') as f:
            func_names = findall('(?<=def ).*(?=\()', f.read())
            # 过滤匹配到的正则表达式本身
            r = ").*(?=\\()', f.read"
            if r in func_names: func_names.remove(r)
            # py 是 WindowsPath，str 后得到路径字符串
            print(str(py).split('\\')[-1], func_names)


if __name__ == '__main__':
    get_py_func_name()
