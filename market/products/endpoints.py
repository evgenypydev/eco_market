from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cloudinary.uploader import upload

from .models import Product, Category
from .serializers import ProductCRUDSerializer, CategoryCRUDSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCRUDSerializer

    def create(self, request, *args, **kwargs):
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            image_response = upload(
                image,
                folder="image/",
                transformation=[
                    {"width": "auto", "crop": "scale"},
                    {'quality': "auto:best"},
                    {'fetch_format': "auto"}
                ],
                resource_type='auto'
            )
            request.data['image'] = image_response['secure_url']

        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Product added successfully.'}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.FILES.get('image'):
            image = request.FILES.get('image')
            image_response = upload(
                image,
                folder="image/",
                transformation=[
                    {"width": "auto", "crop": "scale"},
                    {'quality': "auto:best"},
                    {'fetch_format': "auto"}
                ],
                resource_type='auto'
            )
            request.data['image'] = image_response['secure_url']

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Product edited successfully.'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Product.objects.filter(category=category)
        return super().get_queryset()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategoryCRUDSerializer
    queryset = Category.objects.all()

    def create(self, request, *args, **kwargs):
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            image_response = upload(
                image,
                folder="image/",
                transformation=[
                    {"width": "auto", "crop": "scale"},
                    {'quality': "auto:best"},
                    {'fetch_format': "auto"}
                ],
                resource_type='auto'
            )
            request.data['image'] = image_response['secure_url']

        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Category added successfully.'}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.FILES.get('image'):
            image = request.FILES.get('image')
            image_response = upload(
                image,
                folder="image/",
                transformation=[
                    {"width": "auto", "crop": "scale"},
                    {'quality': "auto:best"},
                    {'fetch_format': "auto"}
                ],
                resource_type='auto'
            )
            request.data['image'] = image_response['secure_url']

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Category edited successfully.'}, status=status.HTTP_200_OK)




