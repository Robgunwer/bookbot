
def word_count(content):
    num_words = len(content.split())
    return f"Found {num_words} total words"

def character_count(content):
    content = content.lower()
    empty_dict = {}
    for char in content:
        if char in empty_dict:
            empty_dict[char] +=1
        else:
            empty_dict[char] =1
    return empty_dict

def sort_dict(arg):
    return arg[1]

def list_of_dicts(content):
    content_list = list(content.items())
    content_list.sort(reverse=True, key=sort_dict)
    content_list = list(filter(alphanum,content_list))
    result =""
    for item in content_list:
        result += f"{item[0]}: {item[1]}"
        if item != content_list[-1]:
            result += "\n"
    return result
            
def alphanum(arg):
    if arg[0].isalpha():
        return True
    return False 
    