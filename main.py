import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML resume data
with open('data/resume.yaml', 'r', encoding='utf-8') as file:
    resume_data = yaml.safe_load(file)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('resume_template.html')

# Render template with YAML data
rendered_html = template.render(resume_data)

# Write the output to an HTML file
with open('output/index.html', 'w', encoding='utf-8') as file:
    file.write(rendered_html)

print("Resume rendered to output/index.html")
