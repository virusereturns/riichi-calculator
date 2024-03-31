from rest_framework import serializers


class ScoreInputSerializer(serializers.Serializer):
    han = serializers.IntegerField()
    fu = serializers.IntegerField()
    honba = serializers.IntegerField()
    is_dealer = serializers.BooleanField()
    kiriage = serializers.BooleanField()

    def validate_han(self, value):
        """
        Check that han is greater than 0.
        """
        if value <= 0:
            raise serializers.ValidationError("Han must be greater than 0.")
        return value

    def validate_fu(self, value):
        """
        Check that fu is between 20 and 110.
        """
        if not (20 <= value <= 110):
            raise serializers.ValidationError("Fu must be between 20 and 110.")
        return value

    def validate(self, data):
        """
        Check that the combination of han and fu is not (1, 20) or (1, 25).
        """
        han = data.get('han')
        fu = data.get('fu')

        if (han, fu) in [(1, 20), (1, 25)]:
            raise serializers.ValidationError("Invalid score combination.")

        return data
