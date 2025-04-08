%global gitdate 20250325
%global commit e48ac7ce08462f5e33af6ef9deeac6fa87eef01e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name     : mpv-cuda
Version  : 0.40.0
Release  : %{gitdate}.%{shortcommit}
URL      : https://github.com/mpv-player/mpv
Source0  : %{url}/archive/%{commit}/mpv-%{shortcommit}.tar.gz
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
BuildRequires : buildreq-meson
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
BuildRequires : pipewire-dev
BuildRequires : shaderc-dev uchardet-dev zimg-dev SPIRV-Headers-dev
BuildRequires : pkgconfig(vapoursynth)
BuildRequires : pkgconfig(vapoursynth-script)


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
git config --global --add safe.directory /home
# newest nv-codev-headers
unset https_proxy
curl -LO https://github.com/FFmpeg/nv-codec-headers/releases/download/n13.0.19.0/nv-codec-headers-13.0.19.0.tar.gz
tar xf nv-codec-headers-13.0.19.0.tar.gz && rm -rf *.tar.gz 
pushd nv-codec-headers-*
    make
    make PREFIX=/usr LIBDIR=lib64 install
popd



%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export PKG_CONFIG_PATH="/usr/local/lib64/pkgconfig"
export LDFLAGS="-Wl,-rpath=/usr/local-cuda/lib64,-rpath=/opt/3rd-party/bundles/clearfraction/usr/local-cuda/lib64,-rpath=/opt/3rd-party/bundles/clearfraction/usr/lib64 "
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export LDFLAGS="-Wl,-rpath=/opt/3rd-party/bundles/clearfraction/usr/lib64,-rpath=/usr/lib64 "
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
meson --libdir=lib64 --prefix=/usr/local-cuda --buildtype=plain \
      -Dalsa=enabled \
      -Dbuild-date=false \
      -Dcaca=disabled \
      -Dcdda=disabled \
      -Dcplayer=true \
      -Dcplugins=enabled \
      -Dcuda-hwaccel=enabled \
      -Dcuda-interop=enabled \
      -Ddmabuf-wayland=enabled \
      -Ddrm=enabled \
      -Ddvbin=enabled \
      -Ddvdnav=disabled \
      -Degl-drm=enabled \
      -Degl-wayland=enabled \
      -Degl-x11=enabled \
      -Degl=enabled \
      -Dgbm=enabled \
      -Dgl-x11=enabled \
      -Dgl=enabled \
      -Dhtml-build=disabled \
      -Dpdf-build=disabled \
      -Diconv=enabled \
      -Djack=disabled \
      -Djavascript=disabled \
      -Djpeg=enabled \
      -Dlcms2=disabled \
      -Dlibarchive=enabled \
      -Dlibavdevice=enabled \
      -Dlibbluray=disabled \
      -Dlibmpv=true \
      -Dlua=enabled \
      -Dmanpage-build=disabled \
      -Dopenal=disabled \
      -Dopensles=disabled \
      -Doss-audio=disabled \
      -Dpipewire=enabled \
      -Dplain-gl=enabled \
      -Dpulse=enabled \
      -Drubberband=disabled \
      -Dsdl2-audio=disabled \
      -Dsdl2-gamepad=disabled \
      -Dsdl2-video=disabled \
      -Dsdl2=disabled \
      -Dshaderc=disabled \
      -Dsndio=disabled \
      -Dspirv-cross=disabled \
      -Duchardet=enabled \
      -Dvaapi-drm=enabled \
      -Dvaapi-wayland=enabled \
      -Dvaapi-x11=enabled \
      -Dvaapi=enabled \
      -Dvapoursynth=disabled \
      -Dvdpau-gl-x11=disabled \
      -Dvdpau=disabled \
      -Dvector=enabled \
      -Dvulkan=enabled \
      -Dwayland=enabled \
      -Dwerror=false \
      -Dx11=enabled \
      -Dxv=enabled \
      -Dzimg=enabled \
      -Dzlib=enabled      builddir

ninja -v -C builddir
      

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rvf %{buildroot}/usr/local-cuda/share/doc %{buildroot}/usr/local-cuda/etc
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
/usr/share/fish/vendor_completions.d/mpv.fish
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
 
%files lib
%defattr(-,root,root,-)
/usr/local/lib64/libmpv.so.*
 
%files license
%defattr(0644,root,root,0755)
