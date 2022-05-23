# Snaps on WSL2 (Ubuntu)

If at any point you encounter an error like this: 
`sudo: daemonize: command not found` it means you have to install the daemonize package. 
```shell
sudo apt-get install daemonize
```
Run the command that errored out again and it should work.

---


```bash
sudo apt-get update && sudo apt-get install -yqq daemonize dbus-user-session fontconfig
```

```bash
sudo daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
```

```bash
exec sudo nsenter -t $(pidof systemd) -a su - $LOGNAME
```

To check if the installation worked, run `snap version`. The output should look something like below:
```bash
snap    2.54.3+20.04.1ubuntu0.3
snapd   2.54.3+20.04.1ubuntu0.3
series  16
ubuntu  20.04
kernel  5.10.102.1-microsoft-standard-WSL2
```

## Sources
[This GitHub issue](https://github.com/microsoft/WSL/issues/5126)

## Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)


