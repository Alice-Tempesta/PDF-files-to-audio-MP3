from gtts import gTTS  # Google Text-to-Speech library for converting text to speech
from art import tprint  # ASCII art text printing library for displaying program title
import pdfplumber  # Library for extracting text and information from PDF files
from pathlib import Path  # Library for working with file paths


def pdf_to_mp3(file_path='test.pdf', language='ru'):
    try:
        # Check if the file exists and has a .pdf extension
        if not Path(file_path).is_file() or Path(file_path).suffix.lower() != '.pdf':
            raise ValueError("The file doesn't exist or has an invalid format. Check the file path and extension.")

        # Display the original file name
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        # Extract text from each page of the PDF
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        # Concatenate text from all pages and remove newline characters
        text = ''.join(pages)
        text = text.replace('\n', '')

        # Convert text to speech using gTTS
        my_audio = gTTS(text=text, lang=language, slow=False)

        # Generate the output file name based on the original file name
        file_name = Path(file_path).stem

        # Save the MP3 file in the same directory as the original PDF
        output_path = Path(file_path).parent / f'{file_name}.mp3'
        my_audio.save(output_path)

        # Display success message with the saved file path
        return f'[+] {output_path} saved successfully!\n---Have a good day!---'

    except pdfplumber.PDFSyntaxError as e:
        return f"Error reading PDF: {e}"

    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    try:
        # Display the program title using ASCII art
        tprint('PDF>>TO>>MP3', font='bulbhead')

        # Get user input for the file path and language
        file_path = input("\nEnter a file's path: ").strip()
        if not file_path:
            raise ValueError("File path cannot be empty.")

        language = input("Choose language, for example 'en' or 'ru': ").strip()
        while language not in ("en", "ru"):
            language = input("Choose language, for example 'en' or 'ru': ").strip()

        # Call the pdf_to_mp3 function with user inputs
        print(pdf_to_mp3(file_path=file_path, language=language))

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == '__main__':
    # Run the main function when the script is executed
    main()
