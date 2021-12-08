import matplotlib.pyplot as plt
import numpy as np
import re

import sys
import os

from django.conf import settings

from .models import get_plot_path
# from django_plots import settings


def get_arcctg(func_argument: float) -> float: 
    return np.arccos(1 / (1 + func_argument ** 2))

def get_arcth(func_argument: float) -> float:
    return 0.5 * np.log((1 + func_argument) / (func_argument - 1)) if func_argument > 1 or func_argument < -1 else float('inf')

def get_log(base: float, func_argument: float) -> float: 
    return np.log(func_argument) / np.log(base)

def find_closing_bracket(s: str) -> int:
    open_bracket = 0
    close_bracket = 0
    for i in range(len(s)):
        c = s[i]
        if s[i] == '(':
            open_bracket += 1
        elif s[i] == ')':
            close_bracket += 1
        if close_bracket == open_bracket:
            return i
    raise SyntaxError(') missed near log')

def get_plot_function(function_str: str, allowed_func_dict: dict) -> str:
    replace_elements = re.findall(r'[a-zA-Z|\'^\']+', function_str)
    print(replace_elements)
    curr_pos = 0
    for word in replace_elements:
        curr_pos += function_str[curr_pos:].find(word)
        if word not in allowed_func_dict:
            print('word ', word)
            raise ValueError('Misstake in {} or not allowed'.format(word)) 
        
        elif word == 'log':
            base_index = curr_pos + 3
            log_bracket_index = function_str[base_index:].find('(') + base_index
            if log_bracket_index == -1:
                raise SyntaxError('( missed near log')
            
            close_bracket_index = find_closing_bracket(function_str[log_bracket_index:]) + log_bracket_index
            print('function_str[base_index:log_bracket_index]', function_str[base_index:log_bracket_index])
            base = function_str[base_index:log_bracket_index]
            try:
                base = int(base)
            except SyntaxError:
                    print('Wrong log syntax')
            function_str = function_str[:close_bracket_index] + ')' + function_str[close_bracket_index:]
            function_str = function_str[:curr_pos] + \
                function_str[curr_pos:].replace(word + str(base), allowed_func_dict[word] + '(' + str(base) + ',')
            curr_pos += len(allowed_func_dict[word] + '(' + str(base) + ',')
        
        else:
            function_str = function_str[:curr_pos] + function_str[curr_pos:].replace(word, allowed_func_dict[word], 1)
            curr_pos += len(allowed_func_dict[word])
        
    def f(x):
        return eval(function_str)
       
    return f

def draw_plot(plot_instance) -> None:
    start_point = plot_instance.start_point
    interval = plot_instance.interval 
    step = plot_instance.step
    func = get_plot_function(plot_instance.plot_function, allowed_func_dict)
    x_axe = [start_point + i * step for i in range(int((start_point + interval) // step))]

    y_axe = list(map(func, x_axe))
    fig, ax = plt.subplots()
    ax.plot(x_axe, y_axe)
    os.mkdir(settings.MEDIA_ROOT+'/plots/'+str(plot_instance.id))
    plt.savefig(settings.MEDIA_ROOT+get_plot_path(plot_instance))
    return

allowed_func_dict = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'tg': 'np.tan',
    'ctg': '1/np.tan', 
    'arcsin': 'np.arcsin',
    'arccos': 'np.arccos',
    'arctg': 'np.arctan',
    'arcctg': 'get_arcctg',
    'sh': 'np.sinh',
    'ch': 'np.cosh',
    'th': 'np.tanh',
    'cth': '1 / np.tanh',
    'arsh': 'np.arcsinh',
    'arch': 'np.arccosh',
    'arth': 'np.arctanh',
    'arcth': 'get_arcth',
    'exp': 'np.exp',
    'ln': 'np.log',
    'lg': 'np.log10',
    'log': 'get_log',
    'abs': 'np.abs', 
    '^': '**',
    'x': 'x',
    'x^': 'x ** ',
}

if __name__ == '__main__':
    f = 'cos(cos(cos(cos(x*x*x*x*x*x*x*x*x*x*x*x*x))))*3/x*x*x'
    f2 = get_plot_function(f, allowed_func_dict)
    print(f2)
    x = 1
    print(f2, ' = ', f2(x))
    print(sys.path)
    settings.configure()
    print(settings.MEDIA_ROOT)
