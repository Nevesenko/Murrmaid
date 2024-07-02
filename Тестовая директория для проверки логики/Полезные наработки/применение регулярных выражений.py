import re

text = """
\tif(contains({{notion:block_property:title:00000000-0000-0000-0000-000000000000:85184293-3968-4049-95d4-9d187f1cea34}}, \"http\"), style(\"Ссылка\", \"orange\", \"b\") + \"\\n\", \" \")  +
\tif((length({{notion:block_property:title:00000000-0000-0000-0000-000000000000:85184293-3968-4049-95d4-9d187f1cea34}})>30 or test({{notion:block_property:title:00000000-0000-0000-0000-000000000000:85184293-3968-4049-95d4-9d187f1cea34}}, \"\\n\") ) and not(contains({{notion:block_property:title:00000000-0000-0000-0000-000000000000:85184293-3968-4049-95d4-9d187f1cea34}}, \"http\" )), 
\t\tstyle(\"Большой текст\", \"red\", \"b\"), \" \")
"""

# Используем регулярное выражение для поиска текста в кавычках после ключевого слова style
categories = re.findall(r'style\(\"([^"]+)\"', text)

print(categories)