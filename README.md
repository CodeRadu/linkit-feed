# linkit-feed

This is a feed for the LinkIt Smart 7688 (not duo).

## Installation

### 1. Install the build dependencies

```sh
sudo apt install git g++ make libncurses5-dev subversion libssl-dev gawk libxml-parser-perl unzip wget python3 xz-utils flex
```

### 2. Download the openwrt source code

```sh
git clone -b openwrt-23.05 https://github.com/openwrt/openwrt.git
```

### 3. Setup feeds

```sh
cd openwrt
cp feeds.conf.default feeds.conf
echo "src-git linkit https://github.com/CodeRadu/linkit-feed.git" >> feeds.conf
./scripts/feeds update
./scripts/feeds install -a
```

### 4. Setup build config

```sh
make menuconfig
```

- Select the following options:
  - Target System: `MediaTek Ralink MIPS`
  - Subtarget: `MT76x8 based boards`
  - Target Profile: `MediaTek LinkIt Smart 7688`

### 5. Build

```sh
make -j $(nproc)
```

- The target image will be in `bin/targets/ramips/mt76x8/`
