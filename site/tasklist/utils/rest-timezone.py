
class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''Class to make output of a DateTime Field timezone aware
    '''
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ('id', 'branch', 'date', 'length', 'wait_time',)

    date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')