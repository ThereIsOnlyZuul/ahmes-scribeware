\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ahmesworksheet}[2014/08/16 Ahmes Scribeware Worksheet class]

\LoadClass{article}

% Set the paper size and margins
\RequirePackage{geometry}
\geometry{margin=.75}

% Mulitcols
\RequirePackage{multicol}
\setlength{\oclumnseprule}{2pt}

% Math
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{pgfplots}

% Fonts
\usepackage{pxfonts}

% Redefine maketitle

\renewcommand{\maketitle}{\makeworksheettitle}
\newcommand\makeworksheettitle{\@title}

% Ahmes Worksheet Commands