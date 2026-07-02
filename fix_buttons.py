import re
import os

for f in ['Pagina de Vendas Maria.dc.html', 'index.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def repl(m):
        url = m.group(1)
        attrs = m.group(2)
        text = m.group(3)
        return f'<a class="btn-cta" href="{url}" target="_blank"{attrs}>{text}</a>'
        
    new_content = re.sub(r'<button class="btn-cta" onclick="window\.open\(\'([^\']+)\', \'_blank\'\)"([^>]*)>(.*?)</button>', repl, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f'Updated {f}')
