import PyPDF2

def extract_links(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            annotations = page.get('/Annots')
            if annotations:
                for annotation in annotations:
                    annotation_object = annotation.get_object()
                    if '/A' in annotation_object:
                        action = annotation_object['/A']
                        if '/URI' in action:
                            uri = action['/URI']
                            print(f"Page {page_num + 1}: {uri}")
            
            # Extract GoTo links
            destinations = page.get('/Dests')
            if destinations:
                for dest_name, dest_value in destinations.items():
                    print(f"Page {page_num + 1}, GoTo Destination: {dest_name}, Value: {dest_value}")

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = 'C:\\Program Files\\Axion BioSystems, Inc\\AxIS Z\\AxISZUserGuide3.11.pdf'
extract_links(pdf_path)
