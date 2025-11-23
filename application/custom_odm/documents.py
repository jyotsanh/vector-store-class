from nosql.base import CustomODM


class UserDocument(CustomODM):
    first_name:str
    last_name:str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Settings:
        name = "users"


class PdfDocument(CustomODM):
    pdf_name:str
    pdf_size:str

    class Settings:
        name = "pdf_documents"


filters = {
    "pdf_name":"heheh",
    "pdf_size":"122"
}

pdf1 = PdfDocument(**filters)
pdf1.save() 

