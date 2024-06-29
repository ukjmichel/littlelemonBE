from  rest_framework.serializers import ModelSerializer ,CharField, ValidationError
from django.contrib.auth.models import User
from .models import Menu,Booking


class MenuSerializer (ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title','price', 'inventory']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date"]


class UserRegistrationSerializer(ModelSerializer):
    password1 = CharField(write_only=True, style={"input_type": "password"})
    password2 = CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise ValidationError({"password2": "Passwords do not match"})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password1"],
        )
        return user
