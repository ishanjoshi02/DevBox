from os import system, chdir
from sys import argv
from settings import (ROOT_DEV_FOLDER, codebases)
from constants import EDITORS



def main():
    requested_codebase = argv[1]
    for codebase in codebases.values():
            if requested_codebase in codebase['valid_commands']:
                working_dir = ROOT_DEV_FOLDER + "/" + codebase['folder']
                try:
                    if argv[2] == 'edit':
                        try:
                            if argv[3] in EDITORS:
                                ret_val = system(f'{argv[3]} {working_dir}')
                                if ret_val == 0:
                                    return
                        except IndexError:
                            pass
                        if 'editor' in codebase.keys():
                            if system(f'{codebase["editor"]} {working_dir}') == 0:
                                return
                        for editor in EDITORS:
                            ret_val = system(f'{editor} {working_dir}')
                            if ret_val == 0:
                                return
                        print(f'Valid Editors: {", ".join(EDITORS)}')
                    else:
                        chdir(working_dir)
                        system('/bin/bash')
                except IndexError:
                    chdir(working_dir)
                    system('/bin/bash')
                return


    print("Valid commands are: ")
    for codebase_key, codebase_value in codebases.items():
        valid_commands = ', '.join(codebase_value['valid_commands'])
        print(f'{codebase_key}: {valid_commands}')

if __name__ == '__main__':
    main()