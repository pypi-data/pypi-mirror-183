def get_values_of_key(key2find: str, dictData: dict, notFound=[]):
    """
    获取字典中某个键的全部值
    """
    queue = [dictData]
    result = []
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == key2find:
                result.append(value)
            elif type(value) == dict:
                queue.append(value)
    if not result: result = notFound
    return result
