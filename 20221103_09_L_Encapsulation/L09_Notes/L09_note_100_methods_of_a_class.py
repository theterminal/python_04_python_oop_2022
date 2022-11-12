# from https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has

import pandas as pd


print('\n_________ ex. 1 __________\n')


df = pd.DataFrame([[10, 20, 30], [100, 200, 300]], columns=['foo', 'bar', 'baz'])


def get_methods(object, spacing=50):
    method_list = []

    for method_name in dir(object):
        try:
            if callable(getattr(object, method_name)):
                method_list.append(str(method_name))
        except Exception:
            method_list.append(str(method_name))

    process_func = (lambda s: ' '.join(s.split())) or (lambda s: s)

    for method in method_list:
        try:
            print(str(method.ljust(spacing)) + ' ' + process_func(str(getattr(object, method).__doc__)[0:150]))
        except Exception:
            print(method.ljust(spacing) + ' ' + ' getattr() failed')


get_methods(df['foo'])


print('\n_________ ex. 2 __________\n')


object_methods = '\n'.join([method_name for method_name in dir(object) if callable(getattr(object, method_name))])
print(object_methods)


print('\n_________ ex. 3 __________\n')


object_methods = '\n'.join([method_name for method_name in dir(object)])
print(object_methods)
