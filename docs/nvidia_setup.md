# How to setup nvidia jetson nano kits
### You need:
- [ ] A **micro SD card*** with 64GB+ storage to flashing the OS onto 
- [ ] An **hdmi cable** to connect the kit to a monitor
- [ ] A **power cable** for the nvidia computer
- [ ] A **micro-usb cable** to connect the kit to a computer
- [ ] A **jumper-cable**
- [ ] An **nvidia jetson nano kit** (obviously)

## Sanity Check (and for bootable SD cards)
1. Put the micro SD-card in an adapter and into your laptop.
2. In the disk manager, check if the SD-card has its full sotrage available. 

**If yes:** Proceed to the step [SDK manager](#sdk-manager).
**If no:** Continue with the steps below.

3. Go into the SD-card storage manager by clicking on the Sd-card in your file system. On the top right, make sure you are in `/dev/mmcblk0` or a similar directory, and not the local. 
4. Delete all partitions or other elements that are not `Free Space`. IF only free space is left, continue to [SDK manager](#sdk-manager). 


## SDK manager
1. Start the SDK manager on your laptop.
2. Choose `Jetson nano modules` as your target device and click on next step.
3. Accept the conditions at the bottom left and click next step.
4. Choose manual setup and the nano jetson kit with 2GB. Use the jumper cable on `FC REC` (Force recovery) and the `GND` (ground) node above it.  Set the username and password.
5. Remove the jumper cable. 
6. Click on flash. You should see a progress bar with the flash progress. 
7. Wait for the OS-screen on your monitor, even if the flashing process is complete. Then click install. 

