from fpdf import FPDF


class PDFCreator:

    @staticmethod
    def create_pdf_file(file_name: str, order_as_text: str):
        # save FPDF() class into a
        # variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)

        # create a cell
        pdf.cell(200, 10, txt="Lemos Test", ln=1, align='C')

        # add another cell
        pdf.cell(200, 10, txt=order_as_text, ln=2, align='C')

        # save the pdf with name .pdf
        pdf.output(f"./files_to_print/{file_name}.pdf")


PDFCreator.create_pdf_file(file_name="test1", order_as_text="bla bla bla")
