def exclude_title_fields(df, titlename):
    '''извелкает Id и категорию имени'''
    cur = df
    cur = cur[['id', titlename]]
    cur[titlename] = cur[titlename].apply(lambda x: x[0]['text']['content'])
    res = cur
    return res

def exclude_category_field(df, cats):
    cur = df
    cur = cur[cats]
    for cat in cats:
        print(cat)
        if cat.find('relation'):
            cur[cat] = cur[cat].map(lambda x : x[0]['id'])
    res = cur
    return res
