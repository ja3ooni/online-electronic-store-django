from django.http.response import HttpResponseRedirect
from django.contrib import messages
from shop.models import Review

def postreview(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    if request.method == "POST":
        subject = request.POST['subject']
        review = request.POST['review']
        rating = request.POST['rating']

        product_review = Review(
            product_id = prid,
            user_id = current_user.id,
            subject = subject,
            review = review,
            rating = rating,
        )
        product_review.save()

        messages.success(request, "Review Posted")
        return HttpResponseRedirect(url)