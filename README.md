

# Automated Penetration Testing Script

This project is a Python-based automated penetration testing tool designed to streamline the process of assessing the security of a target system. The script performs various tasks, including information gathering, reconnaissance, discovery and scanning, vulnerability assessment, exploitation, and final analysis. It integrates multiple tools to automate the scanning and testing process, making it easier for security professionals to identify and exploit vulnerabilities.

## Features

- **Update CVE Database**: Fetches the latest Common Vulnerabilities and Exposures (CVE) from an API for use in vulnerability assessment.
- **Information Gathering**: Collects basic information about the target using tools like `whois`, `nslookup`, `dig`, and `fierce`.
- **Reconnaissance**: Uses `nmap` and `nikto` to discover services and potential vulnerabilities.
- **Discovery and Scanning**: Performs a full port scan using `nmap` and a directory brute-force attack using `dirb`.
- **Vulnerability Assessment**: Evaluates the target against known CVEs using `nmap` scripts and performs an OWASP ZAP scan.
- **Exploitation**: Attempts to exploit discovered vulnerabilities using `msfconsole` and brute-force attacks with `hydra`.
- **Final Analysis and Review**: Reviews the collected data, analyzes open ports and services, and summarizes the findings.
- **Report Generation**: Compiles the results into a comprehensive report for further analysis.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup4` library
- `subprocess` library
- Various external tools like `whois`, `nslookup`, `dig`, `fierce`, `nmap`, `nikto`, `dirb`, `msfconsole`, `hydra`, and `zap-cli`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/automated-penetration-testing.git
    cd automated-penetration-testing
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that all the external tools (`whois`, `nmap`, etc.) are installed and accessible in your system's PATH.

## Usage

1. Run the script:
    ```bash
    python script_name.py
    ```

2. Enter the target IP address or domain when prompted.

3. The script will automatically perform the following tasks:

    ### Step 1: Update CVE Database
    - Fetches the latest CVE data from an external API.

    ### Step 2: Information Gathering
    - Executes `whois`, `nslookup`, `dig`, and `fierce` to gather basic information about the target.

    ### Step 3: Reconnaissance
    - Uses `nmap` to detect open ports and services, and `nikto` to identify vulnerabilities in web applications.

    ### Step 4: Discovery and Scanning
    - Performs a comprehensive port scan using `nmap` and directory enumeration using `dirb`.

    ### Step 5: Vulnerability Assessment
    - Cross-references open services with known CVEs using `nmap` scripts and performs a web application security scan with OWASP ZAP.

    ### Step 6: Exploitation
    - Attempts to exploit identified vulnerabilities using `msfconsole` and performs brute-force login attacks with `hydra`.

    ### Step 7: Final Analysis and Review
    - Analyzes and reviews the collected data, summarizing the results.

    ### Step 8: Utilize the Testing Results
    - Generates a detailed report of the findings, including all steps taken and vulnerabilities discovered.

## Report

The script generates a report summarizing the results of the penetration test. This report is stored in the `reports` directory.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
