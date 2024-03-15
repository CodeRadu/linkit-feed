include $(TOPDIR)/rules.mk

PKG_NAME:=linkit-python3
PKG_VERSION:=1.0
PKG_RELEASE:=1

include $(INCLUDE_DIR)/package.mk

define Package/linkit-python3
	TITLE:=Linkit Smart 7688 python3
	DEPENDS:=@TARGET_ramips_mt76x8_DEVICE_mediatek_linkit-smart-7688 \
		+python3-light +python3-gpiod
	CATEGORY:=Board
endef

define Package/linkit-python3/description
	Includes python3-light, python3-gpiod and iot examples
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
endef

define Build/Compile
endef

define Package/linkit-python3/install
	$(CP) ./files/* $(1)
endef

$(eval $(call BuildPackage,linkit-python3))
