## GoFile Uploader with Keyboard Navigation

This Python script provides a user-friendly way to upload files to the GoFile service using keyboard shortcuts. It features:

* **File selection:** Choose multiple files using the file dialog.
* **Server selection:** Automatically attempts to retrieve the best server for uploading.
* **Upload status:** Displays success or failure messages for each file.
* **Download links:** Presents download links for successfully uploaded files.
* **Keyboard navigation:** Use the up and down arrow keys to select options and Enter to confirm.
* **Clear interface:** Optionally hides the main window for a cleaner interface.
* **Color highlighting:** Uses colorama for visually distinct output messages.

### Installation

1. **Install required libraries:**

   ```bash
   pip install tkinter requests colorama
   ```

2. **Save the script as `gofile_uploader.py`.**

### Usage

1. **Run the script:**

   ```bash
   python gofile_uploader.py
   ```

2. **Navigate:**
   - Use the **up** and **down** arrow keys to select options.
   - Press **Enter** to choose an option.

3. **Upload:**
   - Select "Start uploading" and choose files using the file dialog.
   - The script will upload the selected files and display success/failure messages.

4. **Exit:**
   - Select "Leave the tool" and press **Enter**.


### Notes

* This script utilizes the GoFile API for file uploading. Refer to GoFile's documentation for service details and terms of use.
* This script is provided for educational purposes only. Use it responsibly and in accordance with GoFile's policies.



### Additional Information:

- This script uses the `tkinter` library for the graphical user interface.
- The `requests` library handles communication with the GoFile API.
- The `colorama` library provides colored output messages for better readability.
- The `keyboard` library enables keyboard interaction for navigating the menu.
- The `mimetypes` library helps determine the MIME type of files.
