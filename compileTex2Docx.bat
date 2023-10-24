@echo in file in %%1 and bib file in %%2. set custom style in %%3 or default be used

@set d0=%~dp0


@set iname=%1
@set oname=%iname:.tex=~out.docx%

@set bibfile=%2
@echo use bibfile=%bibfile%

set style=%3
if not defined style (
    @set style=%d0%__configCollection\TeX\GOST_R_7011_numeric1a.csl
    )
@echo use style=%style%

exit /b

@move %oname% %oname%.old.bak

@rem https://tex.stackexchange.com/questions/588317/how-to-generate-a-bibliography-with-pandoc
@rem https://tex.stackexchange.com/questions/316555/beginners-question-pandoc-latex-and-csl
REM --------- you want to use CSL files you can't use biblatex or BibTeX (or other LaTeX bibliography packages), Pandoc will create the bibliography for you. I have therefore removed the biblatex and BibTeX tags. https://tex.stackexchange.com/questions/316555/beginners-question-pandoc-latex-and-csl
REM pandoc %iname% --bibliography=sample.bib --citeproc --csl=chicago-fullnote-bibliography.csl -o %oname% & start %oname%
REM ---------

@echo style=%style%
pandoc %iname% --biblatex --bibliography=%bibfile% --citeproc --csl=%style% -o %oname% & start %oname%

echo pandoc %iname% --biblatex --bibliography=%bibfile% --citeproc --csl=%style% -o %oname% ^& start %oname% > _%iname%_compile~.bat

