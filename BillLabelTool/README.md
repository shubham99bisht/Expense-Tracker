## Bill Label Tool

This folder contains tool for efficiently hand labelling various entity in Invoices.
**This step works after OCR** i.e it requires all the text to be extracted from the invoice images.

Here's a demo on how we can efficiently label large dataset quickly!

![](Media/demo_BillLabel.gif)


Steps:

1. Extract all the text and store the .txt files in /data folder. (It is assumed that all files are named sequentially starting from 1)
2. Run
    `$python3 preprocess.py` 
3. Start Flask server to start Labelling:
    ```
        $export FLASK_APP=server.py
        $flask run
        
        
        Visit: 127.0.0.1:5000/index/1 to start Labelling
     ```
