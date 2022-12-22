#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-energy
Version  : 1.7.11
Release  : 54
URL      : https://cran.r-project.org/src/contrib/energy_1.7-11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/energy_1.7-11.tar.gz
Summary  : E-Statistics: Multivariate Inference via the Energy of Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-energy-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-gsl
BuildRequires : R-Rcpp
BuildRequires : R-gsl
BuildRequires : buildreq-R

%description
including distance correlation, one-sample, two-sample, and multi-sample tests for
             comparing multivariate distributions, are implemented. Measuring and testing
             multivariate independence based on distance correlation, partial distance correlation,
             multivariate goodness-of-fit tests, k-groups and hierarchical clustering based on energy 
             distance, testing for multivariate normality, distance components (disco) for non-parametric 
             analysis of structured data, and other energy statistics/methods are implemented.

%package lib
Summary: lib components for the R-energy package.
Group: Libraries

%description lib
lib components for the R-energy package.


%prep
%setup -q -n energy
cd %{_builddir}/energy

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671727509

%install
export SOURCE_DATE_EPOCH=1671727509
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/energy/DESCRIPTION
/usr/lib64/R/library/energy/INDEX
/usr/lib64/R/library/energy/Meta/Rd.rds
/usr/lib64/R/library/energy/Meta/data.rds
/usr/lib64/R/library/energy/Meta/features.rds
/usr/lib64/R/library/energy/Meta/hsearch.rds
/usr/lib64/R/library/energy/Meta/links.rds
/usr/lib64/R/library/energy/Meta/nsInfo.rds
/usr/lib64/R/library/energy/Meta/package.rds
/usr/lib64/R/library/energy/NAMESPACE
/usr/lib64/R/library/energy/NEWS.md
/usr/lib64/R/library/energy/R/energy
/usr/lib64/R/library/energy/R/energy.rdb
/usr/lib64/R/library/energy/R/energy.rdx
/usr/lib64/R/library/energy/data/Rdata.rdb
/usr/lib64/R/library/energy/data/Rdata.rds
/usr/lib64/R/library/energy/data/Rdata.rdx
/usr/lib64/R/library/energy/help/AnIndex
/usr/lib64/R/library/energy/help/aliases.rds
/usr/lib64/R/library/energy/help/energy.rdb
/usr/lib64/R/library/energy/help/energy.rdx
/usr/lib64/R/library/energy/help/paths.rds
/usr/lib64/R/library/energy/html/00Index.html
/usr/lib64/R/library/energy/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/energy/libs/energy.so
/usr/lib64/R/library/energy/libs/energy.so.avx2
/usr/lib64/R/library/energy/libs/energy.so.avx512
