from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Compose

from applaudo_nike.processors import take_first, take_first_and_strip, identity, \
                                       match_nike_art_no, match_uniqlo_art_no


class ProductLoader(ItemLoader):
    default_output_processor = take_first
    images_out = identity

    @classmethod
    def delete_url_query_arguments(cls, url):
        return url.rsplit('?', maxsplit=1)[0]

class NikeLoader(ProductLoader):
    images_out = Compose(
        identity,
        lambda urls: [url for url in urls if 'LOADING' not in url]
    )
    art_no_out = Compose(take_first, match_nike_art_no)

class UniqloLoader(ProductLoader):
    images_out = Compose(
        identity,
        lambda urls: [url for url in urls if 'LOADING' not in url]
    )
    art_no_out = Compose(take_first, match_uniqlo_art_no)


