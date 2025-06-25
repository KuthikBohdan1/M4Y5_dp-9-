from django.shortcuts import render
from cofe_bar.models import Review
def Reviews(request):

    review = Review.objects.all()

    context = {
        "all_review": review
    }

    return render(
        request,
        template_name="index.html",
        context=context,
    )
    