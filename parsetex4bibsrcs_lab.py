# -*- coding: utf-8 -*-
# %% 
CSL = r'D:\nemo\UTILS\__configCollection\TeX\GOST_R_7011_numeric1a.csl'
# %% ------------------------- imports std lab set --------------------------- #
from turtle import isvisible
from typing import Dict,Optional,List,Sequence,Iterable,Any, Tuple, Union, cast,ClassVar,Callable
from pathlib import Path
import re
import sys,os
# %% ------------------------------------------------------------------------- #
# %%
# ------------------------------ def getArgs(): ------------------------------ #
def getArgs():
    #isVScode = any(['ipykernel_launcher' in argvi for argvi in sys.argv])
    isVScode = 'get_ipython' in globals() and (get_ipython().__class__.__name__ == 'ZMQInteractiveShell')  #type: ignore
    import argparse
    aparser = argparse.ArgumentParser(description='...description...')
    if isVScode:
        args = argparse.Namespace(
            # S=['doc1.tex']
            S=[r'.\data-pr\doc1.tex']
        )
    else:
        #aparser.add_argument('-m','--IgnoreSzLess',dest='IgnoreSzLess', type=int, default=1024, help='ignore files with size less ... (def 1024)')
        # aparser.add_argument('-i','--OnlyInfo',dest='onlyInfo', action='store_true', default=False, help='do not create links- just report')
        # aparser.add_argument('integers', metavar='N', type=int, nargs='+',help='...')
        aparser.add_argument('S', metavar='TeX_file', type=str, nargs=1,help='tex file to process')
        # aparser.add_argument('-g', '--gui', dest='gui', action='store_true', default=False, help='gui progress')
        # aparser.add_argument('infls', metavar='infls', type=str, nargs='*', help='file to view')
        args = aparser.parse_args()

    print(args, '      (from', 'predefined debug' if isVScode else 'cli args', ')')
    return isVScode, args

# %%
def parseTex_find_bibs(s:Union[str,Path])->list:
    '''path for all existed bib soruces, mensioned in tex'''
    if not isinstance(s,Path): s=Path(s)
    if not s.is_file(): raise FileNotFoundError('1st arg must be TeX file to process')
    tx=s.read_text(encoding='utf8')
    fndallbib = re.findall(r'^\s*?\\addbibresource{\s*(.*?)\s*?}\s*?$',tx,re.IGNORECASE+re.MULTILINE+re.UNICODE)
    # path for all existed bib soruces
    fndallbib = [p for f in fndallbib if (p:=pr.joinpath(f)).is_file() ]
    return fndallbib


# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%

# %%
# %%
# %%
# ============================================================================ #
#                                     main                                     #
# ============================================================================ #
if __name__ == "__main__":
    pass
    # %% ------------------------------------------------------------------------- #
    isVScode, args=getArgs()
    s=Path(args.S[0])   #process only 1 tex for now. see `nargs`
    pr=s.parent.absolute()
    fndallbib=parseTex_find_bibs(s)
    bibsrcsstr=' '.join([ f' --bibliography={str(Path(a).absolute().relative_to(pr))}'  for a in fndallbib])
    print(bibsrcsstr)
    print(f'pandoc {str(s)} {bibsrcsstr} --citeproc --csl={CSL} -o doc1~out.docx & start doc1~out.docx')

    # %%