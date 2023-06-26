import inspect

def tag(name, *contents, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, val) for (attr, val) in attrs.items())
    else:
        attr_str = ''
    if contents:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in contents)
    else:
        return '<%s%s />' % (name, attr_str)

if __name__ == '__main__':
    sign = inspect.signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    bound_var = sign.bind(**my_tag)
    for name, value in bound_var.arguments.items():
        print(name, ' = ', value)

    del my_tag['name']
    bound_var = sign.bind(**my_tag)