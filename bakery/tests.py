from django.test import TestCase
from .models import YourModelName  # Replace with your actual model name

class BakeryModelTests(TestCase):
    def test_example(self):
        # Example test case
        instance = YourModelName.objects.create(field_name='value')  # Replace with actual fields
        self.assertEqual(instance.field_name, 'value')  # Replace with actual assertions

    # Add more test cases as needed