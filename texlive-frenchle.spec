Name:		texlive-frenchle
Version:	5.9993
Release:	1
Summary:	French macros, usable stand-alone or with Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/french/frenchle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a light (and free) version of the excellent (shareware)
French Pro package for LaTeX, a package to typeset French
documents according to the rules of the "Imprimerie Nationale".
The package comprises three LaTeX files (plus documentation,
etc.): frenchle.sty is for use in a French-only document, while
frenchle.ldf is for use as a babel language file (utilised by
\usepackage[frenchle]{babel}; note that babel itself no longer
permits such usage, but the babelfr.sty package in this
distribution makes it possible).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/frenchle/babelfr.sty
%{_texmfdistdir}/tex/latex/frenchle/french.ldf
%{_texmfdistdir}/tex/latex/frenchle/frenchle.cfg
%{_texmfdistdir}/tex/latex/frenchle/frenchle.ldf
%{_texmfdistdir}/tex/latex/frenchle/frenchle.sty
%doc %{_texmfdistdir}/doc/latex/frenchle/FAQ.pdf
%doc %{_texmfdistdir}/doc/latex/frenchle/README.le
%doc %{_texmfdistdir}/doc/latex/frenchle/frenchle.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
