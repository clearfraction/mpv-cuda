%global gitdate 20221014
%global commit dfb5b0c55fa442ca53208f6b38ad3885acf945f8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name     : mpv-cuda
Version  : 0.34.1
Release  : 107.%{shortcommit}
URL      : https://github.com/mpv-player/mpv
Source0  : %{url}/archive/%{commit}/mpv-%{shortcommit}.tar.gz
#Source   : https://github.com/mpv-player/mpv/archive/refs/heads/master.zip 
Patch1   : 0001-waf-add-waf-as-a-patch-for-ClearLinux.patch
Patch2   : 0002-Makefile-quick-wrapper-for-waf-cuda.patch
Summary  : media player
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libvdpau-lib
Requires: ffmpeg-cuda-libs
Requires: mpv-cuda-bin = %{version}-%{release}
Requires: mpv-cuda-data = %{version}-%{release}
Requires: mpv-cuda-lib = %{version}-%{release}
Requires: mpv-cuda-license = %{version}-%{release}
#Requires: mpv-cuda-filemap = %%{version}-%%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : SPIRV-Cross-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXpresent-dev
BuildRequires : libXv-dev
BuildRequires : libvdpau-dev
BuildRequires : libva-dev
BuildRequires : mesa-dev 
BuildRequires : nv-codec-headers
BuildRequires : ffmpeg-cuda-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(libass)
BuildRequires : pkgconfig(libplacebo)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xpresent)
BuildRequires : pkgconfig(xv)
BuildRequires : zlib-dev
BuildRequires : SDL2-dev
BuildRequires : LuaJIT-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libarchive)

# fonts-related
BuildRequires : v4l-utils-dev fontconfig-dev fribidi-dev harfbuzz-dev libpng-dev


%description
TA ("Tree Allocator") is a wrapper around malloc() and related functions,
adding features like automatically freeing sub-trees of memory allocations if
a parent allocation is freed.
 
%package bin
Summary: bin components for the mpv package.
Group: Binaries
Requires: mpv-cuda-data = %{version}-%{release}
Requires: mpv-cuda-license = %{version}-%{release}
#Requires: mpv-cuda-filemap = %%{version}-%%{release}

 
%description bin
bin components for the mpv package.
 
 
%package data
Summary: data components for the mpv package.
Group: Data
 
%description data
data components for the mpv package.
 
 
%package dev
Summary: dev components for the mpv package.
Group: Development
Requires: mpv-cuda-lib = %{version}-%{release}
Requires: mpv-cuda-bin = %{version}-%{release}
Requires: mpv-cuda-data = %{version}-%{release}
Provides: mpv-cuda-devel = %{version}-%{release}
Requires: mpv-cuda = %{version}-%{release}
 
%description dev
dev components for the mpv package.
 
 
%package doc
Summary: doc components for the mpv package.
Group: Documentation
 
%description doc
doc components for the mpv package.
 
%package lib
Summary: lib components for the mpv package.
Group: Libraries
Requires: mpv-cuda-data = %{version}-%{release}
Requires: mpv-cuda-license = %{version}-%{release}
#Requires: mpv-cuda-filemap = %%{version}-%%{release}

 
%description lib
lib components for the mpv package.
 
 
%package license
Summary: license components for the mpv package.
Group: Default
 
%description license
license components for the mpv package.


%prep
%setup -q -n mpv-%{commit}
%patch1 -p1
%patch2 -p1


%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export PKG_CONFIG_PATH="/usr/local/lib64/pkgconfig"
export LDFLAGS="-Wl,-rpath=/usr/local-cuda/lib64,-rpath=/opt/3rd-party/bundles/clearfraction/usr/local-cuda/lib64,-rpath=/opt/3rd-party/bundles/clearfraction/usr/lib64"
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
make  %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local-cuda/share/package-licenses/mpv
cp Copyright %{buildroot}/usr/local-cuda/share/package-licenses/mpv/Copyright
cp LICENSE.GPL %{buildroot}/usr/local-cuda/share/package-licenses/mpv/LICENSE.GPL
cp LICENSE.LGPL %{buildroot}/usr/local-cuda/share/package-licenses/mpv/LICENSE.LGPL
%make_install
rm -f %{buildroot}/usr/local-cuda/share/man/man1/mpv.1
mv %{buildroot}/usr/local-cuda %{buildroot}/usr/local

 
%files
%defattr(-,root,root,-)
 
%files bin
%defattr(-,root,root,-)
/usr/local/bin/mpv
 
%files data
%defattr(-,root,root,-)
/usr/local/share/applications/mpv.desktop
/usr/local/share/icons/hicolor/16x16/apps/mpv.png
/usr/local/share/icons/hicolor/32x32/apps/mpv.png
/usr/local/share/icons/hicolor/64x64/apps/mpv.png
/usr/local/share/icons/hicolor/128x128/apps/mpv.png
/usr/local/share/icons/hicolor/scalable/apps/mpv.svg
/usr/local/share/icons/hicolor/symbolic/apps/mpv-symbolic.svg
/usr/local/share/zsh/site-functions/_mpv
/usr/local/share/bash-completion/completions/mpv
/usr/local/share/metainfo/mpv.metainfo.xml
 
%files dev
%defattr(-,root,root,-)
/usr/local/include/mpv/client.h
/usr/local/include/mpv/render.h
/usr/local/include/mpv/render_gl.h
/usr/local/include/mpv/stream_cb.h
/usr/local/lib64/libmpv.so*
/usr/local/lib64/pkgconfig/mpv.pc
 
%files doc
%defattr(0644,root,root,0755)
%doc /usr/local/share/doc/mpv/*
 
%files lib
%defattr(-,root,root,-)
/usr/local/lib64/libmpv.so.*
 
%files license
%defattr(0644,root,root,0755)
/usr/local/share/package-licenses/mpv/Copyright
/usr/local/share/package-licenses/mpv/LICENSE.GPL
/usr/local/share/package-licenses/mpv/LICENSE.LGPL
