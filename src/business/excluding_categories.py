def exclude_fields(df, titlename):
    '''извелкает Id и категорию имени'''
    cur = df
    cur = cur[['id', titlename]]
    cur[titlename] = cur[titlename].apply(lambda x: x[0]['text']['content'])
    return df