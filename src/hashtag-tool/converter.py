"""
Handles text manipulation
"""
# Hashtag converter


def convert(text_input):
    """
    Convert strings into working hashtag strings
    Ex: Str1, St r2,  sTR 3, -> #str1,#str2,#str3
    """
    # Format - Remove space, put into lowercase, and split by comma
    cache = text_input.replace(" ", "").lower().split(",") 
    # Convert
    result = "".join(f'#{txt}' for txt in cache if txt)
    # Return
    return result
    
