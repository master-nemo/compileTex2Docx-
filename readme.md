# tex2docx via pandoc bib-gost-citeproc

### style 
based on https://github.com/Darxor/CSL-GOST  +some uncompatible fixes
https://github.com/Darxor/CSL-GOST/commit/f1f334a9f4eb840322d9fdbb83a7f4ee6cda9720


### bat params:
- in_file in 		_%1_ 
- bib_file in 		_%2_
- set custom style in _%3_ or default be used

### py params:
```
usage: texbib2docx.py [-h] [-b BATNAMETEMPLATE] [-d DOCXNAMETEMPLATE] [-q]
                      [-s CSL]
                      TeX_file

parse TeX to create pandoc convert bat with citeproc

positional arguments:
  TeX_file              tex file to process

optional arguments:
  -h, --help            show this help message and exit
  -b BATNAMETEMPLATE, --batNameTemplate BATNAMETEMPLATE
                        template of out bat where `%s` is name of src TeX file
                        (`` for not create)
  -d DOCXNAMETEMPLATE, --docxNameTemplate DOCXNAMETEMPLATE
                        template of out DOCX where `%s` is name of src TeX
                        file
  -q, --doNotStart_rez_docx
                        do not start result docx
  -s CSL, --csl CSL     absolute or relative to THIS SCRIPT pathname of CSL
                        style file
```


### tips used
thanks to:
- https://tex.stackexchange.com/questions/588317/how-to-generate-a-bibliography-with-pandoc
- https://tex.stackexchange.com/questions/316555/beginners-question-pandoc-latex-and-csl
