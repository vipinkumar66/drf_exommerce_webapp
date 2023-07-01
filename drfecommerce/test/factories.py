import factory

from drfecommerce.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "brand_category"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "Product_category"
    description = "Product_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
