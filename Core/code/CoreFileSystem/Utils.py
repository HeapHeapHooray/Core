from typing import Union

def get_extension_from_name(name: str) -> Union[None,str]:
    if '.' not in name or name.endswith('.'):
        return None
    return name.split('.')[-1]
