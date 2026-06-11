from datetime import date

from relacionesunoamuchos import renderers


def pdf_view(request):

    data = {
        "pdf_title": "Laboratorio Django",
        "invoice_number": "001",
        "customer_name": "Diego Cervantes",
        "amount": "100.00",
        "date": date.today(),
    }

    return renderers.render_to_pdf(
        "pdfs/invoice.html",
        data
    )