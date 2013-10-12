# revision 29803
# category Package
# catalog-ctan /language/french/frenchle
# catalog-date 2012-05-31 00:57:47 +0200
# catalog-license lppl
# catalog-version 5.9995
Name:		texlive-frenchle
Version:	5.9995
Release:	2
Summary:	French macros, usable stand-alone or with Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/french/frenchle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a redistribution and repackaging of the late Bernard
Gaulle's "light" package to typeset French documents according
to the rules of the "Imprimerie Nationale". The package offers
a package, two Babel language definition files (french.ldf and
frenchle.ldf), and a package to enable the non-standard
definition files to be loaded into an unmodified Babel. The
user may simply use frenchle.sty if typesetting a French-only
document, but should use Babel with the frenchle option for a
multilingual document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/frenchle/babelfr.sty
%{_texmfdistdir}/tex/latex/frenchle/french.ldf
%{_texmfdistdir}/tex/latex/frenchle/frenchle.cfg
%{_texmfdistdir}/tex/latex/frenchle/frenchle.ldf
%{_texmfdistdir}/tex/latex/frenchle/frenchle.sty
%doc %{_texmfdistdir}/doc/latex/frenchle/ALIRE.le
%doc %{_texmfdistdir}/doc/latex/frenchle/README
%doc %{_texmfdistdir}/doc/latex/frenchle/README.le
%doc %{_texmfdistdir}/doc/latex/frenchle/faq.pdf
%doc %{_texmfdistdir}/doc/latex/frenchle/frenchle.pdf
%doc %{_texmfdistdir}/doc/latex/frenchle/sources/faq.tex
%doc %{_texmfdistdir}/doc/latex/frenchle/sources/frenchle.tex
%doc %{_texmfdistdir}/doc/latex/frenchle/sources/myfroptn.sty
%doc %{_texmfdistdir}/doc/latex/frenchle/sources/mymaj.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
