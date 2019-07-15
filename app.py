from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('./templates/'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('receipt.html')

output = template.render({
 "category": "Meals",
 "date": "June 23,2019",
 "merchant": "Momofuko Ko",
 "total": 560.75,
 "purpose": "",
 "attendees": "<missing data>",
 "attendees_list": ["atendee 1","atendee 2", "atendee 3"]
})

with open('my_new_html_file.html', 'w') as f:
    f.write(output)
