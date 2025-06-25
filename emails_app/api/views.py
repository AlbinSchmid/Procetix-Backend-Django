from rest_framework.views import APIView
from rest_framework.response import Response
import django_rq
from .emails import send_contact_email
from .utils import extract_optional_fiels


class ContactEmailView(APIView):
    """
    View to handle contact email submissions.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to submit contact emails.
        """
        data = {
            "name": request.data.get('name'),
            "email": request.data.get('email'),
            "phone": request.data.get('phone'),
            "message": request.data.get('text')
        }
        data.update(extract_optional_fiels(request))
        if not all([data.get("name"), data.get("email"), data.get("phone"), data.get("message"),]):
            return Response({"error": "One or more required fields are missing"}, status=400)

        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(send_contact_email, data)
        return Response({"message": "Emails send correctly"}, status=200)
