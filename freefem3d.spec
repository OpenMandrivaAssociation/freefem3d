Name:          freefem3d
Version:       1.0
Release:       %mkrel 0.pre9.2
Summary:       FreeFEM3D is a 3D version of freeFEM
License:       GPL
Group:         Sciences/Mathematics
Url:           http://www.freefem.org/ff3d/index.html
Source:        %{name}-%{version}pre9+cvs.tar.gz

BuildRequires: bison
BuildRequires: tetex-latex
# (nl) Readd those buildrequires when vtk will be builded against Qt4
#BuildRequires: qt4-devel
#BuildRequires: vtk-devel
#BuildRequires: libvtk-qt

%description
freeFEM3D is a 3D version of freeFEM.
It is a 3D finite element PDE solver. It does not use standard FEM 
approximation but is based on fictitious domain method. The main 
reason for this is the absence of free 3D mesh generators.
freeFEM3D, as well as its cousins, is a PDE solver driven by a user 
friendly language.

%files 
%defattr(-,root,root,0755)
%{_bindir}/ff3d

#--------------------------------------------------------------------


%prep
rm -rf %buildroot

%setup -q -n ff3d

%build

%configure --disable-gui


make 

%install
%makeinstall

%clean
rm -rf %buildroot


