# A brief introduction and usage of HPC

You can only login to a HPC server using SSH protocol. 

## Running

### Login

Read more on SSH here < https://en.wikipedia.org/wiki/Secure_Shell >.

```
ssh <Nutzerkürzel>@hpc.rz.uni-duesseldorf.de
```

Here the `Nutzerkürzel` is your Unikennung.

With the above command, you will enter the login shell.

### HPC allocation


To get the computing power of your needs, you need to create a shell script something like below --

Creating and opening the shell script
```
vi job.sh
```

Once you enter the shell script, press `i` for `insert mode`, here's an example script --

```
#!/bin/bash
#PBS -l select=1;ncpus=8;mem=128G
#PBS -l walltime=13:59:00
#PBS -A informativity
```

Keywords:

- `select` is the number of compute nodes (NOTE: just keep this value as 1)
- `ncpus` is the number of CPUs
- `ngpus` is the number of GPUs
- `mem` is the RAM size
- `PBS` is the Portable Batch System. Read more here: < https://en.wikipedia.org/wiki/Portable_Batch_System >
- `walltime` is the time for which the HPC instance is active
- `informativity` is the name of the project

Press `esc` and `:wq` to save and quit the file.

### Activate the HPC shell

```
qsub -I job.sh
```

`qsub` submits the job to PBS

You need to wait till the machine is assigned.

### Mount devices

For copying the files from the your local machine to HPC, you need to mount your device on HPC.

Read more about [Mount](https://man7.org/linux/man-pages/man8/mount.8.html)

Go through the guide here < https://wiki.hhu.de/pages/viewpage.action?pageId=55725648 > for more details.


For a detailed guide consider -- https://docs.google.com/document/d/1C7EfX_I1TLYUOMxvxSzxTukBfh53JipeSJG_XuixzOo/edit

