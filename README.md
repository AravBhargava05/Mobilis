# Mobilis LLC
### A website by Kyle Hanson, Arav Bhargava, and Antonia M. Salame

Welcome to our CS50 Final Project. For our final project, we chose to create a website for Mobilis LLC, a prosthetics startup founded by one of our group members (Arav). This README will explain how to compile, use, and run our project.

In the future, we plan to link this code with an actual website domain. For now, this code is hosted in the `mobilis` folder we have been working on. Below are the steps for running this project:

---

## How to Run the Project

1. **Download the Code**
   - The folder containing our website is called `mobilis`. Download this folder (submitted as a zip file) onto your computer.

2. **Open the CS50 Codespace**
   - Use the CS50 codespace hosted at [CS50.dev](https://cs50.dev) (the Visual Studio Code environment used in CS50).

3. **Navigate to the Project Folder**
   - Run the following command in your terminal:
     ```bash
     cd mobilis
     ```
   - Your terminal should now look like this:
     ```bash
     mobilis/ $
     ```

4. **Run the Flask Server**
   - Run the following command in your terminal:
     ```bash
     flask run
     ```
   - A popup should appear with a message like:
     ```
     Your application running on port 5000 is available
     ```
     - The popup will include a button labeled **Open in Browser**. Click this button.

5. **Explore the Website**
   - You should now be on the homepage of our website, Mobilis!

---

## Website Navigation

Our website is designed to be straightforward and user-friendly. After following the steps above, you will arrive at our homepage. The website includes a **Navbar** with the following pages:
- **Home**
- **The Problem**
- **Our Product**
- **The Team**
- **Contact Us**

Use the navbar to navigate between these pages. Alternatively, you can scroll down on the homepage to learn more about Mobilis, its product, and click a button to **Get Involved** to contact the Mobilis team and learn how you can help.

---

## Key Features

### **Interactive Map**
- Navigate to the **The Problem** page via the navbar.
- On this page, you will find an **Interactive Map**.
  - To use the map, click on one of the countries outlined/highlighted in red.
  - Information about the number/status of amputees in that country will be displayed.

- A red button labeled **Discover Our Product** on this page will take you to the **Our Product** page, which can also be accessed via the navbar.

### **Model Calculator**
- On the **Our Product** page, scroll to the section titled **Model Calculator**.
- This feature is designed for patients:
  - Input your residual limb length (in cm) and hit **Calculate**.
  - The website will output a suggestion for what model you should use, e.g., *"Your Model: 3.1."*

---

## Final Notes

The website is designed to be intuitive and accessible, requiring no technical experience to navigate or use. We hope you find it helpful and easy to explore!
