import os
import requests
import json
import subprocess

def update_cve_database():
    url = "https://cve.circl.lu/api/last"
    response = requests.get(url)
    cve_data = json.loads(response.text)
    return cve_data

def information_gathering(target):
    print("Information Gathering")
    subprocess.run(["whois", target])
    subprocess.run(["nslookup", target])
    subprocess.run(["dig", target])

def reconnaissance(target):
    print("Reconnaissance")
    subprocess.run(["nmap", "-sV", "-O", target])
    subprocess.run(["nikto", "-h", target])

def discovery_and_scanning(target):
    print("Discovery and Scanning")
    subprocess.run(["nmap", "-p-", "-sS", "-sV", "-sC", "-oA", "scan_results", target])

def vulnerability_assessment(target, cve_data):
    print("Vulnerability Assessment")
    for cve in cve_data:
        cve_id = cve["id"]
        cve_description = cve["summary"]
        print(f"Checking for {cve_id}: {cve_description}")
        subprocess.run(["nmap", "--script", "vulners", "--script-args", f"vulners.cve={cve_id}", target])

def exploitation(target, cve_data):
    print("Exploitation")
    for cve in cve_data:
        cve_id = cve["id"]
        cve_exploit = cve.get("exploit", "")
        if cve_exploit:
            print(f"Exploiting {cve_id} using {cve_exploit}")
            subprocess.run(["python", cve_exploit, target])

def final_analysis_and_review():
    print("Final Analysis and Review")
    print("Reviewing scan results...")
    with open("scan_results.nmap", "r") as file:
        scan_results = file.read()
        print(scan_results)

def utilize_testing_results():
    print("Utilize the Testing Results")
    print("Generating report...")
    subprocess.run(["python", "generate_report.py"])

def main():
    target = input("Enter the target IP address or domain: ")
    cve_data = update_cve_database()

    information_gathering(target)
    reconnaissance(target)
    discovery_and_scanning(target)
    vulnerability_assessment(target, cve_data)
    exploitation(target, cve_data)
    final_analysis_and_review()
    utilize_testing_results()

if __name__ == "__main__":
    main()
