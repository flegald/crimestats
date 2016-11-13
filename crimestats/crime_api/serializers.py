"""crime statsapi serializers."""

from rest_framework import serializers
from year.models import Years


class YearSerializer(serializers.ModelSerializer):
    """Year Serializer."""

    class Meta:
        """Meta."""

        model = Years

        fields = ['year', 'population', 'total', 'violent',
                    'prop', 'murder', 'rape', 'robbery', 'assault',
                    'burglary', 'theft', 'gta']
