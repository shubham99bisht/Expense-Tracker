## Unifynd Hackathon
Team Name: **GroupTwo**<br/>
Team Leader: Shubham Bisht

### **Problem Statement 2:** <br/>
*Extract neccessary information from bill/invoice* <br/>
&nbsp;    Step 1: Extracting all the text from given Invoice Image. (Text Region Detection, OCR) <br/>
&nbsp;    Step 2: Recognising Key information from the text like Store Name, Address, Total Amount etc using **Bi-directional LSTM based approach**

**Key Information Extraction from Scanned Receipts**: The aim of this task is to extract texts of a number of key fields from given receipts, and save the texts for each receipt image in a `json` file.

## Usage Guide

This repository contains our trials and solutions of three tasks. Inside each folder there are documentations of the method we adopted and guide of usage.

- **Task 1 - Scanned Receipt OCR**: Tesseract OCR
- **Task 2 - Key Information Extraction**: Character-wise classification with Bi-LSTM

### Approach

For the information extraction task, each image in the dataset is annotated with a text file with format shown below:
```json
{
  "company": "STARBUCKS STORE #10208",
  "address": "11302 EUCLID AVENUE, CLEVELAND, OH (216) 229-0749",
  "date": "14/03/2015",
  "invoice id":"5628391",
  "total": "4.95", 
  "items": "WhiteMochaV"
}
```

### Results

