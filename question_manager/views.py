# from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from rest_framework.response import Response
from django.http import JsonResponse

from question_manager.openai_integration.openai_integration import generate_mcq
# Create your views here.


@require_http_methods(["POST"])
def generate_questionnaire(request):
    # try:
    request_payload = json.loads(request.body.decode('utf-8'))
    input_text = request_payload.get("input_text", None)
    if not input_text:
        raise Exception("No input text provided for generating questions")
    number_of_questions = request_payload.get("number_of_questions")
    question_set = generate_mcq(input_text, number_of_questions)
    return JsonResponse(question_set, safe=False)
    # except Exception as e:
    # return Response(f"Error occurred while generating questionnaire for input text: {e}", status=400)
