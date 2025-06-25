from rest_framework.views import APIView
from rest_framework.response import Response
import django_rq
from .emails import send_contact_email


class ContactEmailView(APIView):
    """
    View to handle contact email submissions.
    """
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to submit contact emails.
        """
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        message = request.data.get('text')

        if not all([name, email, phone, message]):
            return Response({"error": "All fields are required"}, status=400)

        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(send_contact_email, name, email, phone, message)
        return Response({"message": "Contact email submitted succesfuly"}, status=201)


class ProjectEmailView(APIView):
    """
    View to handle project email submissions.
    """
    pass
