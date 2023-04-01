import os, re, inspect


def _get_parser_list(dirname):
    files = [file.replace('.py', '') for file in os.listdir(dirname) if not file.startswith('__')]
    return files


def _import_parsers(files):
    regexp_obj = re.compile('.+parser$', re.IGNORECASE)
    modules = __import__('app.parsers', fromlist=[''])
    parsers = [(x, y) for x,y in inspect.getmembers(modules) if inspect.ismodule(y) and regexp_obj.match(x)]
    classes = dict()
    for x,y in parsers:
        classes.update({x:y for x,y in inspect.getmembers(y) if inspect.isclass(y) and regexp_obj.match(x)})
    return classes


def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)


