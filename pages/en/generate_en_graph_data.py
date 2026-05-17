import os
import json
import re

# We can import the PAGES list from the existing script
# or just parse it if we want to be safe. 
# Here I will parse it to avoid execution environment issues.

concepts_file = 'f:/26年4月/kb01/pages/en/concepts/generate_en_concepts.py'

def extract_nodes_and_links():
    with open(concepts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find the PAGES list
    # This is a bit brittle but faster than full parsing
    pages_match = re.search(r'PAGES = \[(.*?)\]', content, re.DOTALL)
    if not pages_match:
        return None, None
    
    pages_text = pages_match.group(1)
    
    # Extract each dict
    entries = re.findall(r'\{.*?"slug": "(.*?)",.*?"title": "(.*?)",.*?"emoji": "(.*?)",.*?"subtitle": "(.*?)",.*?"tags": \'(.*?)\'', pages_text, re.DOTALL)
    
    nodes = []
    links = []
    
    # Add a central node if not present
    nodes.append({ "id": "ramana", "name": "🙏 Ramana", "type": "center", "url": "persons/index.html", "desc": "Sri Ramana Maharshi (1879–1950)" })
    
    for slug, title, emoji, subtitle, tags_html in entries:
        # Node
        nodes.append({
            "id": slug,
            "name": f"{emoji} {title}",
            "type": "atman", # default type
            "url": f"concepts/{slug}.html",
            "desc": subtitle
        })
        
        # Links based on tags
        # Extract href from tags like <a href="brahman.html">
        targets = re.findall(r'href="(.*?)\.html"', tags_html)
        for target in targets:
            links.append({ "source": slug, "target": target })
            
        # Also link most to Ramana
        links.append({ "source": "ramana", "target": slug })

    return nodes, links

nodes, links = extract_nodes_and_links()
print(json.dumps({ "nodes": nodes, "links": links }, indent=2))
