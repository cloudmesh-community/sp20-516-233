# Hyper-V on Microsoft Windows 10 (Pro, EDU, Home) :o2: sp20-516-233 Holly Zhang

## Hyper-V Concepts
Hyper-V is a [@www-microsoft-overview].


## Hyper-V management from CMD.EXE

### Enable Hyper-V from CMD.EXE

To enable Hyper-V from Command Prompt, first start Command Prompt as 
Administrator. On the command line, enter the following command:

```bash
$ DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

### Disable Hyper-V from CMD.EXE

Open Command Prompt as Administrator and enter the following command:

```bash
$ 
```
 
## Hyper-V management from Powershell

### Enable Hyper-V

First start Powershell as Administrator. There are two ways to enable Hyper-V 
from Powershell. Only choose one of the the following commands. 

Run the following command:
 
```bash
$ Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

**OR** run this following command:

```bash
$ DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

### Disable Hyper-V

To disable Hyper-V, start Powershell as Administrator and then enter the 
following command:

```bash
$ Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor 
``` 

## Multipass Benchmark

### Windows 10 Pro and EDU

After enabling Hyper-V as shown in the previous section, Multipass can be now be 
downloaded from <https://multipass.run/>. Find the download button for Windows 
and press it to obtain the executable file. Then run the executable file to 
install Multipass.  

### Windows 10 Home

Installation of Multipass on Windows 10 Home requires Virtualbox. Although 
possible, this way has multiple steps compared to the installation on Windows 10 
Pro or EDU. The following two subsections show how to prepare the installation 
for Virtualbox on Windows Home or how to upgrade to Windows 10 Pro or EDU. 

#### Virtualbox Installation

Before installing Virtualbox, make sure that Hyper-V has been disabled. The 
previous section includes commands to disable Hyper-V. Once Hyper-V is disabled, 
Virtualbox can be installed at <https://www.virtualbox.org/wiki/Downloads>.

#### Upgrade Windows 10 Home to Windows 10 Pro or EDU

For those who already have a Windows operating system but not Windows 10 Pro or 
EDU, downloading the Windows installer can be skipped. What is needed instead is 
a product key. When getting the product key, choose the 64-bit OS. A product key 
for Windows 10 Pro 64-bit can be obtained at 
<https://www.microsoft.com/en-us/store/b/windows?activetab=tab:shopwindows10>. 
Windows 10 EDU 64-bit is provided free of charge for 
Indiana University students at <https://iuware.iu.edu/Windows/Title/2977>.

Once the product key is obtained, navigate to the 
