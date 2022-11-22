import re

from itemloaders.processors import TakeFirst, Identity, Compose


take_first = TakeFirst()
identity = Identity()
take_first_and_strip = Compose(take_first, lambda x: x.strip())

def match_nike_art_no(text):
    return re.search(r'.{6}-.{3}', text).group()

def match_uniqlo_art_no(text):
    return re.search(r'.{6}-.{3}', text).group()
