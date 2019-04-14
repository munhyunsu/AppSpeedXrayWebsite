from rest_framework import serializers
from xray.models import Xray


class XraySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Xray
        fields = ('package_name', 'experiment_date', 'scene_start', 'scene_end', 'raw_si', 'raw_fp',
                  'raw_cs', 'raw_ll', 'raw_rt', 'ps', 'per_si', 'per_fp', 'per_cs', 'per_ll', 'per_rt')
