## Python-Security-Log-Analysis
Security automation using Python to analyze authentication logs and detect suspicious failed login activity.

## Project Overview
This lab focused on using Python to automate basic log analysis tasks similar to those performed by a Security Operations Center (SOC) analyst. The goal was to parse authentication logs, identify repeated failed login attempts, and highlight suspicious IP addresses that could indicate brute-force activity.

The project demonstrates how scripting can support threat detection workflows by transforming raw log data into meaningful security insights.

---

## Project Execution

**1. Verify Python Installation & Setup Environment**

- Opened Command Prompt and verified Python installation.
- Created a structured project folder with Logs and Screenshots directories.

<img width="900" alt="Python Version Check" src="screenshots/01_python_version_check.png" />

<img width="900" alt="Project Folder Structure" src="screenshots/02-project_folder_structure.png" />

---

**2. Create Sample Authentication Logs**

- Created an authentication log file (`auth.log`) inside the Logs folder.
- Added login events including successful logins and multiple failed login attempts.
- These logs simulate authentication activity monitored by SOC analysts.

<img width="900" alt="Auth Log File Created" src="screenshots/03- auth_log_file_created.png" />

<img width="900" alt="Auth Log Content" src="screenshots/04-05_auth_log_content.png" />

---

**3. Develop Python Log Analyzer Script**

- Created a Python script called `log_analyzer.py`.
- The script performs the following actions:
  - Reads authentication logs line by line
  - Searches for "Failed login attempt" entries
  - Extracts IP addresses from log data
  - Counts repeated failures per IP
  - Flags suspicious activity when failures exceed a threshold

<img width="900" alt="Python Script File Created" src="screenshots/05-python_script_file_created.png" />

<img width="900" alt="Python Code Added" src="screenshots/06-python_code_added.png" />

---

**4. Execute Script & Analyze Output**

- Opened Command Prompt inside the project folder.
- Ran the Python script to analyze logs automatically.
- The script detected suspicious IP addresses with multiple failed login attempts.

<img width="900" alt="CMD Opened in Project Folder" src="screenshots/07-cmd_opened_in_project_folder.png" />

<img width="900" alt="Script Output" src="screenshots/08-script_output.png" />

---

## Skills Shown in this Lab

- Python scripting for cybersecurity automation
- Authentication log analysis
- Identifying brute-force style behaviour
- Basic detection logic implementation
- SOC-style investigation workflow

---

## Conclusion
This Python automation project provided hands-on experience with log analysis and security scripting. By developing a custom log analyzer, I learned how automation can assist SOC analysts in detecting suspicious authentication activity faster and more efficiently. The project demonstrates how even simple scripts can enhance threat detection processes and reduce manual log review.
