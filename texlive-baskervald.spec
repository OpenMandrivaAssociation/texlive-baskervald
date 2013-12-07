# revision 19490
# category Package
# catalog-ctan /fonts/baskervaldadf
# catalog-date 2010-07-14 23:45:16 +0200
# catalog-license lppl
# catalog-version 1.016
Name:		texlive-baskervald
Version:	1.016
Release:	5
Summary:	Baskervald ADF fonts collection with TeX/LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/baskervaldadf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervald.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervald.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervald.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Baskervald ADF is a serif family with lining figures designed
as a substitute for Baskerville. The family currently includes
upright and italic or oblique shapes in each of regular, bold
and heavy weights. All fonts include the slashed zero and
additional non-standard ligatures. The support package renames
them according to the Karl Berry fontname scheme and defines
two families. One of these primarily provides access to the
"standard" or default characters while the other supports
additional ligatures. The included package files provide access
to these features in LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvb8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvbi8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvh8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvho8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvr8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvri8a.afm
%{_texmfdistdir}/fonts/enc/dvips/baskervald/supp-ybv.enc
%{_texmfdistdir}/fonts/map/dvips/baskervald/ybv.map
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbiw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvhow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvhw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvriw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvrw8t.tfm
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvb8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvb8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvbi8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvbi8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvh8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvh8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvho8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvho8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvr8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvr8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvri8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvri8a.pfm
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvb8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvb8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbi8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbi8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbiw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvh8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvh8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvho8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvho8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvhow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvhw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvr8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvr8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvri8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvri8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvriw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvrw8t.vf
%{_texmfdistdir}/tex/latex/baskervald/baskervald.sty
%{_texmfdistdir}/tex/latex/baskervald/t1ybv.fd
%{_texmfdistdir}/tex/latex/baskervald/t1ybvw.fd
%{_texmfdistdir}/tex/latex/baskervald/ts1ybv.fd
%{_texmfdistdir}/tex/latex/baskervald/ts1ybvw.fd
%doc %{_texmfdistdir}/doc/fonts/baskervald/COPYING
%doc %{_texmfdistdir}/doc/fonts/baskervald/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/baskervald/README
%doc %{_texmfdistdir}/doc/fonts/baskervald/baskervaldadf.pdf
%doc %{_texmfdistdir}/doc/fonts/baskervald/baskervaldadf.tex
%doc %{_texmfdistdir}/doc/fonts/baskervald/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/baskervald/reglyph-ybv.tex
%doc %{_texmfdistdir}/source/fonts/baskervald/supp-ybv.etx
%doc %{_texmfdistdir}/source/fonts/baskervald/t1-baskervald-lig.etx
%doc %{_texmfdistdir}/source/fonts/baskervald/t1-baskervald.etx
%doc %{_texmfdistdir}/source/fonts/baskervald/ts1-baskervald.etx
%doc %{_texmfdistdir}/source/fonts/baskervald/ybv-drv.tex
%doc %{_texmfdistdir}/source/fonts/baskervald/ybv-map.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.016-2
+ Revision: 749452
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.016-1
+ Revision: 717886
- texlive-baskervald
- texlive-baskervald
- texlive-baskervald
- texlive-baskervald
- texlive-baskervald

