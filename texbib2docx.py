# -*- coding: utf-8 -*-
# %% 
# CSL = r'%~dp0\__configCollection\TeX\GOST_R_7011_numeric1a.csl'
CSLrel = r'__configCollection\TeX\GOST_R_7011_numeric1a.csl'
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
            S=[r'.\data-pr\doc1.tex'],
            batNameTemplate='compile_%s_.bat',
            docxNameTemplate='%s~out.docx',
            doNotStart_rez_docx=False,
            csl = CSLrel,
        )
    else:
        aparser = argparse.ArgumentParser(description='parse TeX to create pandoc convert bat with citeproc')
        #aparser.add_argument('-m','--IgnoreSzLess',dest='IgnoreSzLess', type=int, default=1024, help='ignore files with size less ... (def 1024)')
        # aparser.add_argument('-i','--OnlyInfo',dest='onlyInfo', action='store_true', default=False, help='do not create links- just report')
        # aparser.add_argument('integers', metavar='N', type=int, nargs='+',help='...')
        aparser.add_argument('S', metavar='TeX_file', type=str, nargs=1,help='tex file to process')
        aparser.add_argument('-b','--batNameTemplate',dest='batNameTemplate', type=str,  default='compile_%s_.bat', help='template of out bat where `%%s` is name of src TeX file (`` for not create)') 
        aparser.add_argument('-d','--docxNameTemplate',dest='docxNameTemplate', type=str,  default='%s~out.docx',  help='template of out DOCX where `%%s` is name of src TeX file') 
        aparser.add_argument('-q','--doNotStart_rez_docx',dest='doNotStart_rez_docx', action='store_true', default=False, help='do not start result docx')
        aparser.add_argument('-s','--csl',dest='csl', type=str, default=CSLrel, help='absolute or relative to THIS SCRIPT pathname of CSL style file')
        args = aparser.parse_args()

    print(args, '      (from', 'predefined debug' if isVScode else 'cli args', ')')
    return isVScode, args


# %%

# %%

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
    # %%
    odocx=args.docxNameTemplate%(str(s.absolute().relative_to(pr)))
    # %%
    csl=pcsl if (pcsl:=Path(args.csl)).is_absolute() else Path(__file__).parent.joinpath(CSLrel).absolute()
    if not csl.is_file(): raise Exception(f'can`t find CSL in it`s place or specified path (`{csl}`)')
    # %%
    sbat1 = f'pandoc {str(s.absolute().relative_to(pr))} {bibsrcsstr} --citeproc '+\
            f'--csl="{str(csl)}" -o {odocx}'
    print(sbat1)    #print only main convert string in case you want create oun bat by `>` of stdout
    # %%
    sbat1 +=f''' ||(
        @echo eccor occured!
        @exit /b 1
        )
    ''' 
    sbat1 +=f'\nstart {odocx}\n' if not args.doNotStart_rez_docx else ''
    
    sbat1 = f'@move {odocx} {odocx}.old.bak \n\n' + sbat1
    sbat1 +=f'exit /b\n' 
    sbat1
    # %%
    if (args.batNameTemplate!=''):
        obatname=args.batNameTemplate%(str(s.absolute().relative_to(pr)))
        obatp=pr.joinpath(obatname)
        obatp.write_text(sbat1+'\n','utf8')
    # %%
    if not args.doNotStart_rez_docx:
        os.system(f'cd /d {str(pr)} & start {str(obatp)} ')
    # %%
    