# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse


# @api_view(['GET'])
# def api_root(request, format=None):
#     response = Response({
#         'product': reverse('product', request=request, format=format),
#         'category': reverse('category', request=request, format=format),
#         'news': reverse('news', request=request, format=format),
#         'gallery': reverse('gallery', request=request, format=format),
#     })
#     return response