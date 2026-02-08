from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
from pathlib import Path
import os

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")

    with open(from_path) as f:
        md = f.read()
    
    with open(template_path) as t:
        template = t.read()

    htmlnode = markdown_to_html_node(md)
    html = htmlnode.to_html()

    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
