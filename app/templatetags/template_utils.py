from django.template.defaulttags import register


@register.filter
def ref_lis(lis, arg):
    return lis[int(arg)]


@register.filter
def ref_dic(dic, arg):
    if arg not in dic:
        raise KeyError(f'Dictionary doesn\'t have key: {arg}')
    return dic[arg]
