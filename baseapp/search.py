from post.models import Post, PropertyType, OfferType


def check_for_matches(property_type, offer_type, location, minimum_price, maximum_price):
    result = []
    posts = Post.objects.all()
    property_type = PropertyType.objects.get(id=property_type)
    offer_type = OfferType.objects.get(id=offer_type)
    

    for post in posts:
        if post.property_type == property_type and post.offer_type == offer_type:
            result.append(post)

    if location != '':
        for post in result:
            if post.location.lower() != location.lower():
                result.remove(post)

    if minimum_price != '':
        for post in result:
            if post.price < int(minimum_price):
                result.remove(post)

    if maximum_price != '':
        for post in result:
            if post.price > int(maximum_price):
                result.remove(post)

    return result

def search(request):
    property_type = request.GET.get('property_type')
    offer_type = request.GET.get('offer_type')
    location = request.GET.get('location')
    minimum_price = request.GET.get('minimum_price')
    maximum_price = request.GET.get('maximum_price')
    posts = check_for_matches(property_type,
                             offer_type,
                             location,
                             minimum_price,
                             maximum_price)

    return posts