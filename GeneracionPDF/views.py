from datetime 
import datetime
from relacionesunoamuchos import renderers


def pdf_view(request):

    invoice_number = "001"

    context = {
        "customer_name": "Diego Cervantes",
        "invoice_number": invoice_number,
        "amount": "100.00",
        "date": datetime.date.today(),
        "pdf_title": f"Laboratorio #{invoice_number}",
    }

    response = renderers.render_to_pdf(
        "pdfs/invoice.html",
        context
    )

    filename = f"Laboratorio_{invoice_number}.pdf"

    content = f"inline; filename={filename}"

    download = request.GET.get("download")

    if download:
        content = f"attachment; filename={filename}"

    response["Content-Disposition"] = content

    return response