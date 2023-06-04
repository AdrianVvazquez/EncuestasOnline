from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F

from .models import Choice, Question

class IndexView(generic.ListView):
    # Default: <app name>/<model name>_list.html
    template_name = "todoDB/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # return the latest 5 poll questions in the system, according to publication date
        return Question.objects.order_by("-pub_date")[:5]

# Recibir id de pregunta y mostrar formulario
class DetailView(generic.DetailView):
    model = Question
    template_name = "todoDB/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    # Default: <app name>/<model name>_detail.html
    template_name = "todoDB/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay form
        return render(
            request,
            "todoDB/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.refresh_from_db()
        selected_choice.votes = F("votes")+1  # Avoiding race conditions 
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("encuestas:results", args=(question.id,)))
