# Software

## Environment setup

## (only windows) 

``` 
#power shell
winget install marha.VcXsrv
```

### wsl setup

```
#power shell
wsl --install
```
### wsl usb setup
```
# powershell (administrator)
winget install --interactive --exact dorssel.usbipd-win
usbipd list
usbipd bind --busid 3-1
usbipd attach --wsl --busid 3-1 --auto-attach
```

```
# wsl
# check usb connectivity
lsusb
```

### after entering docker container
```
cd /colcon_ws/src/
colcon build
source install/setup.bash
```