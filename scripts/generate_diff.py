import argparse
from file_loader.loader import pair_files_loader

import colorama
from itertools import chain


def gendiff(file1, file2):
  
  dict1, dict2 = pair_files_loader(file1, file2)

  
  def diff(d1, d2, indent_lvl=0):

    union_keys = d1.keys() | d2.keys()
    
    intersection_keys = d1.keys() & d2.keys()
    left = d1.keys() - d2.keys()
    right = d2.keys() - d1.keys()
    
    sorted_union_keys = sorted(union_keys)
    lines = []
  
    def parsed_value(value):  
      if isinstance(value, bool):
        if value == True:
          return 'true'
        else:
          return 'false'
      elif value == None:
        return 'null'
      else:
        return value
        
    def get_line(key):
  
      left_value = parsed_value(d1.get(key))
      right_value = parsed_value(d2.get(key))
      is_dict = isinstance(left_value, dict) and isinstance(right_value, dict)

      ind_deep = 1 + indent_lvl
      ind_default = '  ' * ind_deep
      ind_both = '  '
      
      if is_dict:
        return diff(left_value, right_value, ind_deep)
      else:
        value = left_value if left_value == right_value else ''
        
        ind_left = '- '
        ind_right = '+ '
        
        if key in intersection_keys:
          
          if left_value == right_value:
            return f'{ind_default}{ind_both}{key}: {value}'
          else:
            return f'{ind_default}{ind_left}{key}: {left_value}\n{ind_default}{ind_right}{key}: {right_value}'
        if key in left:
            return f'{ind_default}{ind_left}{key}: {left_value}'
        if key in right:
            return f'{ind_default}{ind_right}{key}: {right_value}'
  
    lines = list(map(get_line, sorted_union_keys))
      
    files_diff =  '\n'.join(chain('{', lines, '}'))
  
    return files_diff

  return diff(dict1, dict2)
  
def main():

  colorama.init()
  print(colorama.Fore.RED)
  parser = argparse.ArgumentParser(description='Compares two   configuration files and whows a difference.')

  parser.add_argument('-f', '--format', help='set format of output')
  parser.add_argument('file_1', metavar='first_file')
  parser.add_argument('file_2', metavar='second_file')

  args = parser.parse_args()

  # result = gendiff(args.file_1, args.file_2)


if __name__ == '__main__':
  main()