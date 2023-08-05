import json

class TemplateRenderingError(Exception):
    def __init__(self, msg, template_str, params):
        msg = 'Template rendering error:\n{0}\n\nParameters:\n{1}\n\nTemplate:\n{2}'.format(
            msg, json.dumps(params, indent=2), template_str)
        #msg = 'Template error:\n{0} in:\n{1}'.format(msg, template_str)
        super().__init__(msg)
