\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ahmesworksheet}[2014/08/16 Ahmes Scribeware Worksheet class]

\LoadClass{article}

% Set the paper size and margins
\RequirePackage{geometry}
\geometry{margin=.75in}

% Mulitcols
\RequirePackage{multicol}
\setlength{\columnseprule}{2pt}

% Math
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{pgfplots}

% Fonts
\usepackage{fontspec}
\setromanfont[Ligatures=TeX]{TeX Gyre Schola}
\usepackage{unicode-math}

\setmathfont[math-style=ISO,bold-style=ISO]{TeX Gyre Schola Math}


% Redefine maketitle

\renewcommand{\maketitle}{\makeworksheettitle}
\newcommand\makeworksheettitle{
\tline{Student Name}{\lgblank}\hfil
\tline{Date}{\mdblank}\hfil
\tline{Class}{\mdblank}
\newline
\worksheettitle
}

\newcommand\worksheettitle{
	{{\hspace{1in}} {\Large\bfseries{\@title}}}
}

% Ahmes Worksheet Commands
\newcommand{\blank}[1]{\underline{\hspace{#1}}}
\newcommand{\tline}[2]{$\underset{\text{#1}}{\text{\underline{\hspace{#2}}}}$}

% Custom Lengths

\newlength{\smblank}
\setlength{\smblank}{.5in plus .25in minus .25in}
\newlength{\mdblank}
\setlength{\mdblank}{1in plus .25in minus .75in}
\newlength{\lgblank}
\setlength{\lgblank}{2in plus .25in minus 1.5in}
\newlength{\xlgblank}
\setlength{\xlgblank}{2.5in plus .25in minus 1.5in}