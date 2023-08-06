# TPython
TPython a better python REPL.

## Features
- Built-in TimeIt, clear/cls
- Colors
- Update Notifier 
- Custom Config

## Future Updates
- Tab Completion

## Installation
```
$ pip install TPython
```

## Dependencies
```
colorama
jsonc_parser
requests
```

## Usage

### **Run**
```
$ tpy
```

### **Built-in Commands**
| Command | Function |
| :-------: | :--------: |
| version | tells version |
| exit/quit/close | exits the REPL |
| cls/clear | clears the terminal |
| timeit | tells execution time of code |

### **Config**

#### **Create File**
**Windows:**
```
> mkdir %USERPROFILE%\.TPython
> curl https://raw.githubusercontent.com/Techlord210/TPython/main/config.jsonc -o %USERPROFILE%\.TPython\config.jsonc
```
**Mac OS/Linux/BSD:**
```
$ mkdir ~/.TPython
$ curl https://raw.githubusercontent.com/Techlord210/TPython/main/config.jsonc -o ~/.TPython/config.jsonc
```

#### **Instructions**
- File location: `~/.config/TPython/config.jsonc`
- Read all the comments in config file.
- Do not remove/edit any keys from config file.
- Do not use uppercase in config file.
- Do not use Spaces in values of config file.