import enum

class BeerType(enum.Enum):
    BELGIAN_STRONG_GOLDEN_ALE = 'Belgian Strong Golden Ale'
    CALIFORNIA_COMMON = 'California Common'
    ENGLISH_BITTER = 'English Bitter'
    HEFEWEIZEN = 'Hefeweizen'
    IPA_ENGLISH = 'IPA - English'
    IPA_AMERICAN = 'IPA - American'
    LAGER_AMERICAN_LIGHT = 'Lager - American Light'
    LAGER_EURO = 'Lager - Euro'
    LAGER_NA_ADJUNCT = 'Lager - North American Adjunct'
    LAGER_PALE = 'Lager - Pale'
    LAGER_VIENNA = 'Lager - Vienna'
    LAGER_WINTER = 'Lager - Winter'
    MARZEN = 'Märzen'
    PALE_ALE_AMERICAN = 'Pale Ale - American'
    PALE_WHEAT_ALE_AMERICAN = 'Pale Wheat Ale - American'
    PILSNER_GERMAN = 'Pilsner - German'
    PORTER_AMERICAN = 'Porter - American'
    ROOT_BEER = 'Root Beer'
    SHANDY_RADLER = 'Shandy / Radler'
    STOUT_AMERICAN_IMPERIAL_DOUBLE = 'Stout - American Imperial / Double'
    WITBIER = 'Witbier'   

class SocialMediaType(enum.Enum):
    FACEBOOK = 'Facebook'
    TWITTER = 'Twitter'
    INSTAGRAM = 'Instagram'
    GOOGLE = 'Google'
    
class BreweryType(enum.Enum):
    MACRO = 'Macro Brewery'
    MICRO = 'Micro Brewery'
    REGIONAL = 'Regional Brewery'
    HOME = 'Home Brewery'
    BREW_PUB = 'Brew Pub'

class ServingType(enum.Enum):
    BOTTLE = 'Bottle'
    DRAFT = 'Draft'
    TASTER = 'Taster'
    CAN = 'Can'