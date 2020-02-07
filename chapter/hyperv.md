# Hyper-V on Microsoft Windows 10 (Pro, EDU, Home) :o2: sp20-516-233 Holly Zhang

## Hyper-V Concepts



## Hyper-V management from CMD.EXE

To enable Hyper-V from Command Prompt, first start Command Prompt as 
Administrator. On the command line, enter the following command:

```bash
$ DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

## Hyper-V management from Powershell

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

## Multipass Benchmark

### Windows 10 Pro and EDU

After enabling Hyper-V, Multipass can be downloaded from  
<https://multipass.run/>. Find the download button for Windows and press it to 
obtain the executable file. Then run the executable file to install Multipass.  

### Windows 10 Home

Installation of Multipass on Windows 10 Home requires Virtualbox. Although 
possible, this way has multiple steps compared to the installation on Windows 10 
Pro or EDU. The following two subsections show how to either install Virtualbox 
and Multipass on Windows Home or how to upgrade to Windows 10 Pro or EDU. 

#### Virtualbox Installation

Virtualbox can be installed at <https://www.virtualbox.org/wiki/Downloads>.

#### Upgrade Windows 10 Home to Windows 10 Pro or EDU

