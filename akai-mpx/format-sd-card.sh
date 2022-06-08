# These are all commented out for a reason
# If you do these incorrectly you can easily format hard drives
# and lose data etc, please do not use these unless you know which
# each part of the command means

# find out name, the sd slot for my laptop is /dev/mmcblk0
lsblk

# change XYZ to drive to wipe
sudo parted /dev/XYZ --script -- mklabel msdos
# format sd card as fat32
sudo parted /dev/XYZ --script -- mkpart primary fat32 1MiB 100%

sudo mkfs.vfat -F32 /dev/XYZ
