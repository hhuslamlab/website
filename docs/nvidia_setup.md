# How to setup nvidia jetson nano kits

## You need:

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

Connect all of your cables. Connect the jumper cable on `FC REC` and the `GND`above it.  
1. Start the SDK manager on your laptop.
2. Choose `Jetson nano modules` as your target device and click on next step.
3. Accept the conditions at the bottom left and click next step.
4. Choose manual setup and the nano jetson kit with 2GB. Set the username and password.
5. Remove the jumper cable. 
6. Click on flash. You should see a progress bar with the flash progress. 
7. Wait for the OS-screen on your monitor, even if the flashing process is complete. Then click install. 

# Connecting Jetson Nano to your device

On the backside of your device you can see labels starting with PIN 1. 

Connect the cables to the pins according to the below instructions.
```
Jetson Nano J50 Pin 4 (TXD) → White Wire
Jetson Nano J50 Pin 3 (RXD) → Green Wire
Jetson Nano J50 Pin 7 (GND) → Black Wire
```
Double check the cables. There are two GND pins, you need to connect to the seventh one, not the one below.  

## Windows

### Check your Ubuntu version

1. Press the Windows key.
2. Search for `Ubuntu` but DO NOT press enter.
3. On the right side, you should see the Ubuntu logo. Click on `app settings` below that. 
4. Make sure that the version starts with `2004`....

If your version is something else you need to uninstall Ubuntu. Search for Ubuntu again, the same way as in 1. and 2. Click on `uninstall`. Follow the instructions in the [WSL guide]() LINK!! to install WSL again. Then repeat the steps, starting from 1.  

### Install busipd 

Download and install usbipd-win by clicking on  https://github.com/dorssel/usbipd-win/releases

![usbipd](usbipd.png)

Follow the installation procedure and make sure that you complete all the steps.

### Install/update necessary packages

1. Launch Ubuntu.
2. Type `sudo apt update` and press enter.
3. Install linux tools with the lines below: 
```sh
sudo apt install linux-tools-5.4.0-77-generic hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/5.4.0-77-generic/usbip 20
```

4. DO NOT close Ubuntu. 

### Set up UART connection

1. Press the Windows key and search for `command prompt` 
2. Launch the Windows command prompt as an administrator. 
3. Type `usbipd wsl list`
4. Find the row that mentions `USB to UART` and get its BUSID from the leftmost column
5. Type `usbipd wsl attach --busid <busID>` and  replace the busID with the one from step 4. For example: 
```sh
usbipd wsl attach --busid 2-2
```

No output is good output:)

6. Run the command from step 4 again. The column with `USB to UART` should now say `attached`  
7. DO NOT close the command prompt

### Set up Minicom

1. Go back to Ubuntu an type `sudo apt-get install minicom`
2. Once its done, type `sudo minicom -s`
3. With the arrow keys, navigate to `serial port setup`
4. Press `a`
5. Your cursor is now in the first row and can type. Change `/dev/modem` to `/dev/ttyUSB0` (the last character is a zero)
6. Press `Enter`
7. Press `f`
8. You are now in the line that mentions hardware flow control. It should be set to NO.
9. Press `Enter` again.
10. With the arrow keys, navigate to `Save setup as dfl` and press enter. 
11. With the arrow keys, navigate to `Exit from Minicom` and press enter again.

You should be back at the command line. 

### Start Minicom

1. Type `sudo minicom -D /dev/ttyUSB0` (the last character is a zero). You should see a screen saying `Welcome to Minicom`. 
2. Quadruple check if you have attached the cables correctly. **Connecting the cables in any other way could break the device.**
3. Attach the power cable to your nvidia device. You should see something that makes you feel like you are hacking in a movie. 
4. Once you see a login prompt, use `nvidia` as both the login and the password. The password will not be visible when you type it, but the login should be. 

You should now be on the command line again, but this time its the command line of the nvidia device. 

:confetti_ball: YOU DID IT! :confetti_ball: 

## Mac OS
### Download and Install VCP drivers

Go to [https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

![vcp drivers](vcp.png)

Download and follow the installation instructions.

### Serial communication program

1. Install brew with the command below: 
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install minicom by typing `brew install minicom` in your command line.

### Set up Minicom

1. Once its done, type `sudo minicom -s`
2. With the arrow keys, navigate to `serial port setup` 
3. Press `a`
4. Your cursor is now in the first row and can type. Change `/dev/modem` to `/dev/tty.SLAB_USBtoUART`, the last character is a zero.
5. Press `Enter`
6. Press `f`
7. You are now in the line that mentions hardware flow control. It should be set to NO.
8. Press `Enter` again.
9. With the arrow keys, navigate to `Save setup as dfl` and press enter. 
10. With the arrow keys, navigate to `Exit from Minicom` and press enter again.

You should be back at the command line. 

### Start Minicom

1. Type `sudo minicom -D /dev/tty.SLAB_USBtoUART`, the last character is a zero. You should see a screen saying `Welcome to Minicom`. 
2. Quadruple check if you have attached the cables correctly to the nvidia device. **Connecting them any other way could break the device.**
3. Attach the power cable to your nvidia device. You should see something that makes you feel like you are hacking in a movie. 
4. Once you see a login prompt, use `nvidia` as both the login and the password. The password will not be visible when you type it, but the login should be. 

You should now be on the command line again, but this time its the command line of the nvidia device. 

:confetti_ball: YOU DID IT! :confetti_ball: 

## Trouble shooting

---

:x: **Error:** `usbipd is not recognized as a command`

:white_check_mark: **Solution:**
1. Install usipd (again) like [here](#install-busipd)
2. Close and re-open the command line and continue. 

---

:x: **Error:** The installation of linux tools is not working

:white_check_mark: **Solution:** Check if your Ubuntu version is correct like [here](#check-your-ubuntu-version)

---

:x: **Error:** In the nvidia command line you see something mentioning 'Finish the nvidia conifguration...'

:white_check_mark: **Solution:** Give the device to an instructor. 

---

:x: **Error:** You don't get the `Welcome to Minicom` screen for some reason. 

:white_check_mark: **Solution:** Try opening Minicom with `sudo minicom -s` and then pressing `esc`. 

---

:x: **Error:** usbipd error: WSL 'usbipd' error client not correctly installed. 

:white_check_mark: **Solution:** Install linux tools like [here](#install/update-necessary-packages)

---

:x: **Error:** The wsl distribution is not running.

:white_check_mark: **Solution:** WSL has to be open in the background. So, open it.

---

:x: **Error:** Nothing happens after you connect the power cable to the device. 

:white_check_mark: **Solution:** Check if you connected the cables correctly, see [this instruction](#connecting-jetson-nano-to-your-device). 

---

:x: **Error:** Your keyboard input is not recognized when you try to login.  

:white_check_mark: **Solution:** Check your hardware control flow settings (should be set to NO) from [this step](#-set-up-minicom).



## Authors:
[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilesh)
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna)


