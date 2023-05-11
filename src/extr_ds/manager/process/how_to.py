


def print_help() -> None:
    print()
    print('----- extr-ds -----')
    print(' * --init')
    print(' |   sets up workspace')
    print(' |   example: extr-ds --init')
    print(' * --reset')
    print(' |   cleans out saved annotations')
    print(' |   example: extr-ds --reset')
    print(' * --split')
    print(' |   subset source file and run all annotations')
    print(' |   example: extr-ds --split')
    print(' * --annotate -ents')
    print(' |   run annotation rules for entities')
    print(' |   example: extr-ds --annotate -ents')
    print(' * --annotate -rels')
    print(' |   run annotation rules for relations')
    print(' |   example: extr-ds --annotate -rels')
    print(' * --relate -label <label>=<rows>')
    print(' |   <rows>: list of row ids to set as <label>')
    print(' |   example: extr-ds --relate -label NO_RELATION=1,3,6')
    print(' * --relate -delete <rows>')
    print(' |   <rows>: list of row ids to remove')
    print(' |   example: extr-ds --relate -delete 1,3,6')
    print(' * --relate -recover <rows>')
    print(' |   <rows>: list of row ids to undelete')
    print(' |   example: extr-ds --relate -recover 1,3,6')
    print(' * --save -ents')
    print(' |   saves entities for model building')
    print(' |   example: extr-ds --save -ents')
    print(' * --save -rels')
    print(' |   saves relations for model building')
    print(' |   example: extr-ds --save -rels')
