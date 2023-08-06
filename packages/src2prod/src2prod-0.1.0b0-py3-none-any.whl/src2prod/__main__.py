#!/usr/bin/env python3

###
# This module implements a Comand Line Interface.
###


import click

from .project import *


# --------- #
# -- CLI -- #
# --------- #

###
# prototype::
###
def _exit(message):
    print(
f"""
Try 'python -m src2prod --help' for help.

Error: {message}
""".strip()
    )

    exit(1)


###
# prototype::
#     project : the folder project that will be used to communicate during
#               the analysis.
#     src     : the **relative** path of the source dir (regarding the project
#               folder).
#     target  : the **relative** path of the final product dir (regarding the
#               project folder).
#     ignore  : the rules for ignoring files in addition to what ¨git does.
#               You can use this argument even if you don't work with
#     usegit  : ``True`` asks to use ¨git contrary to ``False``.
#     readme  : ``''`` is if you don't need to import an external
#               path::``README`` file, otherwise give a **relative** path.
#
#     :action: this function allows to update a project from a terminal.
###
@click.command()
@click.argument('project')
@click.option('--src',
              default = 'src',
              help    = 'Relative path of the source folder of the project. '
                        'The default value is "src".')
@click.option('--target',
              default = '',
              help    = 'Relative path of the targer folder of the project. '
                        'The default value "", an empty string, indicates '
                        'to use the name, in lower case, of the project.')
@click.option('--ignore',
              default = '',
              help    = 'Path to a file with the rules for ignoring '
                        'files in addition to what git does. '
                        'The default value "", an empty string, indicates '
                        'to not use any rule.')
@click.option('--usegit',
              is_flag = True,
              help    = 'This flag is to use git.')
@click.option('--readme',
              default = '',
              help    = 'Relative path of an external "README" file or "readme" folder. '
                        'The default value "", an empty string, indicates '
                        'to not use any external "README" file.')
@click.option('--notsafe',
              is_flag = True,
              help    = 'TO USE WITH A LOT OF CAUTION! '
                        'This flag allows to remove a none empty target folder.')
def src2prodcli(
    project: str,
    src    : str,
    target : str,
    ignore : str,
    usegit : bool,
    readme : str,
    notsafe: bool,
) -> None:
    """
    Update your "source-to-product" like projects using the Python module src2prod.

    PROJECT: the path of the project to update.
    """
    if not notsafe:
        print('WARNING: Using not ``--notsafe`` can be dangerous.')

# What is the target?
    if target == '':
        project = Path(project)
        target  = project.name.lower()

# readme: '' --> None
    if not readme:
        readme = None

# Do we have an "ignore" path?
    if ignore:
        ignore = Path(ignore)

# Let the class Project does the job.
    try:
        Project(
            project = project,
            source  = src,
            target  = target,
            ignore  = ignore,
            usegit  = usegit,
            readme  = readme,
        ).update(
            safemode = not notsafe
        )

    except Exception as e:
        _exit(repr(e))


# --------------------------------------------- #
# --- Entry point for ``python -m src2prod`` -- #
# --------------------------------------------- #

src2prodcli()
