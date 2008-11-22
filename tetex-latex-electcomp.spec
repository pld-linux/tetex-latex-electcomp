
%define short_name electcomp
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Electrical Circuits with pgf
Summary(hu.UTF-8):	Elektromos áramkörök pgf-fel
Name:		tetex-latex-%{short_name}
Version:	20080312
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://media.texample.net/tikz/examples/extra/circuit-decorations/tzbondgraph/electComp.sty
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-pgf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Electrical Circuits with pgf.

%description -l hu.UTF-8
Elektromos áramkörök pgf-fel

%prep
# empty

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%{_datadir}/texmf/tex/latex/%{short_name}
