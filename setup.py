from cx_Freeze import *

setup(
    name='File Oraganiser',
    options={'build_exe':{'packages':['tkinter']}},
    # version='1.0',
    # packages=[''],
    # url='',
    # license='',
    # author='swapnil',
    # author_email='swapnilbobe9@gmail.com',
    # description='You can organise your folder by file extensions',
    executables=[Executable('tk.py',
                           )]
    )
