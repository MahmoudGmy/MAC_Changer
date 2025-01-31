# 🔧 MAC Address Changer Tool  

## 📜 Description  
This Python tool allows you to easily change the **MAC address** of a network interface on a Linux-based system. It provides functionality to:
- Retrieve the current MAC address of a specified network interface.
- Change the MAC address to a user-defined value.

**Note:** Changing MAC addresses can help you maintain privacy or test network-related applications. This tool is for educational and ethical use only.

---

## 🚀 Features  
- Change the MAC address of any network interface.
- Automatically retrieves the current MAC address of the specified interface.
- Simple to use through command-line arguments.

---

## 🛠️ Prerequisites  
Before using this tool, ensure you have:
- **Python 3.x** installed
- **Root/Administrator privileges** (required to change network configurations)
  
This script is designed to work on **Linux**-based systems (like Ubuntu, Kali Linux, etc.).

---

---

## 🎯 Usage  

### **1. Running the Tool**

The script requires two arguments:
- **`-i` or `--interface`**: The network interface whose MAC address you want to change.
- **`-m` or `--mac`**: The new MAC address.

#### **Example Usage:**  
```bash
sudo python3 change_mac.py -i eth0 -m 00:11:22:33:44:55
