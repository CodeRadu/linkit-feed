include $(TOPDIR)/rules.mk

PKG_NAME:=linkit-defconfig
PKG_VERSION:=1.0
PKG_RELEASE:=1

include $(INCLUDE_DIR)/package.mk

define Package/linkit-defconfig
	TITLE:=Linkit Smart 7688 default configuration
	DEPENDS:=@TARGET_ramips_mt76x8_DEVICE_mediatek_linkit-smart-7688 \
		+luci +uhttpd +openssh-sftp-server +libgpiod \
		+kmod-fs-vfat +kmod-fs-exfat +block-mount \
		+kmod-fs-ext4 +e2fsprogs
	CATEGORY:=Board
	DEFAULT:=y
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
endef

define Build/Compile
endef

define Package/linkit-defconfig/install
	$(CP) ./files/* $(1)
endef

$(eval $(call BuildPackage,linkit-defconfig))
