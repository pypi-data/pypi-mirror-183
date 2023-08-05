import json
import re
from jinja2 import Template, DebugUndefined

from keyrock_core import json_util

from . import exc

import logging
logger = logging.getLogger(__name__)


def finalize(val):
    if val is None:
        return 'NULL'
    elif isinstance(val, dict) or isinstance(val, list):
        return json.dumps(val, cls=json_util.CustomEncoder)
    else:
        return val


def render(template_str, params):
    t = Template(template_str, trim_blocks=True, undefined=DebugUndefined, finalize=finalize)
    try:
        if isinstance(params, dict):
            return t.render(params)
        else:
            return template_str
    except Exception as e:
        raise exc.TemplateRenderingError(str(e), template_str, params)


def flatten_params(params, max_depth=3):
    # For consistent depth, even though it's possible to nest deeper in fewer iterations in-place
    flat_params = params.copy()
    for i in range(max_depth):
        changed = False
        for key, old_val in flat_params.items():
            try:
                # The problem with Mustache/chevron is that it removes rather than ignores missing keys
                #new_val = chevron.render(old_val, params)
                if isinstance(old_val, str):
                    new_val = sub_dict(old_val, params)
                    #new_val = render(old_val, params)
                else:
                    new_val = old_val

                if new_val != old_val:
                    changed = True
                    flat_params[key] = new_val
            except Exception as e:
                flat_params[key] = str(e)

        if not changed:
            return flat_params

    # Hit max depth
    return flat_params


def escape_str(str_val):
    return re.sub(r'[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]', '\\$&', str(str_val))


def sub_dict(str_val, params, sub_wrap=False):
    if not str_val:
        return ''

    if not params:
        return str_val

    str_val = str(str_val)

    if isinstance(params, list):
        # Convert params list to dict
        params = {str(i): params[i] for i in range(0, len(params))}

    for key, val in params.items():
        clean_key = escape_str(key)
        tag_str = '\{\{' + escape_str(key) + '\}\}'
        sub_val = escape_str(val)
        if sub_wrap:
            sub_val = '{{' + sub_val + '}}'
        str_val = re.sub(tag_str, sub_val, str_val)

    return str_val


def compile_row_template(template_str, col_list):
    template_str = str(template_str)

    # Convert column names to indexes
    #  e.g. {{col_name}} --> {{r[0]}}
    #  or {{col_name.something}}  or {{r[0].something}}
    for c, col_name in enumerate(col_list):
        re_str = '\{\{\s*' + col_name + '([\}\s\}|.]?)'
        regex = re.compile(re_str, re.DOTALL)

        def row_hack_fn(match):
            return '{{row[' + str(c) + ']' + match.group(1)
        template_str = regex.sub(row_hack_fn, template_str)

    # Convert raw column indices to reference the row element
    #  e.g. {{0}} --> {{row[0]}}
    #  or {{0.x}} --> {{row[0].x}}
    regex = re.compile('\{\{\s*(\d+)', re.DOTALL)
    template_str = regex.sub(_index_replace_hack, template_str)

    return Template(template_str, trim_blocks=True, undefined=DebugUndefined, finalize=finalize)

def _index_replace_hack(match):
    return '{{row[' + match.group(1) +']'

def render_row_template(template, row, final_params=None, empty_as_null=True):
    sub_dict = {
        'row': row,
    }
    if final_params:
        sub_dict.update(final_params)

    # Include parameter values, along with the base row value-array
    try:
        rv = template.render(sub_dict)
        if empty_as_null and rv == '':
            return None
        return rv
    except Exception as e:
        raise exc.TemplateRenderingError(str(e), template_str, params)
