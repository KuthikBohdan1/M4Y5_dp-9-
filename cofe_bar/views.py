from django.shortcuts import render
from cofe_bar.models import Review
def Reviews(request):

    review = Review.objects.all()

    context = {
        "all_review": review
    }

    return render(
        context=context
        template_name="index.html"
    )