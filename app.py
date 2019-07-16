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
 "date": "8:30 AM Wednesday, July 17 2017",
 "purpose": "",
 "location": "3617 Tully Street, Livonia, MI",
 "attendees_list": ["John Doe","Jane Doe"]
})

with open('my_new_html_file.html', 'w') as f:
    f.write(output)
