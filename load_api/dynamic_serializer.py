from load_api.models import Budget
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import BindingDict
from collections import OrderedDict

data = {"guid":"ED50707B-21A4-43C3-B91D-FDF40BA305DA","test":"ACTIVE","code":"01021251","name":"Бюджет Республики Башкортостан","parentcode":"99010001","budglevelcode":"2","budgtypecode":"02","okatocode":"","oktmocode":"80000000","foorgcode":"","foorgcodeubp":"04381","tofkcode":"0100","opendate":"2014-01-01 00:00:00.0","closedate":"","startdate":"2014-01-01 16:20:41.0","enddate":"","filedate":"2020-07-31 09:28:48.0","loaddate":"2020-08-03 22:05:59.0"}
data_many = [{"guid":"ED50707B-21A4-43C3-B91D-FDF40BA305DA","status":"ACTIVE","code":"01021251","name":"Бюджет Республики Башкортостан","parentcode":"99010001","budglevelcode":"2","budgtypecode":"02","okatocode":"","oktmocode":"80000000","foorgcode":"","foorgcodeubp":"04381","tofkcode":"0100","opendate":"2014-01-01 00:00:00.0","closedate":"","startdate":"2014-01-01 16:20:41.0","enddate":"","filedate":"2020-07-31 09:28:48.0","loaddate":"2020-08-03 22:05:59.0"},{"guid":"6865A22D-84E9-436E-9E5B-B14E24685CE6","status":"ACTIVE","code":"01030059","name":"Бюджет муниципального района Бакалинский район Республики Башкортостан","parentcode":"01021251","budglevelcode":"3","budgtypecode":"05","okatocode":"","oktmocode":"80607000","foorgcode":"","foorgcodeubp":"р2965","tofkcode":"0100","opendate":"2014-01-01 00:00:00.0","closedate":"","startdate":"2014-01-01 18:44:42.0","enddate":"","filedate":"2019-04-29 21:31:25.0","loaddate":"2019-05-02 22:16:25.0"}]


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = None


class SerializerMaker:
    def __init__(self, base_serializer=GeneralSerializer) -> None:
        self.base_serializer = base_serializer

    def make_serializer(self, model):
        self.base_serializer.Meta.model = model
        self.base_serializer.Meta.fields = self.get_fields(model)

        return self.base_serializer

    def get_fields(self, model):
        fields = [field.name for field in model._meta.fields if not field.auto_created]

        return fields
