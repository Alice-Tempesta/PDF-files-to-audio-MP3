# PDF to MP3 Converter

## Project Description:
This project is a converter for PDF files to MP3 audio files. It utilizes the gTTS library for text-to-speech conversion and pdfplumber for extracting text from PDF files. The project is written in the Python programming language and provides a simple command-line interface for users.

## Usage Instructions:

1. **Install Dependencies:**
   Ensure that all necessary dependencies are installed. You can install them by executing the following command in your terminal or command prompt:
<br>```pip install gtts art pdfplumber```<br/>

3. **Clone the Repository:**
   Clone the repository to your computer by executing the command:
   <br>```git clone git@github.com:Alice-Tempesta/PDF-files-to-audio-MP3.git```<br/>

4. **Navigate to the Project Directory:**
   <br>```cd pdf-to-mp3```<br/>
   ```git checkout main -- pdf-to-mp3.py```

6. **Working with Files:**
   - **Uploading PDF File:**
     Place the PDF file you want to convert into the project directory.

7. **Run the Program:**
   Run the program by executing the following command:
   <br>```python pdf_to_mp3_converter.py```<br/>

8. **Input Data:**
   - Enter the name of the PDF file you want to convert (e.g., `example.pdf`).
   - Choose the language (e.g., 'en' for English or 'ru' for Russian).

9. **Wait for Results:**
   - The program will process the PDF file, extract text, and convert it into an MP3 audio file.
   - After completion, you will be notified of the location where your new audio file is saved.

10. **Locating the Output File:**
   - The MP3 audio file will be saved in the same directory as your original PDF file.
   - The new file will have the same base name as the original PDF but with the `.mp3` extension.

## Important Notes:
- Ensure that Python and pip are installed before starting.
- The project uses the gTTS, art, and pdfplumber libraries. Make sure they are installed before using the program.
