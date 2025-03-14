from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import FileSerializer
import PyPDF2
import ollama

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            
            # Convert PDF to Text
            try:
                with open(file_instance.file.path, "rb") as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    text = "\n".join([page.extract_text() or "" for page in reader.pages])

                # Generate Draft with Ollama
                response = ollama.chat(model="mistral", messages=[{"role": "user", "content": text}])
                draft = response.get('message', {}).get('content', "Error generating draft")
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            return Response({"draft": draft})
        return Response(file_serializer.errors, status=400)
