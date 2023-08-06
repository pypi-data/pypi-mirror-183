import os
import sys
sys.path.append(os.getcwd())

import json
from simple_i18n import I18n

i18n = I18n({
    'locales': ['en', 'ru', 'zh', 'fr', 'cz', 'ge', 'it', 'ko', 'jp', 'es', 'de', 'tr', 'hu', 'pl', 'sk', 'pt', 'sv', 'nl'],
    'fallbacks': {'zh': 'en'},
    'defaultLocale': 'en',
    'retryInDefaultLocale': True,
    'cookie': 'yourcookiename',
    'header': 'accept-language',
    'queryParameter': 'lang',
    'directory': 'test/locales/',
    'directoryPermissions': '755',
    'autoReload': True,
    'updateFiles': False,
    'syncFiles': False,
    'indent': '\t',
    'extension': '.json',
    'prefix': '',
    'objectNotation': False,
    'logDebugFn': lambda msg: print(msg),
    'logWarnFn': lambda msg: print(msg),
    'logErrorFn': lambda msg: print(msg),
    'missingKeyFn': lambda locale, value: value,
    'register': globals(),
    'api': {},
    'preserveLegacyCase': True,
    'staticCatalog': {},
    'mustacheConfig': {
        'tags': ['{{', '}}'],
        'disable': False
    },
    'parser': json
})

# try using locale 'sk', however this locale is unavailable and will fallback to 'de'
i18n.setLocale('sk')

# using i18n singleton (i18n.locale == 'de')
i18n.__('Hello') # -> Hallo
i18n.__('Hello %s', 'Marcus') # -> Hallo Marcus
i18n.__('Hello {{name}}', { 'name': 'Marcus' }) # -> Hallo Marcus

# using api bound to globals (locale == 'de')
__('Hello') # -> Hallo
__('Hello %s', 'Marcus') # -> Hallo Marcus
__('Hello {{name}}', { 'name': 'Marcus' }) # -> Hallo Marcus

# passing specific locale
i18n.__({ 'phrase': 'Hello', 'locale': 'fr' }) # -> Salut
i18n.__({ 'phrase': 'Hello %s', 'locale': 'fr' }, 'Marcus') # -> Salut Marcus
i18n.__({ 'phrase': 'Hello {{name}}', 'locale': 'fr' }, { 'name': 'Marcus' }) # -> Salut Marcus

i18n.setLocale('sk')
print(i18n.__('ragfair-missing_barter_scheme', {'name': 'TESTNAME', 'itemId': 'TESTITEMID', 'tpl': 'TESTTPL'}))
print(i18n.__('bot-weapon_missing_mod_slot', {'modSlot': 'TESTMODSLOT', 'weaponId': 'TESTWEAPONID', 'weaponName': 'TESTWEAPONNAME'}))
print(i18n.__('bot-missing_weapon_preset', 'abda873294efc803bfa9cbea4323'))
print(i18n.__('assort-missing_loyalty_level_object', {'traderId': 'Fence'}))



'''
import shutil
from itertools import chain

directory = 'test/locales/'
backupdir = 'test/locales-bak/'

for file in os.listdir(directory):
    os.remove(os.path.join(directory, file))

while not list(filter(lambda name: '123456' in name, chain(os.listdir(directory), os.listdir(backupdir)))):
    for file in os.listdir(directory):
        while True:
            try:
                os.remove(os.path.join(directory, file))
                break
            except:
                pass
    for file in os.listdir(backupdir):
        while True:
            try:
                shutil.copyfile(os.path.join(backupdir, file), os.path.join(directory, file))
                break
            except:
                pass
'''