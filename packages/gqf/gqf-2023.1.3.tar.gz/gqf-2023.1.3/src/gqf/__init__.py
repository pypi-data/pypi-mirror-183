"""
函数一览表
beautify.py ['separator']
crypto.py ['asciis2char', 'b64decode', 'MD5', 'MD5_16']
dict.py ['get_values_of_key']
file.py ['get_files', 'extract_aes', 'get_py_func_name']
HTTP.py ['set_proxy', 'get_img_src', 'download_file', 'download_file_streamed', 'download_file_concurrently', 'github_releases_latest_version'
]
mouse.py ['scroll', 'echo_mouse_pos']
process.py ['proc_exist']
str.py ['up_n_low', 'random_string']

"""

if __name__ == '__main__':
    from qf.file import get_py_func_name
    get_py_func_name()
