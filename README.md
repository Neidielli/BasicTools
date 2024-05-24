# 🔧 BasicTools

This repository contains a collection of basic tools for hackers, designed to assist in various tasks such as port scanning and DNS enumeration. These tools are written in Python and can be easily utilized for security testing and exploration purposes.

## Tools Included:

### 🛠️ 1. Port Scanner (portscan.py)

This tool allows you to scan a target host for open ports within a predefined list of common ports. By specifying a target IP address, it checks each port in the list and reports whether it's open or closed.

#### Usage:
```bash
python portscan.py
```

Remember to replace "localhost" with your desired target domain in the script before running it.

### 🔍 2. DNS Brute Forcer (dnsbrute.py)

This tool performs DNS enumeration by brute-forcing subdomains of a specified domain. It requires a wordlist containing potential subdomains commonly used for brute-forcing. Ensure you have a wordlist of common subdomains on your machine before running this tool. If successful, it prints the subdomain along with its corresponding IP address.

#### Usage:
```bash
python dnsbrute.py
```

Remember to replace "localhost" with your desired target domain in the script before running it.

## ℹ️ Pre requisites:

- Python 3.x
- Libraries:
  - socket (for port scanning)
  - dns.resolver (for DNS enumeration)
  - worldlist (for DNS enumeration)

## 🚀 Getting Started:

1. Clone this repository:
   ```bash
   git clone https://github.com/Neidielli/BasicTools.git
   ```

2. Navigate to the cloned directory:
   ```bash
   cd BasicTools
   ```

## 🤝 Contributions:

Contributions are welcome! If you have any improvements or additional tools you'd like to add, feel free to fork this repository and submit a pull request.

## 📢 Disclaimer:

These tools are intended for educational and ethical use only. Any misuse or illegal activities performed using these tools are not the responsibility of the authors or contributors.
