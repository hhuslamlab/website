# Working on HPC

# HPC 101

## Table of Contents
- [Logging into HPC and requesting jobs](#Intro)
    - [Option 1: One line](#o1)
    - [Option 2: Shell script](#o2)
- [Setting the stage for your project](#prep)
    - [Loading available modules](#load)
    - [Installing new modules](#install)
- [Errors that I have encountered and how I solved them](#errors)
- [Mounting filesystems](#files)
- [More Help](#help)

## Logging into HPC and requesting a job <a name="Intro"></a>
First, you need to connect your VPN (even if you are on campus). If you don't know how to do it or have not set up a VPN you can go [here](https://wiki.hhu.de/display/OPENVPN/OpenVPN) for instructions.

Second, you need to use SSH to connect to HPC (read more [here](https://en.wikipedia.org/wiki/Secure_Shell). Type the below command in your command line, replacing `<Nutzerkennung>` with your own. This is the same name you use to log into Illias, Hislsf etc.
```shell
ssh <Nutzerkennung>@hpc.rz.uni-duesseldorf.de

```

Now you are on the login node. It is not allowed to do computations here, so we need to start a job request.

Below are example allocations. Feel free to change the requested ressources as needed for your project.
Note that you can only request a job for a project if you are a member of that project. See [this link](https://www.zim.hhu.de/forschung/high-performance-computing/antrag) for a form for applying for membership in a project or starting a new one.

There are two options for starting a job request.

**Option 1:**<a name="o1"></a>
The below command requests a job with 10 cores, 10GB Ram und (the maximum) 4 hours walltime for the project called 'informativity'.
```shell
qsub -A Projekt -I -l select=1:ncpus=10:mem=10G -l walltime=3:59:00
```
---
**Keyword explanation:**
- `select` is the number of compute nodes
- `ncpus` is the number of GPUs
- `mem` is the RAM size
- `ngpus` is the number of GPUs
- `PBS` is the Portable Batch System. Read more [here](https://en.wikipedia.org/wiki/Portable_Batch_system)
---

**Option 2:**<a name="o2"></a>
Create a shell script.
```bash
vi job.sh
```
Once you enter the shell script, press `i` for `insert mode`.
```bash
#!/bin/bash
#PBS -l select=1;ncpus=8,mem=128G
#PBS -l walltime=3:59:00
#PBS -A informativity
```
Submit the job with:

```bash
qsub -I job.sh
```

Depending on the ressources that you allocated, how many other people are currently in the cue and other factors, you will have to for your job to start. This can take a minute or several hours, but it will happen eventually.


## Setting the stage for your project <a name="prep"></a>
Now that your job has started you can get to setting up the environment for you project. Depending on what you are doing, you can skip some steps.

### Loading available modules <a name="load"></a>
With the command `module avail` you can see a list of modules and their versions that are available on hpc. You can load those modules with `module load`.
You can load a specific version of a module, should it be available on hpc, by specifying it in the statement.
```sh
module load Python/3.8.3
```

### Installing modules <a name="install"></a>
You can install new packages with the command below.
```sh
PIP_CONFIG_FILE=/software/python/pip.conf pip install --user xarray
```
In this example, the package "xarray" is being installed, substitute it with the package that you need.

Should you run into an error, you can try the following things:
1. **The installation takes ages and nothing seems to be happening:**
    Stop the command with `Ctr` + `c` and run the command again (Press the up arrow once, then `enter`)
2. **"Something" is missing:**
 Run the same command with the package that is missing. Then run the previous command again. If the error appears again with something else that is missing, rinse and repeat

## Common errors and how you might solve them <a name="errors"></a>
As the heading implies, this is part is highly individual in terms of both the problems and the solutions.

**Error 1: Something using cPython is not working as intended**

Potential solution: Use `module load intel/openAPI_2021.4.0` to load the intel c compiler, which apparently is not done automatically. Optionally, check if `setuptool`and `pydevtools`are available AND loaded.

## Mounting files systems <a name="files"></a>

For copying files from your local machine to HPC, you need to mount your device on HPC.
Install sshfs:
```bash
sudo apt install sshfs
```

Navigate to the root directory and create the folder you want
```bash
cd /mnt
mkdir foldername
```

Mount your file system: Replace `nutzerkennung` with your Nutzerkennung and the `foldername` with the name that you chose in the last step.

```bash
sudo sshfs nutzerkennung@storage.hpc.rz.uni-duesseldorf.de:/gpfs/project/nutzerkennung /mnt/foldername
```
Copy your files to the directory to make them available on hpc.
To access your files on hpc your need to navigate to the General Parallel File System (gpfs) on hpc.
Log into your hpc and enter (replace `Nutzerkennung` with your one).

```bash
cd gpfs/project/nutzerkennung
```


Read more about mounting [here](https://man7.org/linux/man-pages/man8/mount.8.html) or go through the guide [here](https://wki.hhu.de/viewpage.action?pageId=5572564).

## More help<a name="help"></a>
Anything that is not covered in here might be covered in one of the links below, have a look:

- [The official HHU HPC doc](https://wiki.hhu.de/display/HPC/Wissenschaftliches+Hochleistungs-Rechnen+am+ZIM)
- [This guide](https://github.com/black0017/slurm-hpc-survival-guide) on GitHub by Nikolas Adaloglou and Julius Ramarkes explains extra useful stuff specific to the HHU HPC

If none of this works for you, you can contact one of the authors.

### Authors
[**Anna Stein**](https://slam.phil.hhu.de/authors/anna/)
[**Akhilesh Kakolu Ramarao**](https://slam.phil.hhu.de/authors/akhilseh/)
