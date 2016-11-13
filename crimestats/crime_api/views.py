"""REST views."""
from rest_framework.decorators import api_view
from rest_framework.response import Response

from year.models import Years


@api_view()
def single_year_view(request, *args, **kwargs):
    """Send single year info."""
    filter_by = kwargs['year']
    to_show = Years.objects.get(year=filter_by)

    return Response({'year': to_show.year,
                    'population': to_show.population,
                    'total': to_show.total,
                    'violent': to_show.violent,
                    'prop': to_show.prop,
                    'murder': to_show.murder,
                    'rape': to_show.rape,
                    'robbery': to_show.robbery,
                    'assault': to_show.assault,
                    'burglary': to_show.burglary,
                    'theft': to_show.theft,
                    'gta': to_show.gta})
