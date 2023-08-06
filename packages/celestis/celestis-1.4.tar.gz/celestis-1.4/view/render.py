def contextualize(html, variables):
    # Fix with a templating engine

    return html

def render_template(file_path, **context):
    with open(file_path) as f:
        template = f.read()

    template = contextualize(template, context)

    return template
    # Templating using Jinja and context.items()
        