from typing import List

def parse_to_list(simple_list_data: str,separator='\n') -> List[str]:
    return simple_list_data.split(separator)
def convert_list_to_simple_list_data(list_input: List[str],separator='\n') -> str:
    sanitized_list = [str(element) for element in list_input]
    #sanitized_list = __sanitize_list(list_input,separator)       
    list_of_parsed_simple_lists = [parse_to_list(data,separator) for data in sanitized_list]
    flat_list = [element for sublist in list_of_parsed_simple_lists for element in sublist]
    return separator.join(flat_list)
def __sanitize_list(list_input: List[str],separator='\n') -> List[str]:
    sanitized_list = []
    for element in list_input:
        element = str(element)
        if element.startswith(separator): #element[0:len(separator)-1] == separator:
            element = element[len(separator)::]
        if element.endswith(separator): #element[(len(element)-1)-(len(separator)-1):len(element)] == separator:
            element = element[0:(len(element)-1)-(len(separator)-1)]
        sanitized_list.append(element)
    return sanitized_list
