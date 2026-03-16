# Selenium Python File Upload & Download Automation Framework

This project demonstrates an **automation testing framework built using Python, Selenium WebDriver, and PyTest**.
It automates file upload and file download functionality and generates test execution reports.

---

## 🚀 Features

* File Upload Automation
* File Download Automation
* Page Object Model (POM) design pattern
* Screenshot capture on test failure
* HTML Test Reports using pytest-html
* Custom Chrome download directory
* WebDriver Manager integration
* GitHub CI/CD pipeline for automated test execution

---

## 🛠 Tech Stack

* Python
* Selenium WebDriver
* PyTest
* WebDriver Manager
* GitHub Actions

---

## 📁 Project Structure

```
selenium-python-file-automation
│
├── pages
│   ├── upload_page.py
│   └── download_page.py
│
├── tests
│   ├── test_upload.py
│   └── test_download.py
│
├── utils
│   ├── driver_setup.py
│   └── screenshot.py
│
├── downloads
├── screenshots
├── testdata
│   └── sample.txt
│
├── requirements.txt
└── README.md
```

---

## ▶ How to Run Tests

### Install dependencies

```
pip install -r requirements.txt
```

### Run automation tests

```
pytest
```

### Generate HTML test report

```
pytest --html=report.html
```

---

## 📊 Test Report

The framework generates an **HTML report** after execution showing:

* Test results
* Execution time
* Pass/Fail summary

---

## 👨‍💻 Author

**Prajwal Joshi**
