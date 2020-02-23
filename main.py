#!/usr/bin/env python3
import os
import io
import zipfile
import requests
import json


MICROPYTHON_ZIP_URL = 'https://github.com/micropython/micropython/archive/master.zip'
OUTPUT_PATH = 'api_stubs'

def download_zip_mp_master():
    response = requests.get(MICROPYTHON_ZIP_URL)
    if response.status_code != 200:
        print(response.reason)
        raise Warning('Download of micropython failed.')
    return response.content

def get_raw_documentation():
    documentations = []
    mp_repo_zip = zipfile.ZipFile(io.BytesIO(download_zip_mp_master()))
    for zfile in mp_repo_zip.filelist:
        if '/docs/library' in os.path.dirname(zfile.filename) and os.path.splitext(zfile.filename)[1] == '.rst':
            name, ext = os.path.splitext(os.path.basename(zfile.filename))
            with mp_repo_zip.open(zfile.filename) as current_file:
                documentations.append(current_file.read().decode('utf-8'))
    return documentations

def extract_next_doc(lines, index):
    started = False
    doc = ''
    for i in range(index, len(lines)):
        if started and len(lines[i]) > 0:
            if lines[i].startswith('   '):
                lines[i] = lines[i][3:]
            doc += lines[i] + '\n'
        if started and i+1 < len(lines) and lines[i+1].startswith('.') or i+1 < len(lines) and lines[i+1].startswith('-') and started:
            if lines[i+1].startswith('-'):
                doc = '\n'.join(doc.split('\n')[0:-2])
            return doc
        if len(lines[i]) == 0 and not started:
            started = True
    return doc

def extract_modules(documentations):
    modules = {}
    current_module = ''
    for doc in documentations:
        lines = doc.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('.. module:: '):
                name = line.split(':: ')[1]
                current_module = name
                modules[name] = {
                    'doc': extract_next_doc(lines, i),
                    'constants': {},
                    'classes': {},
                    'functions': {}
                }
            if line.startswith('.. function:: '):
                name = line.split(':: ')[1]
                modules[current_module]['functions'][name]={
                    'doc': extract_next_doc(lines, i)
                }
            if line.startswith('.. _' + current_module + '_constants:'):
                modules[current_module]['constants']['doc'] = extract_next_doc(lines, i+4)
    return modules

def enrich_classes(documentations, modules):
    current_module = ''
    current_class = ''
    for doc in documentations:
        lines = doc.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('.. currentmodule:: '):
                current_module = line.split(':: ')[1]
            if line.startswith('.. module:: '):
                current_module = line.split(':: ')[1]
            if line.startswith('class '):
                if len(lines[i+1]) == len(line):
                    name = line.split(' ')[1]
                    current_class = name
                    modules[current_module]['classes'][name] = {
                        'doc': extract_next_doc(lines, i),
                        'constructor': {},
                        'methods': [],
                        'constants': {}
                    }
            if line.startswith('.. class:: ' + current_class) and len(current_class)>0:
                args = '(' + line.split('(')[1]
                
                modules[current_module]['classes'][current_class]['constructor'] = {
                    'args': args,
                    'doc': extract_next_doc(lines, i)
                }
            if line.startswith('.. method:: ' + current_class + '.') and len(current_class)>0:
                method = line.split(current_class + '.')[1]
                modules[current_module]['classes'][current_class]['methods'].append({
                    'args': method,
                    'doc': extract_next_doc(lines, i)
                })

    return modules

def extract_structure(documentations):
    modules = extract_modules(documentations)
    modules = enrich_classes(documentations, modules)
    return modules

def indent_content(content, count=4, indent_char=' '):
    indented = ''
    for line in content.split('\n'):
        if len(line) == 0:
            continue
        indented += indent_char*count + line + '\n'
    return indented

def generate_module(structure):
    content =  '"""\n' + structure['doc'] + '\n"""\n\n'
    for func in structure['functions']:
        content += 'def ' + func.replace(', /', '') + ':\n'
        if len(structure['functions'][func]['doc']) > 0:
            content += '    """\n' + indent_content(structure['functions'][func]['doc']) + '    """\n'
        content += '    pass\n\n'
    
    for classname in structure['classes']:
        content += '\nclass ' + classname + ':\n'
        if len(structure['classes'][classname]['doc']) > 0:
            content += '    """\n' + indent_content(structure['classes'][classname]['doc']) + '    """\n'
        content += '\n'

        if 'args' in structure['classes'][classname]['constructor']:
            args = structure['classes'][classname]['constructor']['args'][1:]
            args = args.replace(', \\*', '').replace(', /', '')
            content += '    def __init__(self, ' + args + ':\n'
            content += '        """\n'
            content += indent_content(structure['classes'][classname]['constructor']['doc'], 8)
            content += '        """\n         pass\n\n'
        
        for method in structure['classes'][classname]['methods']:
            args = method['args'].replace(', \\*', '').replace(', /', '').replace('(', '(self, ')
            content += '    def ' + args + '\n'
            content += '        """\n'
            content += indent_content(method['doc'], 8)
            content += '        """\n         pass\n\n'
    return content



if __name__ == '__main__':
    work_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), OUTPUT_PATH)

    if os.path.isdir(work_path):
        import shutil
        shutil.rmtree(work_path)

    os.mkdir(work_path)

    structure = extract_structure(get_raw_documentation())
    for module in structure:
        file_path = os.path.join(OUTPUT_PATH, module + '.py')
        with open(file_path, 'w') as f:
            f.write(generate_module(structure[module]))

