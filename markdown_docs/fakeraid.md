# What is FakeRAID?
FakeRAID is a RAID functionality that is provided by the motherboard BIOS or SATA cards that has RAID capabilities but technically operating system perform the bulk of the processing. This is done in the form of software drivers provided by the motherboard/SATA card manufacturers.

Note that this is not to be confused with a hardware RAID which does offer RAID functionalities by itself and does not require drivers to perform RAID on the OS itself.

However, some hardware RAID cards do require drivers to be able to see the virtual disk. The RAID card will do everything by its own, and the OS just sees the virtual disks but do not get involved in RAID logic processing.

# Why would anyone use FakeRAID?
Cost. And because it's offered by the board.

# Downsides of FakeRAID

## Non-portability
Disks created on FakeRAID are generally non-portable, i.e., it only works with specific FakeRAID implementation.

## No monitoring
Some, if not all implementations has no monitoring of your FakeRAID arrays. This is particularly problematic as disks eventually will fail and needs replacing.



## Recovery can be difficult, or sometimes impossible
As FakeRAID is provided by the BIOS, there's no standardized format. Each vendor implements their own format which would mean you will have to use the exact hardware in order to recover the data on the disk.

The good news is some vendors uses DDF for their FakeRAID storage which Linux `dmraid` are able to read to varying levels of success. 

# Does that mean that hardware RAID is better?
Yes, and no.

Hardware RAID still shares some downsides of FakeRAID, especially on non-portability but hardware RAID use are widespread in enterprise environments which generally has better firmware quality as well as monitoring.

# Do I have other alternatives?
If you're on Windows, you can utilize the built-in RAID feature that is provided by Windows.

If you're on Linux, you have a lot of choices in which `md` would be your primary choice as it's included in virtually any kernel. The `mdadm` user-space tool is available for most major Linux distributions.

If you still prefer to have access on both Linux and Windows, consider using a NAS with multiple disks. NAS itself uses Samba/CIFS which has good cross-platform support and should be able to utilize the storage without much hassle.