from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('./templates/'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('receipt.html')

print(
    template.render({
        "name": "John",
        "test": 1
    })
)
