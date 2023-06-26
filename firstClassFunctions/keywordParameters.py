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
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', cls='sidebar'))
    print(tag(contents='testing', name='img'))
    print(tag(attrs='testing', name='img', cls="imagine"))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))