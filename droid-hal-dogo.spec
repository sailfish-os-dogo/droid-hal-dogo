%define device dogo
%define vendor sony
%define vendor_pretty Sony
%define device_pretty Xperia ZR
%define installable_zip 1
%define straggler_files \
   /bugreports\
   /d\
   /nonplat_file_contexts\
   /nonplat_hwservice_contexts\
   /nonplat_property_contexts\
   /nonplat_seapp_contexts\
   /nonplat_service_contexts\
   /plat_file_contexts\
   /plat_hwservice_contexts\
   /plat_property_contexts\
   /plat_seapp_contexts\
   /plat_service_contexts\
   /sdcard\
   /vendor\
   /vndservice_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
