from rest_framework import serializers
from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        min_value=1,
        max_value=1914
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        required=False
    )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in [
            "manufacturer",
            "model",
            "horse_powers",
            "is_broken",
            "problem_description"
        ]:
            setattr(
                instance,
                field,
                validated_data.get(
                    field,
                    getattr(instance, field)
                )
            )
        instance.save()
        return instance
