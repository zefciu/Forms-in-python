forms.pdf: forms.latex styles.tex formalchemy.tex sprox.tex django.tex
	latex -output-format=pdf forms.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

formalchemy.tex: formalchemy.py Makefile
	pygmentize -l py -o formalchemy.tex formalchemy.py

sprox.tex: sprox.py Makefile
	pygmentize -l py -o sprox.tex sprox.py

django.tex: django.py Makefile
	pygmentize -l py -o django.tex django.py
