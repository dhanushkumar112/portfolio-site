from jinja2 import Environment, FileSystemLoader

# Load the templates folder
env = Environment(loader=FileSystemLoader('templates'))

# Load the base.html template
template = env.get_template('base.html')

# Portfolio data
portfolio_data = {
    'title': 'Dhanush Kumar Reddy Portfolio',
    'name': 'Dhanush Kumar Reddy Yarragonda',
    'about': 'Aspiring Software Developer skilled in Python, SQL, and building practical solutions.',
    'email': 'your.email@example.com',
    'skills': ['Python', 'SQL', 'HTML', 'CSS', 'Git'],
    'projects': [
        {
            'name': 'Emotion Recognition',
            'link': 'https://github.com/your-username/emotion-recognition',
            'description': 'A deep learning model to detect facial expressions using CNN.'
        },
        {
            'name': 'Another Project',
            'link': 'https://github.com/your-username/another-project',
            'description': 'Description of your second project.'
        }
    ]
}

# Render the HTML with your data
output = template.render(portfolio_data)

# Save the final HTML as index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("✅ Portfolio generated successfully!")
